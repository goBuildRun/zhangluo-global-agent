# Zhangluo (小張羅) — Fiduciary Household & Taste Orchestration Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Architecture: OpenViking Memory](https://img.shields.io/badge/Memory-OpenViking%20Auditable-5B8C7A)](#architecture)
[![Integrations: Qloo | Nebius NVIDIA | PayPal Sandbox | Tavily](https://img.shields.io/badge/Integrations-Qloo%20%7C%20Nebius%20NVIDIA%20%7C%20PayPal%20%7C%20Tavily-D4A056)](#sponsor-integrations)

> **顺时而动，不时不食；知你所念，莼鲈在心；去伪存真，不逐热榜；懂味之后，替你张罗。**  
> *"Move with the season; remember what matters at home; filter out paid ad noise; orchestrate with fiduciary trust."*

**Zhangluo (小張羅)** is a **Fiduciary Personal & Household Life Orchestrator** built around a strict 6-stage closed loop:
`Know Who You Are (Auditable Memory) ➔ Judge Why Now (24 Solar Terms & Phenology) ➔ Find Taste-Aligned Options (Qloo Taste AI + 2,843-County Terroir Anti-Noise Engine) ➔ Explain Why It's Not Paid Ad Noise ➔ Deliver Actionable Orchestration Cards (PayPal Agentic Commerce) ➔ Learn With Explicit Consent.`

---

## 🌟 Core Differentiators (Why Zhangluo Is Not Another Chatbot)

1. **Four Integrated Life Tabs (`Orchestrate 找张罗` · `Household Ledger 起居簿` · `Solar Terroir 风物志` · `Sovereign Memory 自留地`)**
   - **Household Spatial Memory (`起居簿`)**: Snap a photo or speak a sentence (*"Put the winter duvet on the top shelf of the guest closet"*). Before recommending any purchase, Zhangluo checks your existing household inventory first to prevent duplicate buying.
   - **2,843-County Terroir & 10-Year Anti-Noise Filter (`风物志`)**: Powered by `PostGIS + pgvector` and grounded in **Qloo's Cultural Taste Graph**, Zhangluo rejects paid ad rankings by enforcing a strict **Anti-Noise Contract**: operating history $\ge 10\text{ years}$, $\le 2$ branches (no franchise chains), national Geographic Indication (`GI`) standards, and 24 Solar Term phenology windows.
   - **OpenViking Auditable Sovereign Memory & Discovery Pool (`自留地`)**: Preferences inferred from conversation enter a `pending` queue first and never alter your long-term profile without explicit confirmation (`consent_id`). Real-world gems discovered by users are private by default and only enter the shared **Proof-of-Taste Discovery Pool** after opt-in anonymization and POI verification.
   - **Fiduciary Agentic Commerce (`买得对 & 服务妥`)**: Rankings are never manipulated by ad spend or CPS commissions. Once a user approves an Orchestration Card, checkout is executed safely via **PayPal Sandbox Orders v2** with full uncertainty disclosure and inventory write-back.

---

## 🔌 Sponsor & Ecosystem Integrations

| Integration Module | Endpoint / SDK Used | Role in Zhangluo's 6-Stage Loop |
| :--- | :--- | :--- |
| **Qloo Taste AI API** | `GET /v2/insights` (`QLOO_API_KEY`) | Cross-grounds user taste preferences and 24-solar-term terroir items (`好物·好地·好店`) against Qloo's global cultural taste graph, computing an explainable **Cultural Taste Affinity Score** without invasive tracking. |
| **Nebius Token Factory × NVIDIA Models** | `POST https://api.studio.nebius.ai/v1/chat/completions` (`nvidia/Llama-3.1-Nemotron-70B-Instruct-HF`) | Powers multi-modal intent slot extraction, Household Ledger spatial reasoning, and structured Fiduciary Orchestration Card synthesis. |
| **Tavily Search API** | `POST https://api.tavily.com/search` (`TAVILY_API_KEY`) | Real-time verification of merchant longevity, warranty terms, and cross-platform price/stock snapshots to enforce our zero-hallucination evidence gate. |
| **PayPal Agentic Commerce Sandbox** | `POST https://api-m.sandbox.paypal.com/v2/checkout/orders` (`PAYPAL_CLIENT_ID` / `SECRET`) | Executes user-authorized fiduciary purchases and household service bookings directly from an Orchestration Card, automatically updating the `Household Ledger (起居簿)`. |

---

## 🚀 Quick Start (Run Live Demo in 30 Seconds)

No heavy external setup is required to test the end-to-end demo. When API keys are provided via environment variables, the server calls live endpoints; otherwise, it automatically uses deterministic, realistic sandbox fixtures so judges can test every workflow immediately.

```bash
# 1. Start the Zhangluo Hackathon Adapter Server (Python 3.10+, zero external dependency required)
python3 server.py --port 8765

# 2. Open in browser:
# http://127.0.0.1:8765
```

### Optional Environment Variables for Live API Calls
```bash
export QLOO_API_KEY="your_qloo_api_key"
export NEBIUS_API_KEY="your_nebius_token_factory_key"
export TAVILY_API_KEY="your_tavily_api_key"
export PAYPAL_CLIENT_ID="your_paypal_sandbox_client_id"
export PAYPAL_CLIENT_SECRET="your_paypal_sandbox_secret"
```

### Run Automated Verification Suite
```bash
pytest tests/test_zhangluo_hackathon_adapter.py -v
```
