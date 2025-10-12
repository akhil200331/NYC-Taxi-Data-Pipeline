# 🚕 NYC Taxi Data Pipeline – Databricks Medallion Architecture Project

## 📌 Project Overview
This project focuses on developing an end-to-end **data engineering pipeline** for the **NYC Yellow Taxi Trip Records** using **Databricks Delta Live Tables (DLT)**.  
It follows the **Medallion Architecture (Bronze → Silver → Gold)** to transform raw taxi trip data into high-quality analytical datasets.  
The project demonstrates how real-world transportation data can be processed, cleaned, and analyzed efficiently to support **data-driven decision-making**.

---

## 🧠 Business Problem
The NYC Taxi dataset contains millions of records with detailed information about trips, locations, fares, and passengers.  
Analyzing this large dataset directly is challenging due to inconsistencies, missing values, and high data volume.  
The objective of this project is to build a **scalable and automated data pipeline** that ingests, cleans, and enriches the data to uncover key business insights such as **trip trends, passenger behavior, fare structure, and revenue performance**.

---

## 🗂️ Dataset
- **Source:** [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)  
- **Dictionary:** [Data Dictionary PDF](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)  
- **Data Used:** 2025 (January – Present) Parquet files of Yellow Taxi trip data and the NYC Taxi Zone Lookup Table.  

The dataset includes details like pickup/drop-off timestamps, locations, fare amounts, surcharges, tips, payment types, and passenger counts.

---

## 🏗️ Medallion Architecture Pipeline

### 🥉 Bronze Layer — Raw Ingestion
The raw Parquet data was ingested into Databricks using **Auto Loader** and stored in Delta format.  
This layer handled continuous updates from incoming taxi trip data and ensured schema consistency and reliability.

### 🥈 Silver Layer — Data Cleaning and Enrichment
The silver layer focused on **data cleansing and transformation**.  
Invalid records were removed, missing values were handled, and new derived features were added such as:
- **Trip duration** and **average trip speed**  
- **Pickup and drop-off zone names** (mapped using the location lookup table)  
- **Pickup hour** for time-based analytics  

This layer produced a clean and analysis-ready dataset.

### 🥇 Gold Layer — Aggregations and Business Analytics
The gold layer contained **aggregated business metrics** for reporting and visualization.  
It provided insights into:
- Total trips and revenue per month  
- Average fare and distance trends  
- Busiest pickup hours and high-demand zones  
- Vendor-wise and rate-code-based performance  

This layer served as the main source for SQL analytics and dashboard creation.

---

## 🧮 Analytical Insights

### 📊 Trip and Passenger Patterns
- Analyzed the total number of trips to identify monthly and yearly demand patterns.  
- Measured the distribution of **passenger counts**, distinguishing solo riders from group trips.  
- Compared **weekend vs. weekday travel volumes**, helping understand commuter behavior.

### 💳 Payment and Fare Analysis
- Studied **payment trends** to determine the most common payment types used by passengers.  
- Compared **average tips and fares** across payment methods to identify tipping behavior.  
- Evaluated **vendor-based performance** and average earnings per trip.

### 🚦 Extra Charges and Revenue Impact
- Assessed the influence of **MTA tax, surcharges, and other extras** on total revenue.  
- Calculated the **percentage contribution** of extra charges to the overall fare.  
- Derived insights into how these components affect pricing and passenger spending.

### ⚡ Advanced Insights
- Analyzed the **relationship between distance and fare amount** to evaluate pricing efficiency.  
- Identified **anomalies**, such as unusually high fares for short trips.  
- Examined **average trip speeds** to detect congestion-prone periods and zones.  
- Compared **zone-wise revenue contributions**, highlighting the most profitable pickup and drop-off locations.  
- Measured **rate code-based revenue** to understand which service types (e.g., JFK, Newark) generate higher fares.

### 💰 Revenue and Profitability Insights
- Tracked **monthly and daily revenue trends**, identifying high-revenue periods.  
- Calculated **average fare per mile** to assess cost efficiency.  
- Compared **revenue generation by vendor** to evaluate operational performance.  
- Analyzed **busiest hours and top-performing days** to optimize resource allocation.  

---

## 📈 Dashboarding and Visualization
An interactive **Databricks dashboard** was built to visualize insights from the Gold Layer, featuring:
- **Passenger and Trip Insights:** Distribution of passenger counts and trip durations.  
- **Payment Behavior:** Trends in cash vs. card payments and average tips.  
- **Extra Charges Impact:** Share of revenue from surcharges and taxes.  
- **Revenue Analysis:** Monthly revenue trends and vendor comparisons.  
- **Geographical Insights:** Zone-wise revenue heatmaps showing high-demand pickup and drop-off areas.  

These dashboards provided a clear and interactive view of operational performance, helping stakeholders make informed business decisions.

---

## 🧰 Tools and Technologies
- **Databricks** – Delta Live Tables (DLT), SQL, Dashboarding  
- **PySpark** – Data transformation and processing  
- **Delta Lake** – Incremental and versioned data storage  
- **SQL Analytics** – Business reporting and aggregation  
- **Visualization** – Databricks Dashboard / Power BI  

---

## 🚀 Key Outcomes
- Designed and implemented a **scalable Databricks pipeline** using the Medallion Architecture.  
- Processed and transformed millions of records from raw Parquet files into analytical tables.  
- Generated **real-time dashboards** showcasing key performance metrics.  
- Extracted insights on **payment trends, passenger behavior, and revenue generation**.  
- Enhanced **data analytics and visualization skills** through large-scale dataset analysis.  


