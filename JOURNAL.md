# Calyx Project Journal (Evolved from Synapse)

## Session Protocol (MANDATORY)
*To be followed by every AI agent at the start and end of every session:*

### **Start of Session (Bootstrapping):**
0. **RULE ZERO (MANDATORY):** Your very first tool call MUST be `python Calyx/Core/tools/sync_mesh.py`. This ensures you ingest all GitHub updates and LAN mail before proceeding.
0b. **HEALTH CHECK:** Before firing any multi-node tests (e.g. Task #09), run `python Calyx/Core/tools/mesh_status.py`. You MUST see "🟢 MESH READY" before proceeding. If not, wait or coordinate via Mailroom.
1. **Identify Node:** Run `hostname` and check `shard_config.json`. Confirm if you are **PC_MASTER** or **LAPTOP_RELAY**.
2. **Read Mail:** Immediately read the output of the sync script or check `Calyx/MAIL_TO_...`.

### **End of Session (Handoff):**
1. **Update Journal:** Document status changes, technical decisions, and sprint progress below.
2. **Write Mail:** Write a high-signal "letter" to your coworker in their mailbox (`MAIL_TO_...`).
3. **Sync Notification (CRITICAL):** If you push changes to GitHub that the other node needs (Shared Zone fixes, etc.), you MUST prefix your mail with **"PULL REQUIRED"** and send a LAN mail via `mailroom.py`.
4. **The 20-Task Sprint:** Ensure tasks are organized and tested.
4. **Archiving Rule:** If this journal exceeds 150 lines, move entries older than 3 sessions to `Calyx/Docs/ARCHIVE_JOURNAL.md`.
5. **Push Changes:** Commit and push ALL changes (including mailbox updates) using Git CLI: `git add .; git commit -m "..."; git push origin master`.

---

### **Sovereign Territories (Anti-Conflict Rules):**
- **PC_MASTER:** Owns `hub_server.py`, `reward_engine.py`, `governance_dao.py`, `peer_db.json`.
- **LAPTOP_RELAY:** Owns `synapse_packager.py`, `efficiency_monitor.py`, `tools/`.
- **Shared Zone:** `neural_node.py`, `shard_manager.py`, `spike_protocol.py`. 
    - *RULE:* Pull before editing. Limit changes to your node's specific logic.
- **MOBILE_EDGE:** Owns `termux_boot.sh`, `pytorch_mobile_bridge.py`, `vitals_reporter.js`.

---

### [2026-03-02] - Session 21: PC Master (The Launch Sequence)

### Status update
- **Node Identification:** Confirmed session running on **Desktop (PC_MASTER)**.
- **Organization Setup (DONE):** Created **Calyx-Mesh** GitHub Organization.
- **Repo Initialization (DONE):** Created and initialized `calyx-core`, `calyx-framework`, and `calyx-docs`.
- **Codebase Sanitization (DONE):** Removed personal logs and hardcoded local paths. Replaced GitHub URLs with placeholders.
- **Framework Extraction (DONE):** Moved meta-tools (`JOURNAL.md`, `MAIL_TO_...`, `mcp_setup_guide.md`) to `Calyx/Framework/`.
- **Roadmap Expanded (DONE):** Defined Phases 5-8 with 20 granular tasks per phase, hardware delegation, and DAP (Distributed Authority Protocol).
- **Public Sync (DONE):** Created and executed `sync_to_org.ps1`. Successfully pushed sanitized code to the public Org.
- **Content Strategy (DONE):** Created `Creative/Content_Creation/calyx_video_strategy.md` and `calyx_theories_and_usecases.md`.

### Technical Decisions
1. **DAP Implementation:** Formally established the **Distributed Authority Protocol** to manage multi-node file ownership and prevent merge conflicts in a decentralized environment.
2. **Sanitization Strategy:** Moved all sensitive settings to `.env`. Log files containing personal paths were purged.
3. **Framework Separation:** Packaged the "AI-Builder Framework" as a standalone toolkit for the community, while keeping the core neuromorphic logic in `calyx-core`.

### Immediate Goals (PC_MASTER)
- [ ] Phase 5 Task 1: [MOBILE] `termux_bootstrap.sh` on Pixel 8.
- [ ] Create intro content for Instagram/YouTube based on the new "Theories" guide.
- [ ] Revive Skool and The Salty Merchant to share the public launch.
