# ⚙️ Backend Engineering Roadmap

> Tracking my backend engineering journey: Node.js, Express, TypeScript, PostgreSQL, and Python/FastAPI.

---

<details>
<summary>✅ Phase 1 — JS + Node.js Core &nbsp;|&nbsp; COMPLETED</summary>

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

---

<details>
<summary>🟢 Phase 2 — Backend API + Security &nbsp;|&nbsp; Steps 1–10</summary>

<br>

> The backbone of your employability. This is your primary job skill.

<details>
<summary>Steps 1–2 · Express.js Fundamentals</summary>

<br>

- [ ] Routing — GET, POST, PUT, DELETE
- [ ] Middleware — custom + built-in (body-parser, cors, morgan)
- [ ] Error handling middleware
- [ ] MVC folder structure
- [ ] Request/Response cycle
- [ ] **Project:** Basic CRUD REST API (Notes/Todo)

**Resource:** [Express.js Crash Course — Traversy Media](https://www.youtube.com/watch?v=CnH3kAXSrmU) (free)

</details>

<details>
<summary>Steps 3–4 · TypeScript + Express</summary>

<br>

- [ ] Types, Interfaces, Generics
- [ ] Zod — runtime input validation
- [ ] ts-node, tsx setup
- [ ] Express project structure with TypeScript
- [ ] Enums, Union types, Type narrowing
- [ ] **Refactor:** Step 3-4 project → TypeScript

**Resource:** [Total TypeScript — Beginner's Tutorial](https://www.totaltypescript.com/tutorials/beginners-typescript) (free)
**Resource:** [Matt Pocock YouTube](https://www.youtube.com/@maaborern) (free)

</details>

<details>
<summary>Steps 5–6 · PostgreSQL + Prisma</summary>

<br>

- [ ] Tables, Relations (1:1, 1:N, M:N)
- [ ] Joins — INNER, LEFT, RIGHT
- [ ] Indexes, Transactions
- [ ] psql CLI basics
- [ ] Prisma schema design
- [ ] Prisma migration + CRUD operations
- [ ] **Project:** User + Data management API (Express + TS + Prisma)

**Resource:** [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) (free)
**Resource:** [Prisma Docs — Quickstart](https://www.prisma.io/docs/getting-started) (free)

</details>

<details>
<summary>Steps 7–8 · Auth + Application Security</summary>

<br>

- [ ] JWT — access token + refresh token flow
- [ ] bcrypt — password hashing
- [ ] Cookie vs localStorage — security trade-offs
- [ ] RBAC — Role-Based Access Control
- [ ] Protected routes middleware
- [ ] CORS configuration
- [ ] Helmet.js — HTTP header security
- [ ] Rate limiting — express-rate-limit
- [ ] SQL injection protection (Prisma handles this, but understand why)
- [ ] XSS protection — input sanitization
- [ ] Environment variable best practices
- [ ] **Project:** Full auth system with JWT + RBAC + refresh tokens

</details>

<details>
<summary>Step 9 · Testing</summary>

<br>

> Write tests like you expect the code to break — because it will.

- [ ] Jest — unit testing
- [ ] Supertest — API integration testing
- [ ] Test folder structure — keep tests next to code
- [ ] Mocking — DB calls, external APIs
- [ ] Testing auth-protected routes
- [ ] Testing error cases and edge cases — not just the happy path
- [ ] **Project:** Full test suite for the auth system

</details>

<details>
<summary>Step 10 · API Design + Documentation + First Deployment 🚀</summary>

<br>

- [ ] REST conventions — naming, status codes, versioning
- [ ] Pagination, filtering, sorting
- [ ] API versioning (/api/v1/)
- [ ] Swagger / OpenAPI documentation
- [ ] Deploy to Railway or Render
- [ ] HTTPS enforcement
- [ ] Secrets management in production
- [ ] **Project:** Blog API — Express + TS + PostgreSQL + Auth + Tests + Swagger + **Live Deployed**

> **Your first deployed project. This is your portfolio cornerstone. Write a great README — in English, with screenshots.**

</details>

</details>

---

<details>
<summary>🟡 Phase 3 — Python + FastAPI &nbsp;|&nbsp; Steps 11–13</summary>

<br>

> The language of the AI ecosystem. Your JS mastery will make Python fast to learn.

<details>
<summary>Step 11 · Python Production-Ready</summary>

<br>

- [ ] venv, pip — virtual environment
- [ ] Type hints, dataclasses
- [ ] httpx, requests — API calls
- [ ] Pydantic — data validation (FastAPI's foundation)
- [ ] python-dotenv
- [ ] File I/O, JSON handling
- [ ] List comprehension, generators, decorators

**Resource:** [Python for JavaScript Developers](https://www.valentinog.com/blog/python-for-js/) (free)
**Resource:** [Corey Schafer Python Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU) (free)

</details>

<details>
<summary>Steps 12–13 · FastAPI</summary>

<br>

- [ ] Routes, async endpoints
- [ ] Pydantic request/response models
- [ ] Dependency injection
- [ ] Connect to PostgreSQL (SQLAlchemy + asyncpg)
- [ ] FastAPI security (OAuth2, API keys)
- [ ] Auto-generated docs (Swagger UI + ReDoc — built-in)
- [ ] pytest + httpx — testing
- [ ] **Project:** Blog API rebuild — FastAPI version + tested + documented + **deployed**

**Resource:** [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/) (free, excellent)

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
- [ ] **Exercise:** Dockerize your Blog API (both Node.js and FastAPI versions)

**Resource:** [Docker Crash Course — TechWorld with Nana](https://www.youtube.com/watch?v=pg19Z8LL06w) (free)

</details>

<details>
<summary>Step 15 · CI/CD + Portfolio Polish</summary>

<br>

- [ ] GitHub Actions — test → build → deploy pipeline
- [ ] GitHub profile polish — 4-5 pinned projects with great READMEs
- [ ] LinkedIn update — "Backend Developer | Node.js · TypeScript · PostgreSQL · Python"
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

