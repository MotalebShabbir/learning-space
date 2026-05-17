AI Engineering এর সাথে রিলেটেড টপিক গুলো এখানে লিস্ট করে দিলাম। আপনারা এই টপিক গুলো নিয়ে পড়াশোনা করতে পারেন, লস হবে না।
বর্তমানে AI Engineer একটা স্ট্যাবলিশড রোল। যারা ২৩-২৪ এই রোলের জন্য নিজেদের প্রিপেয়ার করেছিল তারা ২৫-২৬ এ প্রচুর কাজ করেছে, প্রচুর ক্লায়েন্ট পেয়েছে, অ্যামেজিং সব প্রজেক্ট করেছে। ভবিষ্যতেও এই রোলের ডিমান্ড থাকবে, কারণ বর্তমানের সকল এপ্লিকেশন কোনো না কোনো ভাবে AI ইন্টিগ্রেট করবেই।

## 𝟏. 𝐋𝐋𝐌 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥𝐬 (𝐟𝐫𝐨𝐦 𝐚𝐧 𝐞𝐧𝐠𝐢𝐧𝐞𝐞𝐫'𝐬 𝐥𝐞𝐧𝐬)

- Tokens, tokenization, context windows, and how they map to cost⁣
- Model families and trade-offs: Claude, GPT, Gemini, Llama, Mistral, Qwen, DeepSeek⁣
- Closed vs open-weight models, and when each makes sense⁣
- Sampling parameters: temperature, top_p, top_k, frequency/presence penalty⁣
- Streaming vs non-streaming responses⁣
- Structured outputs (JSON mode, schema-constrained generation)⁣
- Function calling / tool use mechanics⁣
- Multimodal inputs (vision, audio, PDFs)⁣
- Embedding models and reranker models⁣
- Reasoning models vs standard models (and when extended thinking helps)

## 𝟐. 𝐏𝐫𝐨𝐦𝐩𝐭 𝐄𝐧𝐠𝐢𝐧𝐞𝐞𝐫𝐢𝐧𝐠⁣⁣

- System vs user vs assistant message design⁣
- Few-shot examples, role prompting, persona design⁣
- Chain-of-thought, ReAct, reflection patterns⁣
- XML/Markdown structuring for reliable parsing⁣
- Prompt templating and variable injection⁣
- Prompt versioning (treating prompts like code)⁣
- Output parsers and graceful failure handling⁣
- Prompt injection defense at the prompt layer

## 𝟑. 𝐂𝐨𝐧𝐭𝐞𝐱𝐭 𝐄𝐧𝐠𝐢𝐧𝐞𝐞𝐫𝐢𝐧𝐠 (𝐭𝐡𝐞 𝐧𝐞𝐰 "𝐩𝐫𝐨𝐦𝐩𝐭 𝐞𝐧𝐠𝐢𝐧𝐞𝐞𝐫𝐢𝐧𝐠")⁣

⁣

- Context window budgeting across system, history, tools, and retrieval⁣
- Conversation summarization and rolling memory⁣
- Prompt caching strategies (Anthropic/OpenAI cache)⁣
- Hierarchical memory: short-term, long-term, episodic⁣
- Context compression and pruning⁣
- Tool result truncation strategies⁣
- "Lost in the middle" problem and mitigation

## 𝟒. 𝐑𝐀𝐆 𝐚𝐧𝐝 𝐊𝐧𝐨𝐰𝐥𝐞𝐝𝐠𝐞 𝐒𝐲𝐬𝐭𝐞𝐦𝐬⁣

- Chunking strategies: fixed, semantic, structural, late chunking⁣
- Vector databases: Qdrant, Pinecone, Weaviate, pgvector, Chroma, Milvus⁣
- Hybrid search (BM25 + vector) and reciprocal rank fusion⁣
- Query rewriting, expansion, HyDE⁣
- Multi-hop retrieval, agentic retrieval⁣
- Reranking (Cohere, BGE, Voyage)⁣
- Metadata filtering and structured retrieval⁣
- GraphRAG and knowledge-graph augmentation⁣
- Document parsing pipelines (Unstructured, LlamaParse, Docling)⁣
- Multimodal RAG (images, tables, charts)

## 𝟓. 𝐀𝐠𝐞𝐧𝐭𝐬 𝐚𝐧𝐝 𝐀𝐠𝐞𝐧𝐭𝐢𝐜 𝐒𝐲𝐬𝐭𝐞𝐦𝐬

- Agent loops: ReAct, Plan-Execute, Reflexion, ReWOO
- Single-agent vs multi-agent orchestration
- State machines and workflow graphs (LangGraph, Mastra, Inngest)
- Agent memory: scratchpad, semantic, procedural
- Human-in-the-loop checkpoints and approvals
- Subagents and delegation patterns
- Error recovery, retries, and self-correction
- Long-running agents (durable execution, Temporal, Restate)
- Browser agents and computer-use agents

## 𝟔. 𝐓𝐨𝐨𝐥 𝐔𝐬𝐞 𝐚𝐧𝐝 𝐈𝐧𝐭𝐞𝐠𝐫𝐚𝐭𝐢𝐨𝐧𝐬⁣

- Tool/function schema design (clear names, descriptions, params)⁣
- Parallel tool calling⁣
- Model Context Protocol (MCP): servers, clients, resources, prompts⁣
- Sandboxed code execution (E2B, Modal, Daytona, Cloudflare sandboxes)⁣
- API wrappers as tools⁣
- Tool result formatting for LLM consumption

## 𝟕. 𝐈𝐧𝐟𝐞𝐫𝐞𝐧𝐜𝐞⁣

- API-based vs self-hosted inference⁣
- Inference servers: vLLM, TGI, SGLang, Ollama, llama.cpp⁣
- Quantization: GGUF, AWQ, GPTQ, INT4/INT8⁣
- KV cache optimization, prefix caching, speculative decoding⁣
- Continuous batching and throughput tuning⁣
- Latency vs throughput trade-offs (TTFT, TPS)⁣
- GPU economics, edge inference, on-device models⁣
- Inference providers: Together, Fireworks, Groq, Cerebras, Replicate, Bedrock

## 𝟖. 𝐋𝐋𝐌𝐎𝐩𝐬 𝐚𝐧𝐝 𝐎𝐛𝐬𝐞𝐫𝐯𝐚𝐛𝐢𝐥𝐢𝐭𝐲⁣

- Tracing: Langfuse, LangSmith, Helicone, Arize Phoenix, Braintrust⁣
- Token, cost, and latency tracking per request and per user⁣
- Prompt and agent versioning⁣
- A/B testing prompts and models in production⁣
- Replay and debugging of failed runs⁣
- Drift detection (model upgrades silently changing behavior)⁣
- Feedback loops (thumbs up/down → eval datasets)

## 𝟗. 𝐄𝐯𝐚𝐥𝐮𝐚𝐭𝐢𝐨𝐧 𝐄𝐧𝐠𝐢𝐧𝐞𝐞𝐫𝐢𝐧𝐠⁣

- Offline evals: golden datasets, regression tests⁣
- LLM-as-judge: pairwise comparison, rubric-based scoring⁣
- RAG metrics: faithfulness, answer relevance, context precision/recall (Ragas)⁣
- Agent evals: task success rate, trajectory analysis, tool-call accuracy⁣
- Synthetic data generation for evals⁣
- Frameworks: Promptfoo, DeepEval, Inspect, Braintrust, OpenAI Evals⁣
- Online evals on production traffic⁣
- Red teaming and adversarial testing⁣

## 𝟏𝟎. 𝐂𝐨𝐬𝐭 𝐚𝐧𝐝 𝐏𝐞𝐫𝐟𝐨𝐫𝐦𝐚𝐧𝐜𝐞 𝐎𝐩𝐭𝐢𝐦𝐢𝐳𝐚𝐭𝐢𝐨𝐧⁣

- Model cascading (cheap → expensive routing)⁣
- Semantic caching, output caching, prompt caching⁣
- Batch APIs for non-real-time workloads⁣
- Distillation (small model trained from big model outputs)⁣
- Prompt compression (LLMLingua-style)⁣
- Token budgeting per feature⁣
- Model gateways: LiteLLM, Portkey, OpenRouter

## 𝟏𝟏. 𝐒𝐚𝐟𝐞𝐭𝐲, 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲, 𝐚𝐧𝐝 𝐆𝐮𝐚𝐫𝐝𝐫𝐚𝐢𝐥𝐬⁣

- Prompt injection (direct and indirect)⁣
- Jailbreak resistance⁣
- Data exfiltration via tool calls and rendered links⁣
- Content moderation (Llama Guard, OpenAI moderation, Azure)⁣
- Guardrail frameworks: NeMo Guardrails, Guardrails AI⁣
- PII redaction in inputs and outputs⁣
- Rate limiting and abuse prevention⁣
- Output validation against schemas⁣
- Audit logging for compliance⁣

## 𝟏𝟐. 𝐌𝐮𝐥𝐭𝐢𝐦𝐨𝐝𝐚𝐥 𝐄𝐧𝐠𝐢𝐧𝐞𝐞𝐫𝐢𝐧𝐠⁣

- Vision: image understanding, OCR-via-LLM, document AI⁣
- Voice agents: STT (Whisper, Deepgram, AssemblyAI), TTS (ElevenLabs, Cartesia, OpenAI), realtime APIs (LiveKit, Vapi, Retell)⁣
- Image generation: Flux, SDXL, Imagen, DALL-E, plus ControlNet/LoRA workflows⁣
- Video generation: Sora, Veo, Runway, Kling⁣
- ComfyUI, Replicate, Fal for media pipelines

## 𝟏𝟑. 𝐀𝐈 𝐀𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐀𝐫𝐜𝐡𝐢𝐭𝐞𝐜𝐭𝐮𝐫𝐞⁣

- Streaming over SSE / WebSockets / HTTP chunked⁣
- Background jobs and queues for long agent runs⁣
- Idempotency and resumability of agent runs⁣
- Multi-tenant prompt and key management⁣
- Fallback chains across providers⁣
- Feature flags for prompts and models⁣
- API design patterns for AI features (cancel, retry, partial results)

  নোট: টপিক গুলো AI দিয়ে rephrase এবং অরগানাইজ করা হয়েছে। See less
