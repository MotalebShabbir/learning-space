# 🤖 AI Automation Specialist Roadmap

> Your core money-making track. Combines your logical thinking (C++), backend basics (APIs), and AI knowledge to build automated systems for businesses.

---

<details open>
<summary>🟢 Phase 1 — n8n Foundations &nbsp;|&nbsp; Steps 1–3</summary>

<br>

> Master the tool. n8n is developer-friendly, powerful, and highly requested on Upwork.

<details>
<summary>Step 1 · n8n Basics</summary>

<br>

- [ ] Install n8n locally via npm or Docker (or use n8n Cloud free trial)
- [ ] Nodes, Connections, and Execution Flow
- [ ] Trigger Nodes (Webhook, Schedule, specific app triggers)
- [ ] The JSON data structure in n8n (Items, expressions, `$json`)
- [ ] Credentials management in n8n
- [ ] **Exercise:** Create a workflow that triggers every day at 9 AM and sends a weather update to your Telegram/Slack.

</details>

<details>
<summary>Step 2 · Data Manipulation & Logic</summary>

<br>

- [ ] If / Switch nodes (branching logic)
- [ ] Set node & Item Lists node (data manipulation)
- [ ] Loop node (iterating over arrays)
- [ ] Expressions (using JS inside n8n fields)
- [ ] Error handling (Continue on Fail, Error Trigger node)
- [ ] **Exercise:** Read a Google Sheet of tasks, filter out completed ones, and send the rest to a chat app.

</details>

<details>
<summary>Step 3 · The Developer Edge (Code Nodes)</summary>

<br>

> This is where you beat 90% of freelancers.

- [ ] Code node basics (Writing raw JavaScript in n8n)
- [ ] Transforming complex API responses using Code node
- [ ] HTTP Request node (Calling undocumented APIs)
- [ ] Webhook node (Receiving data from anywhere)
- [ ] **Exercise:** Receive a messy webhook payload, use a Code node to clean and format the JSON, and insert it into Supabase/PostgreSQL.

</details>

</details>

---

<details open>
<summary>🟡 Phase 2 — AI Integration & Applied LLMs &nbsp;|&nbsp; Steps 4–5</summary>

<br>

> Bringing intelligence to automation.

<details>
<summary>Step 4 · LLM Basics in n8n</summary>

<br>

- [ ] OpenAI & Anthropic API connections
- [ ] Advanced AI nodes in n8n
- [ ] Prompt engineering for reliable JSON outputs
- [ ] Information extraction (Unstructured text → Structured JSON)
- [ ] **Project:** AI Email Assistant. Triggers on new Gmail, AI reads it, classifies it (Support/Sales/Spam), and drafts a reply.

</details>

<details>
<summary>Step 5 · RAG & Memory in Automation</summary>

<br>

- [ ] Text splitters & Embeddings
- [ ] Vector Stores (Supabase pgvector or Pinecone) inside n8n
- [ ] Chat memory (Buffer memory)
- [ ] **Project:** Customer Support Bot. Webhook receives user message → AI searches Vector DB (Company FAQ) → Formats response → Sends back via Webhook.

</details>

</details>

---

<details open>
<summary>🚀 Phase 3 — Portfolio & Freelance Launch &nbsp;|&nbsp; Steps 6–8</summary>

<br>

> Time to monetize.

<details>
<summary>Step 6 · Build 3 Core Portfolio Projects</summary>

<br>

Build these out fully, record 2-minute Loom videos explaining them, and write clear READMEs.

1. **Lead Qualification Pipeline:** Web form submission → Clearbit/LinkedIn API for enrichment → AI scores the lead → Adds to CRM (HubSpot/Airtable).
2. **Invoice Processor:** Email with PDF attachment → AI extracts data (Amount, Date, Vendor) → Adds to Google Sheets/Database → Sends Slack summary.
3. **Automated Content Machine:** RSS feed trigger → AI summarizes article → AI generates social media posts → Schedules in Buffer/Notion.

</details>

<details>
<summary>Step 7 · Freelance Setup</summary>

<br>

- [ ] Upwork Profile: "AI Automation Engineer | n8n & API Expert"
- [ ] Emphasize your coding background (Python/JS) as your unique value prop.
- [ ] LinkedIn optimization
- [ ] Cold email templates for local businesses (e.g., local coaching centers, agencies).

</details>

<details>
<summary>Step 8 · The Client Hunt</summary>

<br>

- [ ] Apply to 5 Upwork jobs daily (filter for "n8n", "Make", "API integration", "OpenAI").
- [ ] Offer the first 2-3 jobs at a lower rate ($15-20/hr) just to get 5-star reviews.
- [ ] Gradually increase rate to $40-50/hr as portfolio builds.

</details>

</details>
