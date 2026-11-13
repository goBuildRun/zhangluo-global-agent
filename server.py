#!/usr/bin/env python3
"""
Zhangluo (小張羅) Hackathon Interactive Demo & API Server (Full Real-Codebase Aligned Edition).
"""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import hashlib
from typing import Any, Dict

from firebase_hybrid_ai import compute_keyframe_diff_filter, route_hybrid_inference
from integrations import SOLAR_TERM_CONTEXT, ZhangluoHackathonEngine

ENGINE = ZhangluoHackathonEngine()
ROOT_DIR = Path(__file__).resolve().parent
STATIC_DIR = ROOT_DIR / "static"
AGENT_MANIFEST_PATH = ROOT_DIR / ".well-known" / "agent.json"


def handle_api_request(method: str, path: str, body: Dict[str, Any]) -> Dict[str, Any]:
    if method == "GET" and path == "/api/state":
        initial_orch = ENGINE.orchestrate(
            "Frost's Descent orchestration: check winter duvet & storage boxes, plan low-purine dinner for Mr. Wang using expiring granary bamboo shoots, and prepare return gift for Old Chen.",
            scenario="all",
        )
        return {
            "ok": True,
            "solar_term": SOLAR_TERM_CONTEXT,
            "ios_plugins": ENGINE.ios_plugins,
            "granary_items": ENGINE.granary_items,
            "household_ledger": ENGINE.household_ledger,
            "guest_notes": ENGINE.guest_notes,
            "gift_records": ENGINE.gift_records,
            "terroir_assets": ENGINE.terroir_assets,
            "taste_graph_nodes": ENGINE.taste_graph_nodes,
            "memories": ENGINE.memories,
            "orders": ENGINE.orders,
            "attestations": ENGINE.proof_of_taste_attestations,
            "video_sweep_runs": ENGINE.video_sweep_runs,
            "latest_orchestration": initial_orch,
        }

    if method == "POST" and path == "/api/orchestrate":
        query = str(body.get("query") or "Orchestrate Frost's Descent household tasks and terroir.")
        scenario = str(body.get("scenario") or "all")
        result = ENGINE.orchestrate(query=query, scenario=scenario)
        return {
            "ok": True,
            "latest_orchestration": result,
            "household_ledger": ENGINE.household_ledger,
        }

    if method == "POST" and path == "/api/video-sweep":
        room_name = str(body.get("room_name") or "North Balcony Storage & Dining Sideboard")
        sweep = ENGINE.run_video_sweep_simulation(room_name=room_name)
        return {
            "ok": True,
            "sweep": sweep,
            "household_ledger": ENGINE.household_ledger,
            "video_sweep_runs": ENGINE.video_sweep_runs,
        }

    if method == "POST" and path == "/api/paypal-checkout":
        item_id = str(body.get("item_id") or "tr-good-003")
        quantity = int(body.get("quantity") or 1)
        receipt = ENGINE.execute_paypal_checkout(item_id=item_id, quantity=quantity)
        return {
            "ok": True,
            "receipt": receipt,
            "orders": ENGINE.orders,
            "household_ledger": ENGINE.household_ledger,
            "gift_records": ENGINE.gift_records,
        }

    if method == "POST" and path == "/api/memory-consent":
        memory_id = str(body.get("memory_id") or "mem-003")
        action = str(body.get("action") or "confirm")
        updated = ENGINE.update_memory_consent(memory_id=memory_id, action=action)
        return {
            "ok": True,
            "updated_memory": updated,
            "memories": ENGINE.memories,
        }

    if method == "POST" and path == "/api/proof-of-taste":
        note = str(body.get("note") or "Found a 28-year single-hearth wild mushroom noodle shop at foot of Yushan Mountain.")
        city = str(body.get("city") or "Changshu, Suzhou")
        record = ENGINE.mint_proof_of_taste_discovery(note_en=note, city=city)
        return {
            "ok": True,
            "attestation": record,
            "attestations": ENGINE.proof_of_taste_attestations,
        }

    if method == "POST" and path == "/api/hybrid-ai/infer":
        task_type = str(body.get("task_type") or "multi_constraint_orchestration")
        prompt = str(body.get("prompt") or "Check Study Tatami 65L storage box duplicate and plan low-purine dinner.")
        network_online = bool(body.get("network_online", True))
        constraints_count = int(body.get("constraints_count") or 4)
        has_unmasked_pii = bool(body.get("has_unmasked_pii", False))
        frames = body.get("frames") or [
            {"diff_score": 0.0, "contains_pii": False, "labels": ["65L Moisture-Proof Storage Box"]},
            {"diff_score": 0.012, "contains_pii": False, "labels": ["65L Moisture-Proof Storage Box"]},
            {"diff_score": 0.048, "contains_pii": True, "labels": ["Xinhui 5-Year Chenpi Tin", "Family Address Label"]},
            {"diff_score": 0.009, "contains_pii": False, "labels": ["Xinhui 5-Year Chenpi Tin"]},
            {"diff_score": 0.062, "contains_pii": False, "labels": ["Lin'an Winter Bamboo Shoots"]},
        ]
        sweep_filter = compute_keyframe_diff_filter(frames)
        routing = route_hybrid_inference(
            task_type=task_type,
            prompt=prompt,
            network_online=network_online,
            constraints_count=constraints_count,
            has_unmasked_pii=has_unmasked_pii,
        )
        return {
            "ok": True,
            "hybrid_routing": routing,
            "on_device_sweep_filter": sweep_filter,
        }

    if method == "GET" and path == "/.well-known/agent.json":
        manifest = json.loads(AGENT_MANIFEST_PATH.read_text(encoding="utf-8"))
        manifest["ok"] = True
        return manifest

    if method == "POST" and path == "/api/webmcp":
        rpc_id = body.get("id", 1)
        rpc_method = str(body.get("method") or "tools/list")
        params = body.get("params") or {}
        manifest = json.loads(AGENT_MANIFEST_PATH.read_text(encoding="utf-8"))
        tools = manifest["webmcp"]["tools"]

        if rpc_method == "tools/list":
            return {
                "ok": True,
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "agent_id": manifest["agent_id"],
                    "standard": manifest["standard"],
                    "tools": tools,
                },
            }

        if rpc_method == "tools/call":
            tool_name = str(params.get("name") or "check_duplicate_inventory")
            args = params.get("arguments") or {}
            if tool_name == "check_duplicate_inventory":
                q = str(args.get("item_query") or "65L Moisture-Proof Airtight Storage Box")
                req_qty = int(args.get("requested_qty") or 2)
                matched = [
                    h
                    for h in ENGINE.household_ledger
                    if any(tok in h["item_en"].lower() for tok in q.lower().split() if len(tok) >= 3)
                ] or ENGINE.household_ledger[:1]
                recommended_qty = max(0, req_qty - 1)
                payload = {
                    "tool": tool_name,
                    "item_query": q,
                    "requested_qty": req_qty,
                    "existing_household_match": matched[0]["item_en"],
                    "storage_location": matched[0]["location_en"],
                    "recommended_net_order_qty": recommended_qty,
                    "fiduciary_savings_usd": 19.50 if recommended_qty < req_qty else 0.0,
                    "privacy_boundary": "local_browser_runtime_0_cloud_bytes",
                }
            elif tool_name == "verify_merchant_purity":
                q = str(args.get("category_or_query") or "Aged Xinhui Chenpi & Autumn Terroir")
                candidates = ENGINE.terroir_assets[:2]
                digest_input = "|".join(f"{c['id']}:{c['price_usd']}:{c['purity_grade']}" for c in candidates)
                digest = hashlib.sha256(digest_input.encode("utf-8")).hexdigest()
                payload = {
                    "tool": tool_name,
                    "query": q,
                    "ad_boost_applied": "0.0%",
                    "verified_candidates": [
                        {
                            "id": c["id"],
                            "title": c["title_en"],
                            "purity_grade": c["purity_grade"],
                            "price_usd": c["price_usd"],
                            "standard_code": c["standard_code"],
                        }
                        for c in candidates
                    ],
                    "comparison_digest_sha256": digest,
                }
            else:
                act = str(args.get("action") or "inspect_pending")
                mem_id = str(args.get("memory_id") or "mem-003")
                if act in ("confirm", "revoke"):
                    updated = ENGINE.update_memory_consent(memory_id=mem_id, action=act)
                    payload = {
                        "tool": "request_consent_memory",
                        "mutation_applied": True,
                        "updated_memory": updated,
                    }
                else:
                    payload = {
                        "tool": "request_consent_memory",
                        "mutation_applied": False,
                        "policy": "External agents cannot mutate profile without user consent_id signature",
                        "pending_memories": [
                            {"id": m["id"], "consent_id": m["consent_id"], "status": m["status"], "statement": m["statement_en"]}
                            for m in ENGINE.memories
                        ],
                    }

            return {
                "ok": True,
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(payload, ensure_ascii=False)}],
                    "structuredContent": payload,
                },
            }

        return {"ok": False, "jsonrpc": "2.0", "id": rpc_id, "error": {"code": -32601, "message": f"Method not found: {rpc_method}"}}

    return {"ok": False, "error": f"Unknown endpoint {method} {path}"}


class ZhangluoRequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, data: Dict[str, Any], status: int = 200) -> None:
        raw = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:  # noqa: N802
        clean_path = self.path.split("?", 1)[0]
        if clean_path.startswith("/api/") or clean_path == "/.well-known/agent.json":
            res = handle_api_request("GET", clean_path, {})
            self._send_json(res, 200 if res.get("ok") else 404)
            return

        index_file = STATIC_DIR / "index.html"
        content = index_file.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self) -> None:  # noqa: N802
        clean_path = self.path.split("?", 1)[0]
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw_body = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
        try:
            body = json.loads(raw_body) if raw_body else {}
        except Exception:
            body = {}
        res = handle_api_request("POST", clean_path, body)
        self._send_json(res, 200 if res.get("ok") else 400)

    def log_message(self, fmt: str, *args: Any) -> None:
        return


def main() -> None:
    parser = argparse.ArgumentParser(description="Zhangluo Hackathon Adapter Server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    httpd = HTTPServer((args.host, args.port), ZhangluoRequestHandler)
    print(f"Zhangluo (小張羅) Hackathon Live Server running at http://{args.host}:{args.port}")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
