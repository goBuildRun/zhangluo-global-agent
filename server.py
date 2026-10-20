#!/usr/bin/env python3
"""
Zhangluo (小張羅) Hackathon Interactive Demo & API Server (Full Real-Codebase Aligned Edition).
"""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any, Dict

from integrations import SOLAR_TERM_CONTEXT, ZhangluoHackathonEngine

ENGINE = ZhangluoHackathonEngine()
STATIC_DIR = Path(__file__).resolve().parent / "static"


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
        if clean_path.startswith("/api/"):
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
