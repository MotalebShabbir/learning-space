# ⚙️ Backend, DevOps & Cloud Engineering — Stage 2

> **Goal:** Become a competent Backend Engineer capable of building, deploying, and maintaining production-grade web applications and APIs.
> **When:** Stage 2 of the roadmap
> **Pre-requisite:** Python, SQL basics already known (from Stage 1)
> **What you can build after this:** SaaS products, REST/GraphQL APIs, real-time apps, microservices — and you can deploy them securely to the cloud.

---

<details open>
<summary>🟢 Phase A — Python Backend Foundations</summary>

<br>

> You already know Python basics from Stage 2. Now learn to use it as a professional backend language.

<details>
<summary>Step 1 · Advanced Python for Engineering</summary>

<br>

- [ ] Object-Oriented Programming (OOP) — Classes, Inheritance, Encapsulation, Polymorphism
- [ ] Decorators — function wrappers (heavily used in all Python frameworks)
- [ ] Generators & Iterators — memory-efficient data processing
- [ ] Context Managers — `with` statement, resource management
- [ ] Type Hinting — `def greet(name: str) -> str:`
- [ ] Async/Await — asyncio fundamentals (concurrent I/O operations)
- [ ] Pydantic — data validation and serialization
- [ ] Dataclasses — lightweight data containers
- [ ] **Project:** Build a CLI tool that fetches data from a public API, processes it, and saves structured output to a file

**Resource:** [Real Python](https://realpython.com/) — Best Python tutorials
**Resource:** [Python Cookbook (O'Reilly)](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/) — Advanced patterns

</details>

<details>
<summary>Step 2 · FastAPI — Modern Python Web Framework</summary>

<br>

> FastAPI is Python's fastest and most modern web framework. Auto-generates API docs, built-in validation, async-first.

- [ ] Project setup — virtual environment, project structure, config management
- [ ] Routing — GET, POST, PUT, PATCH, DELETE
- [ ] Path parameters, Query parameters, Request body
- [ ] Request/Response models with Pydantic
- [ ] Dependency Injection — clean, testable code
- [ ] Error handling — HTTPException, custom error responses
- [ ] Middleware — logging, timing, CORS
- [ ] File uploads and downloads
- [ ] Background tasks
- [ ] Auto-generated API docs — Swagger UI & ReDoc (built-in)
- [ ] **Project:** Todo/Notes REST API with full CRUD, pagination, search, and filtering

**Resource:** [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/) — Best docs in the Python ecosystem
**Alternative:** Flask (simpler, more flexible) or Django (batteries-included, admin panel)

</details>

<details>
<summary>Step 3 · PostgreSQL + Database Engineering</summary>

<br>

> You learned SQL for querying in Stage 2. Now learn database design, ORMs, and migrations.

- [ ] Database design — normalization (1NF, 2NF, 3NF), denormalization trade-offs
- [ ] Relationships — One-to-One, One-to-Many, Many-to-Many
- [ ] SQLAlchemy ORM — models, relationships, queries from Python
- [ ] asyncpg — async PostgreSQL driver (for FastAPI)
- [ ] Alembic — database migrations (version control for your schema)
- [ ] Indexing strategies — B-tree, Hash, GIN, GiST (when and why)
- [ ] Connection pooling — handle concurrent users efficiently
- [ ] Transactions — ACID properties, rollback, isolation levels
- [ ] Full-text search with PostgreSQL
- [ ] **Project:** Blog Platform API — FastAPI + PostgreSQL + SQLAlchemy
  - Users, Posts, Comments, Tags (with relationships)
  - CRUD for all entities
  - Pagination, search, and filtering
  - Database migrations with Alembic

**Resource:** [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) — Official
**Resource:** [Use The Index, Luke](https://use-the-index-luke.com/) — SQL indexing deep dive

</details>

<details>
<summary>Step 4 · Authentication & Authorization</summary>

<br>

> Every real-world app needs auth. Learn it properly — security mistakes are career-ending.

- [ ] Password hashing — bcrypt, Passlib (never store plain passwords)
- [ ] JWT (JSON Web Tokens) — access tokens + refresh tokens
- [ ] OAuth2 with FastAPI — Bearer token flow
- [ ] Session-based auth vs Token-based auth — when to use which
- [ ] RBAC — Role-Based Access Control (admin, editor, viewer)
- [ ] API key authentication — for service-to-service calls
- [ ] Social login (OAuth2 with Google/GitHub) — overview
- [ ] **Project:** Add full authentication to your Blog API
  - Registration, Login, Logout
  - Protected routes (only logged-in users can create posts)
  - Admin-only routes (delete any post)
  - Refresh token rotation

**Resource:** [FastAPI Security Docs](https://fastapi.tiangolo.com/tutorial/security/) — Official

</details>

</details>

---

<details open>
<summary>🟡 Phase B — Production, DevOps & Cloud Skills</summary>

<br>

> Building an API ≠ Production-ready. Learn deployment, testing, caching, cloud servers, and CI/CD.

<details>
<summary>Step 5 · Linux & Server Basics</summary>

<br>

> When you deploy to the cloud, it's a Linux server. If you don't know this, you'll get stuck in production.

- [ ] File system navigation — ls, cd, pwd, find, tree
- [ ] File operations — cp, mv, rm, chmod, chown
- [ ] Text processing — cat, grep, head, tail, wc, awk (basics)
- [ ] Process management — ps, top, htop, kill
- [ ] Environment variables — export, .bashrc, .env files
- [ ] SSH — key generation, ssh-copy-id, config file
- [ ] **Exercise:** SSH into a remote server, create a user, set up SSH keys

**Resource:** [Linux Journey](https://linuxjourney.com/) (free)
**Resource:** [The Missing Semester — MIT](https://missing.csail.mit.edu/) (free, excellent)

</details>

<details>
<summary>Step 6 · Testing, Validation & Logging</summary>

<br>

- [ ] Pydantic validators — custom field validators, model validators
- [ ] Structured logging — JSON logs with context (user, request ID)
- [ ] pytest — unit testing fundamentals
- [ ] httpx + pytest — API endpoint integration testing
- [ ] Test fixtures and mocking — reusable test data, mocking DB/APIs
- [ ] Test-Driven Development (TDD) — write tests first, then code
- [ ] **Project:** Write tests for your Blog API — aim for 80%+ coverage

</details>

<details>
<summary>Step 7 · Caching & Performance</summary>

<br>

> Fast APIs keep users happy. Learn to cache smartly and optimize bottlenecks.

- [ ] Redis fundamentals — key-value store, TTL, data structures
- [ ] Caching strategies — cache-aside, write-through, write-behind
- [ ] API response caching with Redis
- [ ] Database query optimization — EXPLAIN ANALYZE, slow query logging
- [ ] N+1 query problem — eager loading vs lazy loading
- [ ] Rate limiting — token bucket, sliding window (using Redis)
- [ ] **Project:** Add Redis caching to your Blog API — cache popular posts, invalidate on update

</details>

<details>
<summary>Step 8 · Docker Deep Dive</summary>

<br>

> Docker solves "works on my machine." Essential for any production deployment.

- [ ] Dockerfile — containerize Python apps
- [ ] Multi-stage builds — smaller, more secure images
- [ ] docker-compose — run app + PostgreSQL + Redis together locally
- [ ] Docker networking & volumes — persistent data, how containers communicate
- [ ] Environment variables & secrets — .env management, never hardcode secrets
- [ ] **Project:** Dockerize your entire Blog API stack (app + DB + Redis) and optimize the image size

</details>

<details>
<summary>Step 9 · Nginx & Cloud Deployment</summary>

<br>

> Deploying to a cheap VPS is the best way to learn cloud fundamentals before tackling AWS.

- [ ] What is a reverse proxy — why you need Nginx in front of FastAPI
- [ ] Nginx reverse proxy setup & SSL/TLS with Let's Encrypt (certbot)
- [ ] Cloud Concepts: IaaS vs PaaS vs SaaS, Regions & Availability Zones
- [ ] VPS Deployment — Rent a DigitalOcean/Hetzner server
- [ ] Basic AWS: EC2 (servers), S3 (storage), RDS (database), IAM (security)
- [ ] **Project:** Deploy your Dockerized Blog API behind Nginx with real SSL on a VPS or AWS EC2

**Resource:** [DigitalOcean Tutorials](https://www.digitalocean.com/community/tutorials) (free, excellent)
**Resource:** [AWS Free Tier](https://aws.amazon.com/free/) (12 months free)

</details>

<details>
<summary>Step 10 · CI/CD & Monitoring</summary>

<br>

- [ ] GitHub Actions — run tests automatically on every push/PR
- [ ] Automated deployment — push to main → deploy to production
- [ ] Health check endpoints — `GET /health` for uptime monitoring
- [ ] Error tracking — Sentry integration (catch production errors)
- [ ] Uptime monitoring — UptimeRobot or Uptime Kuma (self-hosted)
- [ ] **Project:** Set up a complete CI/CD pipeline for your Blog API with Sentry error tracking

**Resource:** [GitHub Actions Docs](https://docs.github.com/en/actions)

</details>

</details>

---

<details open>
<summary>🔵 Phase C — Advanced Topics & System Design</summary>

<br>

> Go beyond CRUD. Learn patterns that senior engineers use in real-world systems.

<details>
<summary>Step 11 · Background Jobs & Real-Time</summary>

<br>

- [ ] Background jobs — email sending, report generation, data processing
- [ ] Celery + Redis — distributed task queue
- [ ] Scheduled tasks — periodic jobs (cron-like)
- [ ] WebSocket fundamentals — persistent bidirectional connection
- [ ] Real-time notifications with FastAPI WebSockets
- [ ] **Project:** Add real-time notifications and background welcome emails to your Blog API

</details>

<details>
<summary>Step 12 · System Design & Architecture Patterns</summary>

<br>

> Think like an architect, not just a coder.

- [ ] Scalability — vertical vs horizontal
- [ ] Load balancers & CAP theorem
- [ ] Monolith vs Microservices vs Event-driven architecture
- [ ] Database scaling — read replicas, sharding
- [ ] AI-Specific Architecture: Streaming LLM output (SSE/WebSocket)
- [ ] AI-Specific Architecture: Background jobs for agent runs (never run 30s agents in HTTP requests)
- [ ] AI-Specific Architecture: Fallback chains across AI providers
- [ ] **Study:** Design a URL shortener at scale or an AI chatbot platform

**Resource:** [System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer) — Best free resource

</details>

</details>

---

<details open>
<summary>🚀 Phase D — Portfolio & Market Entry &nbsp;|&nbsp; Stage 2 Complete</summary>

<br>

> By this phase you'll have multiple production-grade projects. Time to land Backend Engineer roles.

<details>
<summary>Step 13 · Portfolio & Job Applications</summary>

<br>

**Portfolio Projects (by this point you should have):**
- [ ] ✅ Blog Platform API (FastAPI + PostgreSQL + Auth + Tests + Docker)
- [ ] ✅ Real-time features (WebSockets or SSE)
- [ ] ✅ Deployed live on VPS/Cloud with CI/CD pipeline & Nginx

**Bonus Project Ideas (pick 1-2):**
- [ ] E-commerce API — products, cart, orders, payment integration (Stripe)
- [ ] URL Shortener — with analytics, rate limiting, custom slugs
- [ ] Task Management API — teams, projects, tasks, assignments, deadlines

**GitHub Polish:**
- [ ] Professional README for every repo (architecture diagram, API docs, setup guide)
- [ ] 2-minute Loom video demo for each project
- [ ] Clean commit history with meaningful messages

**Job Targeting:**
- [ ] "Backend Engineer (Python)" — FastAPI/Django, PostgreSQL, Docker
- [ ] "Python Developer" — general Python roles
- [ ] "API Developer" — REST API focused roles

</details>

</details>

---

> **🔗 Next Steps After Stage 2:**
> Next up is Data Engineering (Stage 3) → [Data Engineering Track ➔](./04-data-engineering.md)
> After that, AI Engineering (Stage 4) → [AI Engineering Track ➔](./05-ai-engineering.md)
>
> **Your backend skills (FastAPI, PostgreSQL, Docker, AWS, CI/CD) are the foundation for BOTH paths.**
