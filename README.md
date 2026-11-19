# Churn Analysis & Customer Intelligence

**Tools:** SQL \| Python \| Pandas \| NumPy \| Matplotlib

## 1. Project Overview

This project focuses on analyzing customer churn for a
subscription-based business to identify customer segments with higher
churn rates, understand the revenue impact of churn, and develop
data-driven customer retention strategies.

Using SQL and Python, I integrated customer demographics, subscription
information, and customer support records to perform exploratory data
analysis, calculate key business metrics, and identify patterns
associated with customer churn.

The analysis focuses on customer behavior, subscription plans,
geographic segmentation, customer lifetime value (CLTV), and support
escalations.

## 2. Business Objectives

-   Calculate overall customer churn and retention rates.
-   Identify subscription plans with the highest churn rates.
-   Analyze geographic variations in customer churn.
-   Evaluate the revenue impact of customer churn.
-   Analyze customer tenure and Customer Lifetime Value (CLTV).
-   Investigate the relationship between customer support escalations
    and churn.
-   Classify customers into different churn-risk categories.
-   Develop actionable recommendations to improve customer retention.

## 3. Dataset Description

The project uses three relational tables extracted using SQL.

  ------------------------------------------------------------------------
  Table                 Description                                Records
  --------------------- --------------------- ----------------------------
  `db_customer`         Customer demographics                           21
                        and geographic        
                        information           

  `db_subscription`     Subscription details,                           21
                        charges, CLTV and     
                        churn information     

  `db_support`          Customer complaints,                             9
                        escalations and       
                        satisfaction scores   
  ------------------------------------------------------------------------

### Key Columns

**Customer Table** - `customerid` - `country` - `state` - `gender` -
`dob` - `interests`

**Subscription Table** - `customerid` - `subscription_start_date` -
`subscription_type` - `renewal_date` - `plan_type` - `contract_type` -
`cancellation_date` - `cancellation_reason` - `monthly_charges` -
`cltv` - `churn_score`

**Support Table** - `customerid` - `complaint_date` - `escalations` -
`csat_score` - `comment`

## 4. Tools & Technologies

  Technology   Purpose
  ------------ -------------------------------------------------
  SQL          Data extraction and relational data integration
  Python       Data analysis and processing
  Pandas       Data manipulation, aggregation and segmentation
  NumPy        Numerical operations
  Matplotlib   Data visualization

## 5. Analysis & Methodology

### A. Data Extraction and Integration

-   Extracted customer, subscription, and support records using SQL.
-   Imported the extracted datasets into Python as Pandas DataFrames.
-   Integrated relevant information using customer IDs.
-   Prepared the datasets for further analysis.

### B. Data Preparation

-   Converted subscription-related date columns into appropriate
    datetime formats.
-   Prepared customer tenure calculations.
-   Created churn-related analytical fields.
-   Organized customer and subscription information for segmentation and
    analysis.

### C. Exploratory Data Analysis (EDA)

Performed analysis across multiple business dimensions:

-   Overall churn and retention analysis.
-   Subscription plan-wise churn analysis.
-   Geographic churn analysis.
-   Customer tenure analysis.
-   CLTV analysis.
-   Customer support and escalation analysis.

### D. Customer Risk Classification

Classified customers into three churn-risk categories:

-   Low Risk
-   Medium Risk
-   High Risk

Customer risk classification was used to identify customers requiring
additional retention attention.

### E. Customer Support Analysis

Analyzed customer complaints and support escalations to investigate
their relationship with customer churn.

Calculated the correlation between support escalations and churn to
identify potential customer-experience issues.

## 6. Key Business Findings

### A. Overall Churn Performance

  Metric                  Result
  ----------------- ------------
  Total Customers             21
  Churn Rate              28.57%
  Retention Rate          71.43%
  Average Tenure      1,586 days
  Average CLTV          1,175.07

The business experienced a customer churn rate of approximately 28.57%,
indicating that more than one-quarter of the analyzed customers had
churned.

### B. Subscription Plan Analysis

  Subscription Plan     Customers   Churn Rate
  ------------------- ----------- ------------
  Basic                         5       60.00%
  Premium                       7       14.29%
  Standard                      9       22.22%

**Key Finding:**

The Basic subscription plan recorded the highest churn rate at 60%,
significantly higher than the Premium and Standard plans.

This indicates that Basic plan customers represent an important segment
for further retention analysis.

### C. Geographic Churn Analysis

  State             Churn Rate
  --------------- ------------
  Karnataka            100.00%
  Meghalaya             66.67%
  Telangana             50.00%
  Delhi                 25.00%
  Kathmandu              0.00%
  Maharashtra            0.00%
  Nagaland               0.00%
  Rajasthan              0.00%
  Uttar Pradesh          0.00%

**Key Finding:**

Karnataka recorded the highest churn rate at 100%, followed by Meghalaya
at 66.67% and Telangana at 50%.

These geographic segments require further investigation to understand
possible regional differences in customer experience and subscription
behavior. State-level customer counts should be considered when
interpreting these rates, particularly where the sample size is small.

### D. Revenue Impact Analysis

Calculated the proportion of total monthly subscription charges
attributable to churned customers.

**Monthly Charges Attributable to Churned Customers: 18.68% of Total
Monthly Charges**

Formula:

\[ `\text{Percentage}`{=tex} =
`\frac{\text{Monthly Charges of Churned Customers}}`{=tex}
{`\text{Total Monthly Charges}`{=tex}} `\times 100`{=tex} \]

The results indicate that customers who churned accounted for 18.68% of
the total monthly subscription charges in the analyzed dataset.

### E. Customer Support Analysis

  Metric                               Result
  ---------------------------------- --------
  Average Complaints                     0.43
  Escalation vs. Churn Correlation       0.77

**Key Finding:**

A positive correlation of 0.77 was observed between support escalations
and customer churn.

This suggests a strong positive association between support escalations
and churn within the analyzed dataset, highlighting the importance of
investigating customer support experiences.

Correlation does not establish causation.

### F. Customer Lifetime Value

The subscription dataset contained a CLTV field, which was used to
calculate the average customer lifetime value.

**Average CLTV: 1,175.07**

CLTV was considered an important business metric for understanding
customer value and supporting retention prioritization.

## 7. Business Recommendations

Based on the analytical findings, the following retention strategies
were identified:

1.  **Basic Plan Retention:** Investigate the reasons behind the high
    churn rate among Basic plan subscribers and evaluate targeted
    retention offers.
2.  **Geographic Investigation:** Investigate customer experience and
    service-related issues in Karnataka, Meghalaya, and Telangana.
3.  **Proactive Customer Support:** Monitor support escalations and
    prioritize unresolved complaints to improve customer experience.
4.  **Risk-Based Retention:** Prioritize high-risk customers for
    retention campaigns, considering their customer value.
5.  **Customer Value Optimization:** Use CLTV to help allocate retention
    resources toward customers with greater long-term business value.

## 8. Conclusion

This project demonstrates an end-to-end customer churn analysis workflow
integrating SQL and Python.

The analysis identified a 28.57% churn rate, an 18.68% share of total
monthly charges attributable to churned customers, and significant churn
variations across subscription plans and geographic segments.

The findings provide a foundation for developing targeted retention
strategies, improving customer support processes, and making data-driven
customer retention decisions.

## 9. Skills Demonstrated

-   SQL Data Extraction
-   Relational Data Integration
-   Python Data Analysis
-   Pandas Data Manipulation
-   Exploratory Data Analysis (EDA)
-   Customer Segmentation
-   Churn Rate Analysis
-   Revenue Impact Analysis
-   Customer Lifetime Value (CLTV)
-   Correlation Analysis
-   Business Intelligence
-   Data-Driven Decision Making

------------------------------------------------------------------------

**Dataset note:** This project uses a small sample dataset of 21
customer records. Findings are exploratory and should be validated
against a larger dataset before making operational business decisions.
