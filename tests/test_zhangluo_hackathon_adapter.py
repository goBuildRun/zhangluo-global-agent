"""
Automated verification tests for the Zhangluo Hackathon Adapter (Full Real-Codebase Aligned Edition).
"""

from __future__ import annotations

import sys
from pathlib import Path

ADAPTER_DIR = Path(__file__).resolve().parents[1]
if str(ADAPTER_DIR) not in sys.path:
    sys.path.insert(0, str(ADAPTER_DIR))

from server import handle_api_request


def test_initial_state_includes_all_real_zhangluo_modules() -> None:
    res = handle_api_request("GET", "/api/state", {})
    assert res["ok"] is True
    assert res["solar_term"]["code"] == "shuangjiang"
    assert len(res["ios_plugins"]) >= 4
    assert len(res["granary_items"]) >= 3
    assert len(res["household_ledger"]) >= 3
    assert len(res["guest_notes"]) >= 2
    assert len(res["gift_records"]) >= 1
    assert len(res["taste_graph_nodes"]) >= 5


def test_video_sweep_12s_keyframe_batch_intake() -> None:
    before_count = len(handle_api_request("GET", "/api/state", {})["household_ledger"])
    res = handle_api_request(
        "POST",
        "/api/video-sweep",
        {"room_name": "North Balcony Storage & Dining Sideboard"},
    )
    assert res["ok"] is True
    assert res["sweep"]["duration_sec"] == 12
    assert res["sweep"]["sampling_interval_ms"] == 750
    assert len(res["sweep"]["keyframes_extracted"]) == 2
    assert len(res["household_ledger"]) == before_count + 2


def test_orchestrate_qloo_and_nebius_tavily_grounding() -> None:
    res = handle_api_request(
        "POST",
        "/api/orchestrate",
        {
            "query": "Frost's Descent dinner for Mr. Wang (gout low-purine) and return gift for Old Chen.",
            "scenario": "qloo",
        },
    )
    assert res["ok"] is True
    orch = res["latest_orchestration"]
    assert len(orch["six_stage_chain"]) == 6
    assert orch["sponsor_telemetry"]["qloo"]["cultural_taste_clusters"][0]["affinity_score"] >= 0.90
    assert orch["sponsor_telemetry"]["nebius_nvidia_tavily"]["tavily_search_verifier"]["enabled"] is True


def test_paypal_fiduciary_checkout_and_gift_reciprocity_sync() -> None:
    res = handle_api_request(
        "POST",
        "/api/paypal-checkout",
        {"item_id": "tr-good-001", "quantity": 1},
    )
    assert res["ok"] is True
    receipt = res["receipt"]
    assert receipt["paypal_order_id"].startswith("PAYPAL-SANDBOX-")
    assert len(receipt["comparison_digest"]) == 64
    assert res["gift_records"][0]["status"] == "completed_via_paypal"


def test_openviking_memory_consent_and_proof_of_taste() -> None:
    res_confirm = handle_api_request(
        "POST",
        "/api/memory-consent",
        {"memory_id": "mem-003", "action": "confirm"},
    )
    assert res_confirm["ok"] is True
    assert res_confirm["updated_memory"]["status"] == "CONFIRMED"

    res_pot = handle_api_request(
        "POST",
        "/api/proof-of-taste",
        {"note": "28-year non-chain wild mushroom noodle shop", "city": "Changshu, Suzhou"},
    )
    assert res_pot["ok"] is True
    assert res_pot["attestation"]["purity_grade"] == "AAA"
