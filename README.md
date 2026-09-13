# ApexPlanet Data Analytics Internship — Task 1

## Task
Data Immersion & Wrangling

## Source dataset
ApexPlanet_DataAnalytics_Dataset.xlsx

## Dataset profile
- Rows: 1000
- Columns: 12
- Full-row duplicates: 0
- Missing Age values: 20
- Missing City values: 13
- Duplicate Order_ID rows: 9
- Invalid Order_Date values: 0

## Cleaning performed
1. Standardized date values to YYYY-MM-DD.
2. Filled missing Age values with the median age (41).
3. Filled missing City values with `Unknown`.
4. Stripped leading/trailing spaces from text fields.
5. Preserved duplicate Order_IDs in `Original_Order_ID` and assigned suffixes to repeated IDs so the cleaned transaction key is unique.
6. Converted numeric fields to numeric types.
7. Checked that Total_Sales agrees with Quantity × Unit_Price; no material mismatches were found.
8. Outliers were flagged in the quality report rather than automatically deleted because a high sales value can be a valid business transaction.

## Deliverables
- ApexPlanet_Task1_Cleaned_Dataset.xlsx
- ApexPlanet_Task1_Data_Dictionary.xlsx
- ApexPlanet_Task1_Quality_Report.xlsx
- cleaning_script.py
