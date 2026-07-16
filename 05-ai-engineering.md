# 📅 AI Engineering — Stage 5 (Ultimate Goal)

> **The Final Stage.** If you're here, you've already completed the full journey: Excel → Data Analyst → Backend Engineer. You know Python, FastAPI, PostgreSQL, and Docker. Now build AI systems on top of that foundation.
> **When:** After completing Stage 3 Backend (or after optional Stage 4 Data Engineering)

### 🔑 Critical Prerequisites from General Backend (Stage 3)
Before starting this stage, you must be extremely comfortable with these specific backend concepts:
- **FastAPI Mastery:** You must know how to build REST APIs, handle Streaming responses (crucial for LLM token streaming), and WebSockets.
- **Asynchronous Python (asyncio):** AI applications make heavy external API calls to OpenAI/Anthropic. If you can't write async code, your AI app will be unbearably slow.
- **System Design & Caching:** You need to understand Redis (for caching LLM responses to save API costs) and how to design microservices (e.g., separating the AI Agent service from the main web backend).
- **Authentication/Security:** Knowing how to securely store and manage API keys, and implementing Rate Limiting (to prevent users from bankrupting your OpenAI credits).

<details open>
<summary>🔴 Phase 1 — AI Foundations &nbsp;|&nbsp; Steps 1–8</summary>

<br>

> Master the fundamentals of LLMs, embedding models, and AI-powered backend systems.

---

**📐 Math Pre-Requisite (do alongside Steps 1-2):**

| Topic | Why | Resource | Time |
|-------|-----|----------|------|
| Linear Algebra basics | Embeddings, vectors, similarity | [3Blue1Brown — Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | 5-6 hr |
| Probability basics | Token sampling, model confidence | [StatQuest — Probability](https://www.youtube.com/watch?v=uzkc-qNVoOk) | 2-3 hr |

> You don't need research-level math. You're an AI Engineer, not a researcher. Visual intuition > formula memorization.

---

<details>
<summary>Steps 1–2 · LLM Mechanics & Prompt Engineering</summary>

<br>

> Understand the engine before you drive it. Your English Lit background is a massive advantage in Prompt Engineering.

- [ ] Tokens, context windows, sampling parameters (temperature, top_p, etc.)
- [ ] Models: Closed vs Open-weight (GPT, Claude, Gemini, Llama, Qwen)
- [ ] APIs: OpenAI API, Anthropic Messages API
- [ ] Local Inference: Run models locally with Ollama
- [ ] Structured outputs (JSON mode, schema-constrained generation)
- [ ] Prompt patterns: Few-shot, Role prompting, Chain-of-Thought (CoT), ReAct
- [ ] **Project:** Terminal-based Chat CLI that connects to multiple APIs and handles streaming responses.

</details>

<details>
<summary>Steps 3–4 · Embeddings, Vector DBs & Semantic Search</summary>

<br>

> The foundation of RAG and search systems.

- [ ] Embeddings (Vector representation of text, Cosine Similarity)
- [ ] Tools: Sentence-Transformers (Local), OpenAI Embeddings (API)
- [ ] Vector Databases: pgvector (PostgreSQL extension) or ChromaDB
- [ ] Hybrid Search: Combining Keyword search (BM25) with Vector Search
- [ ] **Project:** Semantic Search Engine. Index a set of documents locally and query them using embeddings and pgvector.

</details>

<details>
<summary>Steps 5–6 · Function Calling & Tool Use</summary>

<br>

> Giving LLMs the ability to act upon the world.

- [ ] Function/Tool schema design (OpenAI and Anthropic standards)
- [ ] Handling tool execution loops (Parse request -> Execute code -> Feed back to LLM)
- [ ] Parallel tool calling
- [ ] **Project:** AI Database Assistant. An API endpoint where a user asks a natural language question, the LLM generates a SQL query tool call, executes it safely, and returns the result.

</details>

<details>
<summary>Steps 7–8 · RAG (Retrieval-Augmented Generation)</summary>

<br>

> How to give LLMs access to enterprise data reliably.

- [ ] RAG architecture — Embed → Store → Retrieve → Generate
- [ ] Document loaders & Text Splitters (chunking strategies)
- [ ] Advanced Retrieval: Query Rewriting, HyDE (Hypothetical Document Embeddings)
- [ ] Reranking models (Cohere Rerank, BGE Reranker)
- [ ] Handling tabular data and PDFs (Unstructured, LlamaParse)
- [ ] **Project:** RAG-powered Enterprise Knowledge Bot (FastAPI backend + Reranking + Vector DB).

</details>

</details>

---

<details open>
<summary>⚫ Phase 2 — Advanced Orchestration & Production &nbsp;|&nbsp; Steps 9–16</summary>

<br>

> Moving from scripts to scalable, intelligent, and secure systems.

<details>
<summary>Steps 9–10 · Agentic Workflows with LangGraph</summary>

<br>

> The industry standard for complex, stateful multi-step AI logic.

- [ ] Core Concepts: Nodes, Edges, State
- [ ] Routing logic and conditional edges
- [ ] Memory/Checkpoints: Pausing state, Human-in-the-loop approvals
- [ ] Multi-agent orchestration
- [ ] **Project:** Research Agent. Takes a topic, searches the web (Tavily/SerpAPI), extracts content, summarizes, and drafts a report.

</details>

<details>
<summary>Steps 11–12 · AI Security & Guardrails</summary>

<br>

> Every AI feature is an attack surface.

- [ ] Prompt Injection & Jailbreaking (Direct vs Indirect)
- [ ] Input sanitization and Guardrails (Llama Guard, NeMo Guardrails)
- [ ] PII (Personally Identifiable Information) scrubbing
- [ ] Prompt versioning and secure handling of API keys

</details>

<details>
<summary>Steps 13–14 · MLOps, Evaluation & Observability</summary>

<br>

> You can't improve what you can't measure.

- [ ] Tracing & Observability: Integrate Langfuse to track latency, cost, and inputs/outputs.
- [ ] Evaluation metrics: Faithfulness, Context Precision/Recall (Ragas framework)
- [ ] Evals in CI/CD (Promptfoo)
- [ ] Cost Optimization: Semantic caching (Redis), Token budgeting.
- [ ] **Project:** Optimize the Knowledge Bot (from Step 8) by adding semantic caching and evaluating its accuracy with Ragas.

</details>

<details>
<summary>Steps 15–16 · Fine-Tuning Awareness</summary>

<br>

> You won't fine-tune models, but you must explain to employers/clients when it's needed vs. when it's not.

- [ ] Fine-tuning vs RAG vs Prompt Engineering — decision framework
- [ ] LoRA / QLoRA — concept overview (no hands-on needed)
- [ ] OpenAI fine-tuning API — how it works (overview only)
- [ ] When NOT to fine-tune — most problems are solvable with better prompts + RAG

</details>

</details>

---

<details open>
<summary>🚀 Phase 3 — The Portfolio & Job Hunt &nbsp;|&nbsp; Steps 17–20</summary>

<br>

> Time to package your skills and prove your competence to hiring managers.
> *Proof of work beats a degree.*

<details>
<summary>Steps 17–18 · The Capstone Project</summary>

<br>

> Build one massively impressive, end-to-end deployed system.

- [ ] **Capstone Idea:** "AI Customer Support Engine"
  - FastAPI backend.
  - Receives webhooks/emails.
  - Agentic workflow (LangGraph) routes to departments or resolves tickets via RAG.
  - Fully containerized with Docker.
  - Deployed on AWS/Render/GCP.
  - GitHub repo must have a pristine README, architecture diagram, and automated tests.

</details>

<details>
<summary>Steps 19–20 · Market Entry Strategy</summary>

<br>

- [ ] **Portfolio Polish:** 3 solid projects (RAG system, LangGraph Agent, Capstone).
- [ ] **Online Presence:** Clean up GitHub. Every repo should have a 2-minute Loom video demo.
- [ ] **LinkedIn Rebrand:** Update title to "AI Engineer". Post technical deep dives about the systems you've built.
- [ ] **Targeting Roles:** Apply for "AI Engineer", "Backend Engineer (AI)", or "Data Platform Engineer". Look for startups and product-led SMBs.

</details>

</details>
