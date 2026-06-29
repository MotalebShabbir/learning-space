# ⚙️ Backend Engineering Roadmap

> Tracking my backend engineering journey: Python/FastAPI (Primary) and Node.js/Express (Secondary).

---

<details open>
<summary>🟢 Phase 1 — Python Core to Advanced &nbsp;|&nbsp; Steps 1–2</summary>

<br>

> Master the language of AI before diving into backend frameworks.

<details>
<summary>Steps 1–2 · Python Fundamentals & Production-Ready</summary>

<br>

- [x] venv, pip — virtual environment
- [ ] Variables, Data Types, Lists, Dictionaries, Sets
- [ ] Control Flow (if/else, loops)
- [ ] Functions, *args, **kwargs
- [ ] List comprehension, generators, decorators
- [ ] Type hints, dataclasses
- [ ] Object-Oriented Programming (OOP) in Python
- [ ] httpx, requests — API calls
- [ ] Pydantic — data validation (FastAPI's foundation)
- [ ] python-dotenv
- [ ] File I/O, JSON handling
- [ ] asyncio fundamentals — event loop, async/await, gather, tasks
- [ ] Context managers (with statement) — resource management

**Resource:** [Python for JavaScript Developers](https://www.valentinog.com/blog/python-for-js/) (free)
**Resource:** [Corey Schafer Python Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU) (free)

</details>

</details>

---

<details>
<summary>🟢 Phase 2 — FastAPI (Primary Backend) &nbsp;|&nbsp; Steps 3–8</summary>

<br>

> The backbone of your AI Engineering identity. You will learn all core backend concepts (REST, Auth, DB) using FastAPI.

<details>
<summary>Steps 3–4 · FastAPI Fundamentals</summary>

<br>

- [ ] Routing — GET, POST, PUT, DELETE
- [ ] Path parameters and Query parameters
- [ ] Pydantic request/response models
- [ ] Dependency injection
- [ ] Error handling (HTTPException)
- [ ] Custom error classes
- [ ] Logging — structlog or loguru (Python structured logging)
- [ ] Project folder structure for FastAPI
- [ ] **Project:** Basic CRUD REST API (Notes/Todo)

**Resource:** [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/) (free, excellent)

</details>

<details>
<summary>Steps 5–6 · PostgreSQL + SQLAlchemy + Alembic</summary>

<br>

- [ ] Tables, Relations (1:1, 1:N, M:N)
- [ ] Joins — INNER, LEFT, RIGHT
- [ ] Indexes, Transactions
- [ ] Connect to PostgreSQL (SQLAlchemy + asyncpg)
- [ ] SQLAlchemy models
- [ ] Alembic — database migration
- [ ] CRUD operations with SQLAlchemy
- [ ] **Project:** User + Data management API (FastAPI + PostgreSQL)

**Resource:** [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) (free)

</details>

<details>
<summary>Steps 7–8 · Auth + Application Security</summary>

<br>

- [ ] JWT — access token + refresh token flow
- [ ] Passlib + bcrypt — password hashing
- [ ] FastAPI security (OAuth2 with Password (and hashing), Bearer with JWT)
- [ ] RBAC — Role-Based Access Control
- [ ] CORS configuration (CORSMiddleware)
- [ ] Rate limiting in FastAPI
- [ ] SQL injection protection (SQLAlchemy handles this)
- [ ] Environment variable best practices (Pydantic BaseSettings)
- [ ] **Project:** Full auth system with JWT + RBAC

</details>

<details>
<summary>Step 9 · Testing</summary>

<br>

> Write tests like you expect the code to break — because it will.

- [ ] pytest — unit testing
- [ ] pytest-asyncio and httpx — API integration testing
- [ ] Test folder structure — keep tests next to code
- [ ] Mocking — DB calls, external APIs
- [ ] Testing auth-protected routes
- [ ] Testing error cases and edge cases
- [ ] **Project:** Full test suite for the auth system

</details>

<details>
<summary>Step 10 · API Design + Documentation + First Deployment 🚀</summary>

<br>

- [ ] REST conventions — naming, status codes, versioning
- [ ] Pagination, filtering, sorting
- [ ] API versioning (/api/v1/)
- [ ] Auto-generated docs (Swagger UI + ReDoc — built-in in FastAPI)
- [ ] Deploy to Railway or Render
- [ ] HTTPS enforcement
- [ ] Secrets management in production
- [ ] **Project:** Blog API — FastAPI + PostgreSQL + Auth + Tests + Swagger + **Live Deployed**

> **Your first deployed project. This is your portfolio cornerstone. Write a great README — in English, with screenshots.**

</details>

</details>

---

<details>
<summary>🟡 Phase 3 — Node.js + Express (Secondary Backend) &nbsp;|&nbsp; Steps 11–13</summary>

<br>

> You already know the backend concepts from Phase 2. Now just map them to the Express ecosystem. This makes you a dual-stack developer, expanding job opportunities.

<details>
<summary>✅ Step 11 · JS + Node.js Core (COMPLETED)</summary>

<br>

- [x] JS fundamentals — map, filter, reduce
- [x] Destructuring, spread/rest, template literals
- [x] Closures, scope, hoisting
- [x] Promises, async/await
- [x] fetch API, error handling
- [x] Event Loop — how JS runs
- [x] Node.js modules (import/export, CommonJS)
- [x] fs, path, os modules
- [x] npm, dotenv, nodemon
- [x] **Project:** Prayer Time CLI (Aladhan API) ✅

</details>

<details>
<summary>Steps 12 · Express.js + TypeScript Fundamentals</summary>

<br>

- [ ] Types, Interfaces, Generics
- [ ] Zod — runtime input validation (similar to Pydantic)
- [ ] ts-node, tsx setup
- [ ] Express routing and middleware (body-parser, cors, morgan)
- [ ] Error handling middleware in Express
- [ ] Express project structure with TypeScript
- [ ] **Resource:** [Express.js Crash Course](https://www.youtube.com/watch?v=CnH3kAXSrmU)
- [ ] **Resource:** [Total TypeScript](https://www.totaltypescript.com/tutorials/beginners-typescript)

</details>

<details>
<summary>Step 13 · Prisma, Auth & Testing in Node</summary>

<br>

- [ ] Prisma schema design (Node equivalent of SQLAlchemy models)
- [ ] Prisma migration + CRUD operations
- [ ] JWT Auth implementation in Express
- [ ] Jest + Supertest (Node equivalent of pytest + httpx)
- [ ] **Project:** Blog API rebuild — Express + TS + Prisma version + tested + **deployed**

</details>

</details>

---

<details>
<summary>⭐ Phase 4 — Docker + Deploy + Job Applications Start 🎯 &nbsp;|&nbsp; Steps 14–16</summary>

<br>

> These 3 steps prepare you to start applying. From here, you run two tracks in parallel.

<details>
<summary>Step 14 · Docker Essentials</summary>

<br>

- [ ] Dockerfile for Node.js + Python apps
- [ ] docker-compose — app + DB + Redis
- [ ] Docker security basics — non-root user, minimal base
- [ ] **Exercise:** Dockerize your Blog API (both FastAPI and Node.js versions)

**Resource:** [Docker Crash Course — TechWorld with Nana](https://www.youtube.com/watch?v=pg19Z8LL06w) (free)

</details>

<details>
<summary>Step 15 · CI/CD + Portfolio Polish</summary>

<br>

- [ ] GitHub Actions — test → build → deploy pipeline
- [ ] GitHub profile polish — 4-5 pinned projects with great READMEs
- [ ] LinkedIn update — "Python Developer | FastAPI · Node.js · PostgreSQL"
- [ ] Portfolio website (simple React deploy on Vercel)
- [ ] Write 2-3 case studies: "Problem → Solution → Result"

</details>

<details>
<summary>Step 16 · Job Application Sprint Begins</summary>

<br>

- [ ] Resume — ATS-friendly, projects-focused
- [ ] Upwork profile — Backend Developer niche
- [ ] Start applying: LinkedIn Jobs, Wellfound, Remote.co, RemoteOK
- [ ] Daily: 2-3 applications + 2 LeetCode problems

> **DUAL TRACK STARTS:**
> - **Track A (1-2 hr/day):** Job applications + interview prep + LeetCode
> - **Track B (2-3 hr/day):** AI Engineering learning (AI Engineering)

</details>

</details>

---
