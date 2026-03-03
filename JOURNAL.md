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

---

### [2026-02-28] - Session 18: PC Master Sprint (The Distributed Hub)

### Status update
- **Node Identification:** Confirmed session running on **Desktop (PC_MASTER)**.
- **Task 10 (DONE):** Hub UI Path Graph implemented using D3.js. Real-time topology now visible in the Mesh Monitor tab.
- **Task 11 (DONE):** Refined Global Vitals Dashboard with WebSocket integration for live GPU/Mobile telemetry.
- **Task 14 (DONE):** Implemented Mesh-Wide Reward Splitting in `reward_engine.py`. Rewards are now proportional to shard layer contributions.
- **Task 26 (DONE by Laptop):** Built `mailroom.py` client for LAN-based AI Email.
- **Laptop Relay Sprint:** 
    - **Task 05-08, 12, 15, 17 (DONE):** Optimized Buffer, Sequential Logic, Atomic Relay, Socket Bridge, Thermal Guard, Failover Routing, and Packager.
- **Environment:** Resolved `snntorch` dependency; bypassed `libp2p` using the "Postal Service" (file-based) discovery fallback for the Hub.

### Technical Decisions
1. **Hub Discovery:** The Hub now acts as a passive monitor, polling `mesh_discovery` every 5s to update the D3 graph without requiring direct P2P connections.
2. **Reward Logic:** Shard contributions are calculated as `(layers_processed / total_layers) * final_output_spikes`.
3. **Thermal Guard:** Shards now have an `is_ready` flag. The Hub UI should reflect "OFFLINE" nodes if they overheat.

### Immediate Goals (PC_MASTER)
- [ ] Task 25: Build Hub Mailroom API (POST/GET for AI letters).
- [X] Task 09: First Multi-Hop Inference (End-to-End Test) - SUCCESS.
- [X] Task 18: Marketplace Detail View (Task 18) - COMPLETE. Modal UI and detail API implemented.

---

### [2026-03-01] - Session 20: Laptop Phase 4 Finalization (The Sovereign Relay)

### Status update
- **Node Identification:** Confirmed running on **Laptop (JadeEnvy)**.
- **Laptop Relay Sprint (100% COMPLETE):** 
    - **Task 21 (DONE):** Built `weight_sharder.py` tool for automated model splitting.
    - **Task 22 (DONE):** Integrated **VRAM Pressure Sensor** into `efficiency_monitor.py`. Laptop will now drop shards if VRAM > 90%.
    - **Task 27 (DONE):** Built `mesh_probe.py` (Low-Energy UDP Trigger).
    - **Task 09 (VERIFIED SUCCESS):** Multi-hop inference loop confirmed with PC Master. **Final result received at 03:59Z.**
    - **Phase 4 Sprint:** 100% COMPLETE (All tasks checked and hardened).
- **Communication:** Rule Zero Auto-Sync is functional and hardened.

### Technical Decisions
1. **Dynamic Sharding:** `weight_sharder.py` uses `state_dict` prefix matching to create discrete `.pt` files for mesh deployment.
2. **Pruning Logic:** ShardManager now tracks `last_seen` timestamps in discovery JSONs to maintain a clean mesh topology.
3. **Completion Routing:** PipelineRouter now explicitly routes `END` state spikes back to `PC_MASTER`.

### Immediate Goals (PC_MASTER)
- [X] Task 18: Marketplace Detail View - COMPLETE. Final Phase 4 UI live.
- [X] Task 25: Hub Mailroom API - COMPLETE. Node orchestration verified.
- [X] Task 28: Real-time Mesh Log Stream - COMPLETE. Remote logs streaming to Hub.
- [X] Task 24: Phase 5 Roadmap & Handoff - COMPLETE. Updated `Docs/roadmap.md`.
