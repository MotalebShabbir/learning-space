# 🏗️ Data Engineering — Stage 4 (⚡ Optional Track)

> **Goal:** Become a Data Engineer capable of designing, building, and maintaining scalable data pipelines, data warehouses, and data lakes.
> **When:** Optional — After Stage 3 Backend
> **Status:** ⚡ **Optional.** Take this if you want to add Data Engineering to your toolkit, get a DE job offer, or your AI work involves heavy data pipelines. You can go directly from Stage 3 → Stage 5 (AI Engineering) without this.

### 🔑 Critical Prerequisites from General Backend (Stage 3)
Before starting this stage, you must be extremely comfortable with these specific backend concepts:
- **Advanced Python:** OOP, Generators (for memory-efficient data processing), and Error Handling.
- **PostgreSQL Mastery:** Joins, Indexing strategies, Query optimization (EXPLAIN ANALYZE), and Transactions.
- **Docker:** You must know how to containerize apps and use `docker-compose`, as tools like Airflow and Spark run in containers.
- **Background Jobs / Queues:** Understanding Redis and task queues (like Celery) is essential before learning Airflow.

> **Why this matters:** Data Analysts consume data, AI Engineers train/use models on data. Data Engineers are the ones who *move, clean, and store* that data reliably at massive scale. Every AI team needs Data Engineers.

---

<details open>
<summary>🔵 Phase 1 — Data Warehousing & Modeling &nbsp;|&nbsp; Steps 1–3</summary>

<br>

> You know basic SQL. Now learn how to design databases for analytics (OLAP) rather than transactions (OLTP).

<details>
<summary>Step 1 · Advanced Database Concepts</summary>

<br>

- [ ] OLTP vs OLAP — when to use which
- [ ] Columnar vs Row-oriented databases
- [ ] Advanced SQL: Window Functions, CTEs, Recursive CTEs
- [ ] SQL Performance Tuning (EXPLAIN ANALYZE)
- [ ] **Practice:** Optimize a slow-running SQL query containing multiple joins and aggregations on a large dataset.

</details>

<details>
<summary>Step 2 · Data Modeling (The Core Skill)</summary>

<br>

> A Data Engineer who doesn't know data modeling is just a script writer.

- [ ] Dimensional Modeling (Kimball methodology)
- [ ] Star Schema vs Snowflake Schema
- [ ] Fact Tables vs Dimension Tables
- [ ] Slowly Changing Dimensions (SCD Types 1, 2, 3)
- [ ] Data Vault (concept overview)
- [ ] **Project:** Design a Star Schema for an e-commerce business. Create the DDL (CREATE TABLE) statements for the facts and dimensions.

</details>

<details>
<summary>Step 3 · Data Warehousing & dbt (Data Build Tool)</summary>

<br>

> Cloud Data Warehouses are the industry standard. dbt is the modern tool for transforming data within them.

- [ ] Cloud Data Warehouses: Snowflake or Google BigQuery (pick one to start)
- [ ] ELT vs ETL (Extract, Load, Transform)
- [ ] **dbt (Data Build Tool):**
  - [ ] Setting up dbt core or dbt cloud
  - [ ] Writing models (SQL select statements)
  - [ ] Jinja templating in dbt (`{{ ref() }}`, loops, macros)
  - [ ] dbt tests (unique, not_null, accepted_values)
  - [ ] Documentation auto-generation
- [ ] **Project:** Load raw, messy CSV data into Snowflake/BigQuery. Use dbt to clean, transform, and model it into a Star Schema. Write tests for data quality.

**Resource:** [dbt Fundamentals Course](https://courses.getdbt.com/courses/fundamentals) — Free official course

</details>

</details>

---

<details open>
<summary>🟢 Phase 2 — Pipelines & Orchestration &nbsp;|&nbsp; Steps 4–5</summary>

<br>

> Now that you know how to model data, you need to automate the movement of data on a schedule.

<details>
<summary>Step 4 · Python Data Pipelines</summary>

<br>

- [ ] Interacting with APIs (REST/GraphQL) to extract data
- [ ] Handling pagination, rate limits, and retries in Python
- [ ] File formats: Parquet, Avro, ORC vs CSV/JSON
- [ ] Cloud Storage: AWS S3 or Google Cloud Storage (boto3 in Python)
- [ ] **Project:** Write a Python script that fetches daily weather data from an API, converts it to Parquet, and uploads it to an S3 bucket.

</details>

<details>
<summary>Step 5 · Data Orchestration (Apache Airflow)</summary>

<br>

> Pipelines need to run reliably, on schedule, with error alerts. Airflow is the industry standard.

- [ ] Airflow Architecture (Scheduler, Webserver, Worker, Database)
- [ ] Writing DAGs (Directed Acyclic Graphs) in Python
- [ ] Operators (PythonOperator, BashOperator, PostgresOperator)
- [ ] Sensors and scheduling (cron expressions)
- [ ] XComs — passing data between tasks
- [ ] **Alternative Modern Tools (Overview):** Prefect, Dagster, Mage (good to know they exist)
- [ ] **Project:** Create an Airflow DAG that runs daily:
  1. Triggers the Python script from Step 4 (API to S3).
  2. Loads the S3 data into Snowflake.
  3. Triggers your dbt models to transform the data.
  4. Sends a Slack/Email alert if any task fails.

**Resource:** [Marc Lamberti (YouTube)](https://www.youtube.com/@marclamberti) — The Airflow Guru

</details>

</details>

---

<details open>
<summary>🟡 Phase 3 — Big Data & Cloud &nbsp;|&nbsp; Steps 6–8</summary>

<br>

> When data gets too big for Pandas or a single server, you need distributed computing.

<details>
<summary>Step 6 · Apache Spark & PySpark</summary>

<br>

- [ ] Spark Architecture (Driver, Executors, RDDs, DataFrames)
- [ ] Lazy Evaluation and Transformations vs Actions
- [ ] PySpark DataFrames API (similar to Pandas but distributed)
- [ ] Handling Data Skew and Partitioning
- [ ] Databricks (Cloud platform for Spark)
- [ ] **Project:** Process a 5GB+ dataset using PySpark (on a local cluster or Databricks Community Edition) to find the top 10 most viewed products per category per day.

</details>

<details>
<summary>Step 7 · Streaming (Real-Time Data)</summary>

<br>

> Batch processing (Airflow/Spark) runs periodically. Streaming runs instantly.

- [ ] Batch vs Streaming concepts
- [ ] Apache Kafka (Topics, Producers, Consumers, Brokers)
- [ ] Alternatives: AWS Kinesis, GCP Pub/Sub
- [ ] Spark Structured Streaming
- [ ] **Project:** Write a simple Python producer that streams fake transaction data to Kafka, and a consumer that reads it and prints alerts for high-value transactions.

</details>

<details>
<summary>Step 8 · Cloud, Docker, & DataOps</summary>

<br>

- [ ] **Docker:** Containerize your Python scripts and Airflow setup.
- [ ] **Infrastructure as Code (IaC):** Terraform basics (deploying an S3 bucket or Snowflake database via code).
- [ ] **CI/CD:** GitHub Actions for dbt (run dbt test on every Pull Request).
- [ ] **Data Governance & Data Lineage:** Concepts of tracking where data came from.

</details>

</details>

---

<details open>
<summary>🚀 Phase 4 — Portfolio & Market Entry</summary>

<br>

<details>
<summary>The Capstone DE Project</summary>

<br>

> Build one end-to-end modern data stack (MDS) project.

**Architecture:**
1. **Source:** Fake a PostgreSQL database (acting as a company's main DB) and an external REST API.
2. **Ingestion:** Python + Airflow to extract data daily.
3. **Storage (Data Lake):** AWS S3 (store raw JSON/Parquet).
4. **Data Warehouse:** Snowflake or BigQuery.
5. **Transformation:** dbt to clean and build a Star Schema.
6. **BI/Dashboard:** Connect PowerBI (from Stage 1) to Snowflake and build a dashboard.
7. **Orchestration:** Airflow controls the whole flow.
8. **Deployment:** Entire project is containerized with Docker.

**Job Targeting:**
- [ ] Data Engineer, Junior Data Engineer
- [ ] Analytics Engineer (Heavy focus on SQL, dbt, and Cloud Data Warehouses)
- [ ] Data Platform Engineer

</details>

</details>
