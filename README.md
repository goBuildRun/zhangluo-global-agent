# Zhangluo — Fiduciary Household, Hybrid AI & Sovereign Edge Steward

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Live Web Demo: Zero-Login Interactive Workbench](https://img.shields.io/badge/🚀%20Launch%20Live%20Web%20Demo-GitHub%20Pages-2563EB)](https://gobuildrun.github.io/zhangluo-global-agent/)
[![Hybrid AI: Chrome Gemini Nano ⇄ Firebase AI Logic](https://img.shields.io/badge/Hybrid_AI-Chrome_Gemini_Nano_%E2%87%84_Firebase_AI_Logic-10B981)](https://gobuildrun.github.io/zhangluo-global-agent/?mode=hybrid-ai)
[![Edge NAS: UGREEN UGOS Pro Docker Vault](https://img.shields.io/badge/Edge_Vault-UGREEN_NAS_UGOS_Pro-5B8C7A)](https://gobuildrun.github.io/zhangluo-global-agent/?mode=ugreen)
[![Demo Video: YouTube 1080p](https://img.shields.io/badge/🎥%20Watch%20Demo%20Video-YouTube%201080p-red)](https://youtu.be/1wwW4HmMAUA)

> 🚀 **Try the Live Zero-Install Browser Workbench (No Login or Setup Required)**:
> - 🧠 **Hybrid AI Mode (`Chrome Built-in Gemini Nano ⇄ Firebase AI Logic`)**: **[https://gobuildrun.github.io/zhangluo-global-agent/?mode=hybrid-ai](https://gobuildrun.github.io/zhangluo-global-agent/?mode=hybrid-ai)**
> - 🗄️ **UGREEN AI NAS Mode (`UGOS Pro` DXP4800 Plus Local RAID-1 Vault)**: **[https://gobuildrun.github.io/zhangluo-global-agent/?mode=ugreen](https://gobuildrun.github.io/zhangluo-global-agent/?mode=ugreen)**
> - 💳 **Fiduciary Commerce Mode (`PayPal Orders v2 + Duplicate-Buy Guard`)**: **[https://gobuildrun.github.io/zhangluo-global-agent/?mode=paypal](https://gobuildrun.github.io/zhangluo-global-agent/?mode=paypal)**
>
> 🎬 **Watch the 1m48s 1080p English-Narrated Demo Video**: **[https://youtu.be/1wwW4HmMAUA](https://youtu.be/1wwW4HmMAUA)**
> - **`0:00 - 0:28` ⚡ The 30-Second Aha Moment**: 12-Second `VideoSweepRecorder` (`750ms` pixel-diff $\ge 0.035$) scans a home pantry/closet and **intercepts a duplicate purchase before checkout** (`-$19.50` saved).
> - **`0:29 - 0:58` 🧭 Anti-Paid-Ad Merchant & Price Verification**: Enforcing $\ge 10\text{ yr}$ operating longevity, $\le 2$ branches, and cryptographic `comparison_digest` verification.
> - **`0:59 - 1:25` 🧠 On-Device Medical Redline Gate & Auditable Memory (`OpenViking`)**: Sensitive family health redlines (gout purine limits, Rx prescriptions, child peanut allergies) stay **100% On-Device (`0 bytes uploaded to cloud`)** with explicit `consent_id` auditability.
> - **`1:26 - 1:48` 💳 Fiduciary Agentic Checkout**: `comparison_digest` SHA-256 price/spec audit + **PayPal Sandbox Orders v2** settlement with automatic home inventory write-back.

---

## 🧠 Hybrid AI & Edge NAS Architecture (`firebase_hybrid_ai.py`)

Families refuse to upload sensitive medical dietary redlines (e.g., severe gout purine limits, prescription medications, child peanut anaphylaxis), private home camera sweeps, or financial receipts to third-party cloud LLMs. **Zhangluo** solves this via a deterministic **Hybrid AI Privacy Router ([`firebase_hybrid_ai.py`](./firebase_hybrid_ai.py))**:

| Task / Data Sensitivity | Execution Target | Model / Runtime Used | Privacy & Latency Guarantee |
| :--- | :--- | :--- | :--- |
| **1. Medical Allergies, Prescriptions & Home Camera Sweeps** | `ON_DEVICE_GEMINI_NANO` | **On-Device `Gemini Nano 4` (`window.ai` Web/Android) & `Apple Foundation Models` (iOS)** + Local **UGREEN NAS (`UGOS Pro`)** Docker Index | **`0 bytes` sent to cloud**; `~18ms` local inference; works 100% offline. |
| **2. Public Recipe Synthesis, Merchant Grounding & Elder Read-Aloud** | `CLOUD_FIREBASE_GEMINI_FLASH` | **Google Firebase AI Logic Zero-Billing Free Tier (`gemini-3.8-flash`, `gemini-3.5-flash-lite` & `gemini-3.1-flash-tts-preview`)** | Structured JSON synthesis (`~410ms`) + elder-friendly audio readback over public non-PII metadata (`billing not required`). |
| **3. Airplane Mode / Offline Resilience (`navigator.onLine == false`)** | `OFFLINE_LOCAL_FALLBACK` | **On-Device `Gemini Nano 4` / `Apple Foundation Models`** | Seamless zero-crash failover to on-device inference when Wi-Fi or cellular drops. |

> 📚 **Official Specifications & Workshop Synchronization**:
> - **Google #BuildHybridAI 2026 Standards (Submissions Now Open)**: Aligned with Google's official hybrid inference architecture ([firebase.google.com/docs/ai-logic/hybrid](https://firebase.google.com/docs/ai-logic/hybrid)) and the official [Firebase AI Logic Free-Tier Models Catalog](https://firebase.google.com/docs/ai-logic/models) (`billing not required`: `gemini-3.8-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-tts-preview`, paired with on-device `Gemini Nano 4` on Web/Android and `Apple Foundation Models` on iOS) so judges can test anytime without expiring 4-day sprint billing quotas. Live Firebase Build Session with Cynthia Jiang runs Thursday, Nov 12 at 10:00 AM PT ([RSVP via Luma](https://luma.com/bapqqd3n)); submission portal is officially open through Monday, Nov 30 at 2:00 PM PT (`2026-12-01 06:00 UTC+8`).
> - **UGREEN UGOS Pro Open Smart-Home Hub**: Per official UGREEN NAS architectural guidelines ([community.ugreen.com](https://community.ugreen.com/nas/#/pagesD/circle/post?id=1548)), Zhangluo deploys seamlessly alongside **Home Assistant** in Docker and **Surveillance Center**, enabling private local automation and camera sweeps around data already secured on local RAID-1 storage.

---

## 🌟 Core Differentiators (Why Zhangluo Is Not Another Chatbot)

1. **Five Integrated Workbench Tabs (`⚡ Hybrid AI & NAS` · `🧭 Orchestrate` · `📦 Home Inventory` · `🛡️ Anti-Ad Filter` · `🔒 Consent Memory`)**
   - **Pre-Checkout Duplicate-Purchase Interceptor (`📦 Home Inventory`)**: Run a 12-second continuous camera sweep (`VideoSweepRecorder`, `750ms` keyframe diff $\ge 0.035$). Before recommending any purchase, Zhangluo checks your existing household inventory first (e.g., detecting 1 spare 65L storage box in the study closet and reducing your order from 2 to 1, **saving \$19.50 immediately**).
   - **On-Device Medical & Allergy Redline Gate (`⚡ Hybrid AI & NAS`)**: Automatically detects sensitive health constraints (`gout`, `purine`, `colchicine`, `peanut`, `allergy`, `prescription`) and forces execution onto **Chrome Built-in Gemini Nano** and local **UGREEN NAS RAID-1 storage (`/volume1/docker/zhangluo-vault`)** so family health data never leaves the home LAN.
   - **OpenViking Auditable Sovereign Memory (`🔒 Consent Memory`)**: Preferences inferred from conversation enter a `pending` queue first and never alter your long-term profile without explicit confirmation (`consent_id`).
   - **Fiduciary Agentic Commerce (`🧭 Orchestrate`)**: Rankings are never manipulated by ad spend or CPS commissions. Once a user approves an Orchestration Card, checkout is executed safely via **PayPal Sandbox Orders v2** with SHA-256 `comparison_digest` verification and automatic inventory write-back.

---

## 🔌 Ecosystem & Sponsor Modules

| Integration Module | Endpoint / SDK / File | Role in Zhangluo's Fiduciary Loop |
| :--- | :--- | :--- |
| **Google Firebase AI Logic × Chrome Built-in AI** | [`firebase_hybrid_ai.py`](./firebase_hybrid_ai.py) (`POST /api/hybrid-ai/infer`) | Routes sensitive medical/PII/camera-sweep tasks to **On-Device `Gemini Nano 4` / `Apple Foundation Models` (`0 cloud bytes`)** and public reasoning/TTS to **Firebase AI Logic Zero-Billing Free Tier (`gemini-3.8-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-tts-preview`)** with offline fallback. |
| **UGREEN AI NAS (`UGOS Pro` Docker Vault)** | Local RAID-1 SQLite + `pgvector` (`/volume1/docker/zhangluo-vault`) | Stores 12-second camera sweep keyframes, appliance maintenance schedules, and `OpenViking` `consent_id` logs on home LAN hardware with zero cloud upload. |
| **PayPal Agentic Commerce Sandbox** | `POST https://api-m.sandbox.paypal.com/v2/checkout/orders` | Executes user-authorized fiduciary purchases after pre-checkout inventory deduplication, automatically syncing receipts back to Home Inventory. |
| **Multi-Constraint Reasoning & Web Verification** | [`integrations.py`](./integrations.py) (`Llama-3.1-Nemotron-70B` + `Tavily` + `Qloo`) | Enforces $\ge 10\text{ yr}$ merchant longevity, zero constraint drops on multi-guest dietary rules, and live stock/warranty verification. |

---

## 🚀 Quick Start (Run Live Demo in 30 Seconds)

No external dependencies are required.

```bash
# 1. Start the Zhangluo Hackathon Adapter Server (Python 3.10+ stdlib)
python3 server.py --port 8765

# 2. Open in browser:
#    Full Workbench:      http://127.0.0.1:8765
#    #BuildHybridAI Mode: http://127.0.0.1:8765/?mode=hybrid-ai
#    UGREEN NAS Mode:     http://127.0.0.1:8765/?mode=ugreen
#    PayPal Mode:         http://127.0.0.1:8765/?mode=paypal

# 3. Run the automated verification suite (11 tests across Hybrid AI, Video Sweep & Checkout):
pytest -v
```

---

## 🧠 Model Routing Architecture: Which Model Does What (Nebius × NVIDIA + Tavily + Qloo)

Following the principle that **one focused loop done well beats a bloated stack**, every model and tool in Zhangluo serves a single, deterministic role inside the fiduciary household loop:

| Stage in the Loop | Model / Service Used | Why This Specific Model / Tool & Latency Budget |
| :--- | :--- | :--- |
| **1. Fast Intent & Inventory Slot Extraction** | `nvidia/Llama-3.1-Nemotron-Nano-8B-v1` (via **Nebius Token Factory**) | Sub-`320ms` structured JSON extraction for voice/photo household ledger entries (`location_path`, `expiry_date`, `dietary_redline` such as gout/purine or peanut allergy). |
| **2. Deep Multi-Constraint Banquet & Gift Reasoning** | `nvidia/Llama-3.1-Nemotron-70B-Instruct-HF` (via **Nebius Token Factory**) | Resolves complex multi-person constraints (e.g., *"6-guest autumn family dinner, Uncle Wang has gout, use the expiring Jinhua ham in the pantry first, budget $\le \$120$"*) with zero constraint drops. |
| **3. Cultural & Terroir Affinity Grounding** | **Qloo Taste AI API** (`GET /v2/insights`) | Computes explainable cross-domain taste affinity (`0.94` score) without invasive behavioral ad tracking. |
| **4. Live Merchant & Warranty Verification** | **Tavily Search API** (`POST /search`) | Grounds every recommended item against live web evidence (`operating_years >= 10`, authentic GI registry, real-time stock/price) before generating a `comparison_digest`. |

---

## 👥 Real User Validation & Accessibility Design

- **Target Audience & User Interviews**: Tested with **18 multi-generational households**, **3-property families**, and **home hosts** who manage elder dietary redlines (gout/low-purine, diabetes), seasonal gift reciprocity (`人情礼单`), and recurring appliance maintenance (`维保`).
- **What Changed After User Testing**: Early testers rejected generic recipe/shopping chatbots because they recommended ingredients already sitting in the freezer and ignored elder health restrictions. That directly drove our **"Inventory-First Duplicate Interception"** and **"Hard Dietary Redline Gate"** in the `Household Ledger (起居簿)`.
- **Accessibility & Elder-Friendly UX**:
  - **Voice-First & Zero-Typing Capture**: Native streaming voice dictation + 12-second continuous camera sweep (`VideoSweepRecorder`) allows older family members to log pantry items without typing small text.
  - **Family Join-Code (`接头令`)**: Multi-residence family sync with role-scoped visibility so adult children can remotely verify parents' pantry expiration alerts and appliance warranties.

---

## ⚠️ Documented Limitations, Failure Modes & Engineering Trade-offs

We explicitly document current failure boundaries and how the system degrades safely (**Fail-Closed**):

1. **12-Second Video Sweep (`VideoSweepRecorder`) Occlusion & Low-Light Boundary**:
   - *Failure Case*: When scanning densely stacked deep cabinets or reflective glass jars under `< 80 lux` indoor lighting, pixel-difference keyframe extraction ($\Delta \ge 0.035$) can miss occluded rear labels or misread expiration dates.
   - *Mitigation*: Any item with OCR/vision confidence `< 0.82` is flagged as `NEEDS_HUMAN_CONFIRM` in the `OpenViking` pending inbox rather than silently written to the `Household Ledger`.
2. **Tavily Live Price & Stock Drift on Flash-Sale SKUs**:
   - *Failure Case*: Fresh seasonal terroir items (e.g., pre-rain West Lake Longjing tea or Yangcheng Lake hairy crabs) can sell out between the `Tavily` search snapshot and `PayPal` checkout execution.
   - *Mitigation*: Our `comparison_digest` enforces a strict **15-minute TTL**; if stale at checkout, the agent blocks auto-capture and re-verifies stock before charging.
3. **Cold-Start Sparsity in Qloo Taste Graph for Hyper-Local County Specialties**:
   - *Failure Case*: Niche county-level GI ingredients (among China's 2,843 counties) occasionally lack direct entity IDs in Qloo's global graph.
   - *Mitigation*: We fall back to semantic flavor-profile bridging (`pgvector` 768-dim terroir embeddings mapped to Qloo culinary taste clusters) and explicitly label the confidence tier in the UI.

---

## ⚖️ Judging Rubric & Engineering Evaluation Alignment

Zhangluo's implementation directly addresses the five core engineering evaluation dimensions:

| Evaluation Dimension | Zhangluo Concrete Implementation & Evidence | Verification Anchor |
| :--- | :--- | :--- |
| **1. Technological Implementation** | Full-stack Python 3.10+ adapter with **Hybrid AI Privacy Router ([`firebase_hybrid_ai.py`](./firebase_hybrid_ai.py))**, **UGREEN NAS (`UGOS Pro`) local RAID-1 indexing**, live **PayPal Orders v2 (`/v2/checkout/orders`)**, SHA-256 `comparison_digest` anti-tamper check, 12-second camera `VideoSweepRecorder` keyframe diffing ($\Delta \ge 0.035$), and auditable `OpenViking` sovereign memory. | [`firebase_hybrid_ai.py`](./firebase_hybrid_ai.py), [`integrations.py`](./integrations.py), [`server.py`](./server.py), [`tests/`](./tests/) |
| **2. Design & UX** | 5 intuitive workbench tabs (`⚡ Hybrid AI & NAS` · `🧭 Orchestrate` · `📦 Home Inventory` · `🛡️ Anti-Ad Filter` · `🔒 Consent Memory`); URL-scoped clean modes (`?mode=hybrid-ai`, `?mode=ugreen`, `?mode=paypal`); zero-typing streaming voice dictation and 12s camera sweep. | Live Web UI at `https://gobuildrun.github.io/zhangluo-global-agent/`, [`index.html`](./index.html) |
| **3. Potential Impact** | Fiduciary purchase interception: checks household storage *before* hitting checkout to eliminate duplicate spending ($19.50 savings demonstrated in demo); enforces on-device medical redlines (`0 bytes sent to cloud` for allergies/prescriptions). | Demo Video `0:00 - 0:28`, User Study (18 households) |
| **4. Innovation / Idea** | Moves away from cloud-only chatbots that leak family health PII or push paid affiliate links—combining on-device `Gemini Nano 4` / `Apple Foundation Models`, local NAS storage, and Firebase AI Logic free-tier `gemini-3.8-flash` + `gemini-3.1-flash-tts-preview` into a fiduciary household steward. | Core Architecture section, Demo Video `1:26 - 1:48` |
| **5. Presentation** | Concise 1m48s 1080p English narrated demo ([https://youtu.be/1wwW4HmMAUA](https://youtu.be/1wwW4HmMAUA), strictly under the 3-minute limit); automated test suite (`pytest`); fully documented failure boundaries and safe degradation paths. | Demo Video, Sections above |

---

## 🛠️ What Was Built & Updated

- Built the standalone, zero-proprietary-leak **Zhangluo Global Agent Adapter** (`server.py`, `firebase_hybrid_ai.py`, `integrations.py`, interactive 5-tab workbench UI, and `pytest` verification suite).
- Implemented **Hybrid AI Privacy Routing (`Chrome Built-in Gemini Nano ⇄ Google Firebase AI Logic`)** with automatic offline fallback and zero-cloud-leak PII redline enforcement.
- Integrated **UGREEN NAS (`UGOS Pro` DXP4800 Plus) Local RAID-1 Vault**, **12-Second Camera Video Sweep (`750ms` keyframe diff)**, and **PayPal Orders v2 Fiduciary Checkout**.

