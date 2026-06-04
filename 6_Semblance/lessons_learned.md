# 📓 Lessons Learned & Active Reflection Journal

> This log captures retrospectives, insights, and lessons learned during development milestones.

---

## 📅 2026-05-31: Stage 1 Kanban Implementation & Navigation Setup

### What went well
- Created a standard Markdown-based `kanban.md` that traces tasks back to the 7-Stage Framework.
- Updated the centralized navigation menus (`navigation_config.json`, fallback JSON objects in `index.html`, and `markdown_renderer.html`) to expose the Kanban board as a direct debug option.
- Verified how `markdown_renderer.html` resolves directory paths (defaults to `README.md`) and correctly formatted links.

### Gaps & Challenges
- Navigation fallbacks are duplicated in `index.html` and `markdown_renderer.html`. In the future, it might be cleaner to isolate the fallback menu logic to a shared JS utility, but keeping them synchronized manually works for now and maintains resilience.

### Takeaway for Future AI Agents
- When completing tasks, make sure to update the status of the tasks in `1_Real_Unknown/kanban.md` using matching commit messages.

## 📅 2026-05-31: Stage 1 Cost Tracker Setup

### What went well
- Established a unified structure to track both system infrastructure costs and API token consumption in `1_Real_Unknown/costs.md`.
- Kept navigation fallbacks in sync so that the project menu operates reliably.

### Gaps & Challenges
- Estimates for Key Vault and container execution can fluctuate. Agents should update the log on every significant run/operation to prevent budget surprises.

## 📅 2026-05-31: Agent Git Rule & Error Resolution Update

### What went well
- Clarified the requirement for git error resolution across all core agent documentation (`agents.md`, `gemini.md`, `claude.md`, `copilot.md`, `kilocode.md`).
- Practiced granular commit-and-push cycles for each file modification.

### Gaps & Challenges
- None. Maintaining step-by-step git push commands helps identify remote changes or conflicts early.

## 📅 2026-05-31: Console Debugging & Debug Menu Sync Update

### What went well
- Added custom `debugLog` function to output descriptive messages into browser console when debug mode (`debug=true` cookie) is active.
- Documented Debug Menu synchronization rule across all agent personas to prevent stale menu links when markdown documents are added or updated.

### Gaps & Challenges
- Since debug console logs only print when the debug cookie is active, it protects console cleanliness for standard users while providing rich instrumentation for developers.

## 📅 2026-05-31: Architecture Setup & Sync Rules Update

### What went well
- Created a comprehensive `2_Environment/architecture.md` containing dynamic Mermaid charts showing system components (GitHub Pages, Cloudflare Workers, Fly.io, Azure Key Vault, GitHub Actions).
- Standardized rules in `agents.md` and agent profiles instructing teams to update `architecture.md` as soon as system configurations change.

### Gaps & Challenges
- None. Ensuring all components are mapped visually helps human stakeholders and subsequent AI agents maintain correct contextual orientation.

## 📅 2026-05-31: Kanban Maintenance Section Added

### What went well
- Appended the 7-stage folder structure maintenance checklist directly into `1_Real_Unknown/kanban.md` as requested.
- Tracked this update in the logs to maintain proper execution transparency.

### Gaps & Challenges
- None. Having this checklist helps ensure each stage directory is systematically maintained during development runs.

## 📅 2026-06-04: Supabase POC App & Template Refactoring

### What went well
- Replaced all project files with template structure from `delivery-pilot-template` successfully.
- Resolved and fixed all local folder path links, changing them from `delivery-pilot-template` to `supabase_poc`.
- Proactively created a new Supabase project `supabase-poc-app` under the user's organization using the Management API.
- Diagnosed connection issues by querying the database configuration from Supabase API to retrieve the exact pooler host (`aws-1-eu-west-2.pooler.supabase.com` on port 6543) and populated the Postgres tables with sample data.
- Built a live task manager client in the root `index.html` frontend dashboard that handles real-time task additions, completion toggles, and deletions directly with the Supabase JS API client.

### Gaps & Challenges
- Direct connection via standard PostgreSQL port (5432/6543) on database host resolved to IPv6 addresses or timed out due to network policies. Resolving this required querying the project pooler API configuration and connecting to the designated pooler instance (`aws-1-eu-west-2.pooler.supabase.com`).

### Takeaway for Future AI Agents
- Always inspect the `database` configuration and pooler settings returned by the Supabase Management API to obtain the correct routing credentials rather than assuming default host names.

## 📅 2026-06-04: Realtime WebSockets & Storage Buckets Integration

### What went well
- Configured a PostgreSQL migration setup script (`setup_storage.py`) to dynamically initialize a public storage bucket `poc-files` and set up the corresponding row-level access policies via SQL direct queries.
- Built a WebSocket event streaming view (`realtime_poc.html`) showcasing how client subscriptions parse database replication broadcasts in real-time.
- Implemented file uploading, listing, rendering, and removal capabilities inside `storage_poc.html` without back-end middleware dependency.
- Kept Project and Debug menus globally updated across fallback values and central configurations.

### Gaps & Challenges
- Integrating Realtime changes requires proper channel initialization. Subscribing to wildcard events without specific table targets can clutter feed streams; explicitly targeting `table: 'tasks'` solved this.

### Takeaway for Future AI Agents
- When designing bucket integration modules, make sure the target bucket is explicitly configured with public SELECT policies to avoid retrieval HTTP 403 errors on the client.
