# 🛠️ Data Foundation — Stage 1 (Core Engineering Path)

> **Goal:** Build the essential data manipulation, database, and programming foundation required for Backend, Data Engineering, and AI Engineering.
> **When:** Stage 1 of the roadmap
> **Why this first:** Before building backend systems or training AI models, you must know how to fetch, process, and store data programmatically. This stage replaces pure 'analyst' tools (like PowerBI) with engineering fundamentals.

---

<details open>
<summary>🟢 Stage 1 (Part 1) — Python, Formats & CLI &nbsp;|&nbsp; The Prerequisites</summary>

<br>

> **Target:** Get comfortable with the command line, version control, and programmatically handling different data formats using Python.

---

<details>
<summary>Step 1 · Command Line & Git Basics (Week 1)</summary>

<br>

> Every backend and data engineer lives in the terminal. Learn this before writing code.

**Linux CLI (Bash)**
- [ ] Navigation: `cd`, `ls`, `pwd`, `mkdir`, `touch`, `rm`
- [ ] File Inspection: `cat`, `less`, `head`, `tail`, `grep`
- [ ] Permissions & execution: `chmod`, `./script.sh`

**Git & GitHub**
- [ ] Version Control basics: `git init`, `git add`, `git commit`
- [ ] Branching: `git branch`, `git checkout` / `git switch`, `git merge`
- [ ] Remote repositories: `git push`, `git pull`, `git clone`
- [ ] **Practice:** Create a GitHub repo and push a sample text file via terminal.

</details>

<details>
<summary>Step 2 · Python Fundamentals (Week 2–3)</summary>

<br>

> Python is the lingua franca of Data and AI. With your programming background, this will be quick.

- [ ] Variables, Data Types (str, int, float, list, dict, set)
- [ ] Control Flow — `if/else`, `for`, `while`
- [ ] Functions — `def`, `*args`, `**kwargs`
- [ ] List & Dict Comprehensions
- [ ] Error handling — `try/except/finally`
- [ ] Virtual Environments — `venv`, `pip` (Crucial for managing dependencies)

**Resource:** [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
</details>

<details>
<summary>Step 3 · Data Formats & APIs (Week 4)</summary>

<br>

> Data rarely comes in neat Excel files. Learn to fetch and parse data programmatically.

**Core Data Formats**
- [ ] **CSV:** Reading and writing using Python's `csv` module.
- [ ] **JSON:** The language of the web. Nested dictionaries, `json.loads()`, `json.dumps()`.
- [ ] **Parquet:** Introduction to columnar storage (used heavily in Data Engineering).

**APIs & Web Scraping**
- [ ] REST APIs basics: GET vs POST, HTTP Status Codes.
- [ ] Fetching data using Python `requests` library.
- [ ] Intro to Web Scraping (Optional but helpful): `BeautifulSoup` basics.
- [ ] **Mini Project:** Write a Python script to fetch user data from a public API (e.g., JSONPlaceholder), parse the JSON, and save it locally as a CSV file.

</details>

</details>

---

<details open>
<summary>🟡 Stage 1 (Part 2) — Databases & Data Processing &nbsp;|&nbsp; Core Foundation</summary>

<br>

> **Target:** Master how to store, query, and process large datasets.

---

<details>
<summary>Step 4 · SQL & Relational Databases (Week 5–7)</summary>

<br>

> SQL is the universal language of data. Backend, Data, or AI Engineer — everyone needs it.

**Basic to Intermediate SQL (PostgreSQL)**
- [ ] SELECT, WHERE, ORDER BY, LIMIT, DISTINCT
- [ ] Aggregation: GROUP BY, HAVING, COUNT, SUM, AVG
- [ ] Joins: INNER, LEFT, RIGHT, FULL OUTER
- [ ] Subqueries and CTEs (WITH clause)

**Advanced SQL & Database Design**
- [ ] Window Functions: ROW_NUMBER(), RANK(), SUM() OVER()
- [ ] Performance: EXPLAIN ANALYZE, Indexing strategies
- [ ] Normalization: 1NF, 2NF, 3NF
- [ ] **Practice:** [SQLBolt](https://sqlbolt.com/) (Beginner), [DataLemur](https://datalemur.com/) (Advanced)

</details>

<details>
<summary>Step 5 · Intro to NoSQL Databases (Week 8)</summary>

<br>

> Not all data fits in tables. Understand when to break the SQL rules.

- [ ] Relational (SQL) vs Non-Relational (NoSQL)
- [ ] Document Stores: **MongoDB** basics (JSON-like documents, collections)
- [ ] Key-Value Stores: **Redis** basics (Caching, fast reads)
- [ ] **Mini Project:** Spin up a free MongoDB Atlas cluster, connect via Python (`pymongo`), and insert/query JSON data.

</details>

<details>
<summary>Step 6 · Data Processing with Pandas (Week 9–10)</summary>

<br>

> Pandas allows you to handle and clean massive datasets entirely through code.

- [ ] DataFrame basics — `read_csv`, `read_json`, `head()`, `info()`
- [ ] Filtering, Sorting, and GroupBy
- [ ] Merge/Join DataFrames
- [ ] Handling missing data — `fillna()`, `dropna()`
- [ ] **Resource:** [Kaggle — Pandas Course](https://www.kaggle.com/learn/pandas)

</details>

<details>
<summary>Step 7 · Basic Applied Statistics (Week 11)</summary>

<br>

> Before passing data to AI models, you must understand its statistical properties.

- [ ] Descriptive Stats: Mean, Median, Mode, Variance, Standard Deviation
- [ ] Probability basics & Normal Distribution
- [ ] Outlier detection and data correlation
- [ ] *Note: No need for deep math yet, just understand the concepts to spot bad data.*

</details>

</details>

---

<details open>
<summary>🚀 Capstone — Build an ETL Pipeline (Week 12)</summary>

<br>

> **Target:** Combine Python, APIs, Pandas, and SQL into a single engineering project.

- [ ] **Extract:** Write a Python script to pull live data from a public REST API (e.g., Weather API, Crypto API).
- [ ] **Transform:** Load the JSON data into a Pandas DataFrame, clean missing values, drop unnecessary columns, and convert timestamps.
- [ ] **Load:** Connect to a PostgreSQL (or MongoDB) database using Python and insert the cleaned data.
- [ ] **Deploy:** Push the script to GitHub and run it via command line.

> **Why this matters:** This is a miniature Data Engineering pipeline. Understanding this proves you have a solid "Data Foundation."

</details>

---

> **🔗 Next Stages:**
> Data Foundation complete? → [Backend Engineering Track ➔](./02-backend-engineering.md) (Stage 2)
> Backend complete? → [Data Engineering Track ➔](./03-data-engineering.md) (Stage 3)

---

> **Remember:** This is the bedrock of your engineering journey. Master these fundamentals, and the advanced frameworks will come easily.
