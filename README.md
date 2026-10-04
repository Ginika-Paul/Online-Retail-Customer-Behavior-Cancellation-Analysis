# End-to-End E-Commerce Analytics: Customer Behavior & Cancellation Study

## 📊 Executive Summary
This end-to-end data analytics project investigates customer purchasing behavior, revenue structures, and order cancellation dynamics for a global online retail enterprise. 

The core objective was to solve a specific operational puzzle: **Are repeat customers canceling more orders simply due to higher transaction volumes, or does their baseline cancellation probability scale upward as purchase frequency increases?**

### 💡 Core Discoveries
* **The Revenue Engine:** Repeat buyers make up only **38% of the customer base** but generate **79.5% of total sales revenue** (£8.5M vs. £2.2M).
* **The Retention Leak:** Order cancellation volumes are disproportionately concentrated among high-frequency customers.
* **The Frequency Vector:** Cancellation rates scale exponentially based on user loyalty, climbing steadily from **4.22%** for single-purchase users to **19.14%** for power users (11+ purchases).

---

## 🛠️ Tech Stack & Architecture
* **Data Engineering & Imputation:** Python, Pandas
* **Data Warehousing & Structuring:** Microsoft Excel, SQL Server
* **Business Intelligence & Data Modeling:** Power BI, DAX (Data Analysis Expressions)

---

## 🏗️ Data Preparation Pipeline (Python & Pandas)
Before visualization, the raw transactional dataset containing over **500,000 records** was programmatically cleaned using Python to ensure architectural integrity:
* **Automated Imputation Logic:** Cleaned missing product records by programmatically cross-referencing and matching missing text fields using historical `StockCode` mappings.
* **String Standardization:** Structuralized inconsistent, trailing, and mistyped product description values.
* **Feature Engineering:** Isolated canceled transactions by parsing invoice alphanumeric conventions to separate clean revenue rows from active reversals.
* **Customer Segmentation:** Computed custom attributes and specialized cohort groupings to track user frequency buckets.

---

## 📈 Deep-Dive Analytical Findings

### 1. The Value Disparity (One-Time vs. Repeat Cohorts)
The exploratory analysis identified **8,082 unique customer profiles** across the transactional lifecycle. While acquiring new traffic keeps total customer counts high, active repeat behaviors completely drive financial viability:

* **One-Time Buyers:** 62% of total customer base | **£2.2 Million** total revenue contribution.
* **Repeat Buyers:** 38% of total customer base | **£8.5 Million** total revenue contribution.

### 2. The Loyalty Reversal (Cancellation Volatility)
While repeat buyers keep the business alive, they also account for the highest overhead leaks, driving **3,600 individual cancellations** compared to only **200 cancellations** from one-time shoppers. 

To determine if this was a natural byproduct of volume or a systemic breakdown, transactions were segmented by frequency:

| Purchase Frequency Bucket | Metric Baseline | Target Cancellation Rate |
| :--- | :--- | :--- |
| **1 Purchase** | New/Trial Users | **4.22%** |
| **2 Purchases** | Returning Cohort | **12.00%** |
| **3–5 Purchases** | Core Customers | **14.80%** |
| **6–10 Purchases** | High-Value Advocates | **17.79%** |
| **11+ Purchases** | Enterprise/Power Users | **19.14%** |

**Analytical Vector:** The definitive upward trend proves that cancellation risk scales with loyalty. This suggests that backend platform friction, delivery lag, or stock exhaustion issues disproportionately penalize the company’s most valuable accounts.

### 3. Product & Seasonal Congestion Points
* **Product Risk Profiles:** Cancellation instances heavily cluster around specific high-volume standard units, including *Manual, Regency Cakestand 3 Tier, Postage, Jam Making Set With Jars*, and *Set of 3 Cake Tins Pantry Design*. 
* **Q4 Seasonality:** Cancelled invoices tracked a dramatic upward trajectory toward the close of the calendar year, escalating from a baseline of **260 instances in January** to a peak of **472 instances in December** (coinciding with holiday logistics constraints).

---

## 🚀 Strategic Business Recommendations

Based on the empirical evidence, the business should deploy the following mitigation strategies:
1. **Optimize High-Frequency Fulfillment:** Implement priority logistics processing or dedicated inventory allocations for the `11+ Purchase` customer tier to drive their 19.14% cancellation rate back down to industry baselines.
2. **Execute Root-Cause Audits on High-Risk SKUs:** Investigate inventory, description discrepancies, or quality issues for the top 5 high-volume canceled products (e.g., *Regency Cakestand*) to check for listing errors or systematic return reasons.
3. **Seasonal Buffer Adjustments:** Scale supply chain capacity, server performance checking, and safety stock thresholds ahead of the Q4 holiday surge (November–December) to mitigate transaction drops during peak periods.

---

## 📂 Project Structure & Deliverables
* **[Python Data Cleaning Script](./Python_Cleaning_Script.ipynb):** Comprehensive source code for structural cleaning, data imputation, and initial statistical validation via Pandas.
* **[Power BI Dashboard File](./Ecom_Analysis_Dashboard.pbix):** Interactive `.pbix` framework featuring transactional tracking, dynamic segmentation panels, and automated KPI scorecards.
*
