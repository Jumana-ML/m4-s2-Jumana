# Comparative Analysis: Diverse Analytical Perspectives

## 1. My KPI (Jumana)
**KPI:** Average Order Value (AOV) per Product Category.
**Why:** I chose this KPI from my "Amman Digital Market" project because it identifies the most "lucrative" segments of the market. Understanding which categories drive higher transaction values is essential for any business-oriented data engineering task. I used a horizontal bar chart to allow for clear category comparisons and precise value labeling.

## 2. My Partner's KPI and Selection
**KPI:** Distribution of Weekly Study Hours.
**Why:** My partner independently chose this KPI from a completely different project focused on "Student Performance." Their goal was behavioral—to understand the distribution and frequency of student efforts. They utilized a Histogram with a KDE overlay to visualize the density of study habits across a student population.

## 3. Where We Agreed
Despite working on **completely different datasets and domains** (Retail vs. Education), we agreed on the importance of **Statistical Distribution**. Both of us realized that looking at "totals" isn't enough; we needed to see the "average" (in my case) and the "distribution" (in theirs) to provide actionable insights. We also both prioritized "Publication Quality" by removing chart junk and using professional color palettes (Viridis and Blue-KDE).

## 4. Where We Disagreed (Diverse Focus)
- **Domain Intent:** My analysis was strictly **Commercial/Financial**, focused on revenue-per-order. My partner’s analysis was **Academic/Sociological**, focused on student behavior.
- **Aggregation Methods:** My project required complex data processing to group items by `order_id` and identify the dominant category. My partner’s project focused on the frequency distribution of a single continuous variable (`study_hours_weekly`).
- **Visual Interpretation:** I used ranking as my primary visual cue (sorting from highest to lowest AOV), whereas my partner used central tendency (Mean vs. Median) to show the "Normal Distribution" of the data.

## 5. What We Learned
Comparing these two separate projects taught us that **Data Science is highly contextual**. The same toolset (Python, Seaborn, Pandas) can be used to solve a business problem in one hour and a social/academic problem in the next. Seeing my partner's distribution chart made me realize I could apply similar "Distribution Analysis" to my market data to see if the high AOV in Books is a "Normal" trend or driven by a few extreme outliers.