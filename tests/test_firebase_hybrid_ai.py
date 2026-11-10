import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from firebase_hybrid_ai import compute_keyframe_diff_filter, route_hybrid_inference
from server import handle_api_request


def test_on_device_keyframe_diff_and_pii_masking():
    frames = [
        {"diff_score": 0.0, "contains_pii": False, "labels": ["65L Box"]},
        {"diff_score": 0.011, "contains_pii": False, "labels": ["65L Box"]},
        {"diff_score": 0.049, "contains_pii": True, "labels": ["Chenpi", "Home Mail"]},
        {"diff_score": 0.008, "contains_pii": False, "labels": ["Chenpi"]},
        {"diff_score": 0.055, "contains_pii": False, "labels": ["Bamboo Shoots"]},
    ]
    res = compute_keyframe_diff_filter(frames, threshold=0.035)
    assert res["total_sampled_frames"] == 5
    assert res["retained_keyframes_count"] == 3
    assert res["discarded_redundant_frames"] == 2
    assert res["pii_frames_masked_locally"] == 1
    assert res["cloud_bandwidth_saved_pct"] == 40.0


def test_hybrid_routing_privacy_and_offline_fallback():
    # 1. Unmasked PII strictly blocked from cloud -> runs on-device Gemini Nano
    r_pii = route_hybrid_inference("multi_constraint", "scan room", network_online=True, constraints_count=4, has_unmasked_pii=True)
    assert r_pii["selected_route"] == "ON_DEVICE_GEMINI_NANO"

    # 2. Single-slot duplicate check -> runs on-device
    r_local = route_hybrid_inference("duplicate_check", "do we own 65L box?", network_online=True, constraints_count=1)
    assert r_local["selected_route"] == "ON_DEVICE_GEMINI_NANO"

    # 3. Offline multi-constraint -> automatic fallback to on-device Gemini Nano
    r_offline = route_hybrid_inference("multi_constraint", "plan dinner", network_online=False, constraints_count=4)
    assert r_offline["selected_route"] == "ON_DEVICE_GEMINI_NANO_FALLBACK"

    # 4. Online multi-constraint (PII masked) -> escalates to Cloud Gemini Flash via Firebase AI Logic
    r_cloud = route_hybrid_inference("multi_constraint", "plan dinner + GI terroir", network_online=True, constraints_count=4)
    assert r_cloud["selected_route"] == "CLOUD_GEMINI_FLASH_VIA_FIREBASE"


def test_server_hybrid_endpoint():
    resp = handle_api_request("POST", "/api/hybrid-ai/infer", {"task_type": "multi_constraint", "constraints_count": 4})
    assert resp["ok"] is True
    assert resp["hybrid_routing"]["selected_route"] == "CLOUD_GEMINI_FLASH_VIA_FIREBASE"
    assert resp["on_device_sweep_filter"]["retained_keyframes_count"] == 3
