# 📊 Data Foundation — Stage 1 (Market Entry Path)

> **Goal:** Acquire marketable skills in Python and SQL in the shortest possible time and start earning.
> **When:** Stage 1 of the roadmap
> **Why this first:** Becoming a Data Engineer takes 6-8 months. But Python + SQL can land you backend intern or data extraction work in 2-3 months.

---

<details open>
<summary>🟢 Stage 1 — SQL + Python &nbsp;|&nbsp; Core Data Foundation</summary>

<br>

> **Target:** Build the essential programming and query foundation required for data engineering.

---

<details>
<summary>Step 1 · SQL Fundamentals (Week 1–3)</summary>

<br>

> SQL is the universal language of data. Backend Engineer, Data Engineer — everyone needs it. Learn it once, use it forever.

**Basic Queries**
- [ ] SELECT, WHERE, ORDER BY, LIMIT
- [ ] AND, OR, NOT, IN, BETWEEN, LIKE
- [ ] DISTINCT, AS (aliases)
- [ ] NULL handling — IS NULL, COALESCE, IFNULL

**Aggregation (Most Used in Real Jobs)**
- [ ] GROUP BY + Aggregate functions (COUNT, SUM, AVG, MIN, MAX)
- [ ] HAVING — filter after grouping
- [ ] **This is the #1 topic asked in interviews**

**Joins (Critical)**
- [ ] INNER JOIN — matching records
- [ ] LEFT JOIN — all from left + matching from right
- [ ] RIGHT JOIN, FULL OUTER JOIN
- [ ] Self JOIN
- [ ] **Practice:** Write complex joins across 2-3 related tables

**Intermediate**
- [ ] Subqueries — WHERE IN (SELECT ...)
- [ ] CTEs (Common Table Expressions) — WITH clause
- [ ] Window Functions — ROW_NUMBER(), RANK(), LAG(), LEAD(), SUM() OVER()
- [ ] CASE WHEN — conditional logic in SQL
- [ ] String functions — CONCAT, SUBSTRING, TRIM, UPPER, LOWER

**Portfolio Project:**
- [ ] **Project 1:** Create a sample ecommerce database (PostgreSQL) → Answer 10 business questions with SQL → Export results
- [ ] Create a GitHub repo — "SQL Business Analysis Portfolio"

**Setup:** PostgreSQL locally (or use [SQLiteOnline](https://sqliteonline.com/) to start)
**Resource:** [SQLBolt](https://sqlbolt.com/) — Interactive, free, best for beginners
**Resource:** [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/) — Real-world focused
**Practice:** [HackerRank SQL](https://www.hackerrank.com/domains/sql) — Solve 2-3 problems daily

</details>

<details>
<summary>Step 2 · Python Fundamentals (Week 3–5)</summary>

<br>

> With your C++ background, Python will feel incredibly easy. The syntax is much simpler.

- [ ] Variables, Data Types (str, int, float, bool, list, dict, tuple, set)
- [ ] Control Flow — if/elif/else, for, while
- [ ] Functions — def, *args, **kwargs, return
- [ ] List Comprehension — `[x for x in range(10) if x > 5]`
- [ ] File I/O — read/write CSV, JSON, text files
- [ ] Error handling — try/except
- [ ] Virtual environments — venv, pip
- [ ] **Mini Project:** CSV file reader — read a sales CSV → calculate totals → print report

**Resource:** [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — Free, practical
**Resource:** [Python.org Official Tutorial](https://docs.python.org/3/tutorial/) — Reference

</details>

---

<details open>
<summary>🟡 Stage 1 (Part 2) — Pandas + Advanced Analytics &nbsp;|&nbsp; Level Up</summary>

<br>

> **Target:** Upgrade to Python-powered Data Manipulation.
> **Why Python:** Python handles unlimited data and it opens the door to Backend and Data Engineering.

---

<details>
<summary>Step 3 · Pandas + Data Manipulation (Week 5–8)</summary>

<br>

> Pandas = Python's Excel. Everything you did in Excel, you'll do in Python — but with 100x more data.

- [ ] DataFrame basics — read_csv, head(), info(), describe()
- [ ] Filtering — `df[df['sales'] > 1000]`
- [ ] Sorting — sort_values()
- [ ] GroupBy + Aggregation — `.groupby('category').sum()` (Python version of Excel Pivot Tables)
- [ ] Merge/Join — `pd.merge()` (Python version of SQL JOIN)
- [ ] Pivot Tables — `df.pivot_table()`
- [ ] Handling missing data — fillna(), dropna()
- [ ] String operations — `.str.contains()`, `.str.split()`
- [ ] Date/Time handling — pd.to_datetime(), .dt accessor
- [ ] **Project 2:** Clean a messy real-world dataset using Pandas instead of Excel — see how much faster it is

**Resource:** [Kaggle — Pandas Course](https://www.kaggle.com/learn/pandas) — Free, hands-on
**Resource:** [Pandas Documentation](https://pandas.pydata.org/docs/) — Reference

</details>

</details>

<details>
<summary>Step 4 · Advanced SQL + Database Skills (Week 8–10)</summary>

<br>

> You learned basic SQL in Step 1. Now go to the advanced level — this is what bridges you to Backend and DE.

- [ ] Advanced Window Functions — PARTITION BY, running totals, moving averages
- [ ] Complex CTEs — recursive CTEs, chained CTEs
- [ ] Subqueries vs Joins — performance comparison
- [ ] EXPLAIN ANALYZE — query performance tuning
- [ ] Indexing strategies — when and why
- [ ] Database design — normalization (1NF, 2NF, 3NF), star schema
- [ ] **Project 3:** Build a complete PostgreSQL analytics database — design schema → load sample data → write 20 complex queries

**Practice:** [DataLemur](https://datalemur.com/) — Real interview SQL questions
**Practice:** [StrataScratch](https://www.stratascratch.com/) — Company-specific SQL problems

</details>

<details>
<summary>Step 5 · First Income — Backend Intern / Junior Dev (Week 10+)</summary>

<br>

> You know Python + SQL + Pandas. Time to start looking for work.

**Upwork Profile Update:**
- [ ] Title: "Python Developer | Data Extraction & Scripting"
- [ ] Add new projects to your portfolio

**New Job Types to Target:**
- [ ] "Web scraping + analysis" — collect data from websites → analyze
- [ ] "Database query optimization" — fix slow queries
- [ ] "Automated reporting" — Python scripts for auto-generated reports
- [ ] "Data cleaning & formatting"

**Job Applications (Parallel):**
- [ ] "Backend Intern (Python)" — remote positions
- [ ] "Junior Data Engineer" — focusing on Python and SQL pipelines

</details>

</details>

</details>

---

> **🔗 Next Stages:**
> Stage 1 complete? → [Backend Engineering Track ➔](./02-backend-engineering.md) (Stage 2)
> Backend complete? → [Data Engineering Track ➔](./03-data-engineering.md) (Stage 3)

---

> **Remember:** Don't stop climbing just because the current step feels comfortable. Keep your ultimate goal in sight!
