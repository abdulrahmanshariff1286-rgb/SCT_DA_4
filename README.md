# Marketing Campaign EDA & ROI Optimization Strategy 📊

**Author:** Abdul Rahman 
**Task:** SkillCraft Technology Task 04 - Business Insights Report (EDA)

## 📌 Project Overview
The objective of this project is to perform Exploratory Data Analysis (EDA) on a marketing campaign dataset. Instead of building predictive machine learning models, this analysis focuses on the "Why" behind channel performance by cleaning the data, visualizing the user conversion funnel, and delivering an actionable business summary based on Return on Investment (ROI).

## 🚀 Executive Summary
Our exploratory data analysis reveals that Email Marketing (2236% ROI) and Social Ads (1958% ROI) significantly outperform other channels.  Conversely, the Affiliate channel (657% ROI) drives high traffic volume but fails to convert .We recommend immediately reallocating 30-40% of the Affiliate and Search Engine budgets into Email and Social Ads to maximize net revenue.

## 📉 Funnel Insights & Channel Breakdown
By analyzing the customer journey from Impression to Conversion, we isolated why certain channels succeed or fail:

* **Email Marketing (The Top Performer):** Offers the best balance with a strong CTR (3.14%), robust Conversion Rate (12.59%), and the highest ROI.Re-engaging warm     leads remains our most cost-effective strategy.
* **Social Ads (High Efficiency):** Despite having the lowest overall CTR (2.91%), precise targeting yields the highest Conversion Rate (13.60%). We are getting        fewer clicks, but the audience has extremely high buyer intent.
* **Search Engine (Engagement Lag):** Yields a moderate ROI (732%) but the lowest CTR (2.84%). This indicates our ad copy or keyword targeting is losing attention      to competitors on the results page.
* **Affiliate Network (The Volume Trap):** Generated the highest raw click volume (436,047) and CTR (3.26%), but suffers from the worst Conversion Rate (11.77%).       We are paying for high-volume, low-quality traffic that drops off at the landing page.

## 💡 Strategic Recommendations
* **Reallocate Budget:** Shift 30-40% of the current Affiliate and Search Engine marketing spend directly into Email Marketing and Social Ads.
* **Scale Email Capture:** Prioritize top-of-funnel lead magnets (e.g., newsletter sign-ups) to capture more emails, continuously feeding our most profitable pipeline.
* **Audit Affiliate Traffic:** Pause any planned budget increases for the Affiliate network. Conduct a strict audit of partner traffic to fix the drastic drop-off between clicks and conversions.
* **Optimize Search Ads:** Conduct A/B testing on Search Engine ad copy and refine keyword bidding to target higher-intent searches before allocating further budget.

## 🛠️ Technical Execution & Tech Stack
The data was processed and analyzed using **Python** to ensure accuracy and repeatability.
* **Libraries Used:** `pandas`, `numpy`, `matplotlib`, `seaborn`.
* **Data Cleaning:** Handled missing revenue data utilizing median imputation grouped by channel to prevent extreme outliers from skewing the averages. Removed duplicate campaign logs to ensure accurate spend and revenue metrics.
* **Feature Engineering:** Calculated critical business metrics from raw counts, including CTR (%), Conversion Rate (%), and ROI (%).

## 📂 Repository Structure
* `Task_4_.py`: Python script containing the data simulation, cleaning, aggregation, and visualization logic.
* `raw_marketing_data.csv`: The initial raw dataset with uncleaned values.
* `cleaned_marketing_data.csv`: The processed dataset ready for EDA.
* `Marketing Campaign EDA.pdf`: The official 1-page business insights report highlighting ROI recommendations.
* `Bar_Chart_ROI_Task_4.png`: Exported visualization of ROI by marketing channel.


** Note - This task was asssigned by Skillcraft Technology.
