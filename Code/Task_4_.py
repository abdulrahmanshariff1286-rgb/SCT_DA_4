#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 1. GENERATE RAW DATASET (raw_marketing_data.csv)
# ---------------------------------------------------------
np.random.seed(42) # Keeps the random data consistent every time you run it
channels = ['Social Ads', 'Search Engine', 'Email Marketing', 'Affiliate']
n_rows = 200

# Create the base columns
data = {
    'Campaign_ID': [f'CMP_{i:03d}' for i in range(1, n_rows + 1)],
    'Channel': np.random.choice(channels, n_rows),
    'Spend': np.random.uniform(500, 5000, n_rows).round(2),
    'Impressions': np.random.randint(10000, 500000, n_rows),
}
df = pd.DataFrame(data)

# Simulate the marketing funnel (Impressions -> Clicks -> Conversions)
df['Clicks'] = (df['Impressions'] * np.random.uniform(0.01, 0.05, n_rows)).astype(int)
df['Conversions'] = (df['Clicks'] * np.random.uniform(0.05, 0.20, n_rows)).astype(int)

# Simulate Revenue based on the channel to create clear ROI differences
channel_multipliers = {'Social Ads': 4.5, 'Search Engine': 1.5, 'Email Marketing': 3.5, 'Affiliate': 1.2}
df['Revenue'] = df.apply(
    lambda row: row['Conversions'] * np.random.uniform(20, 50) * (channel_multipliers[row['Channel']]/2), 
    axis=1
).round(2)

# Introduce some intentional "dirty" data so you have something to clean in your EDA
df.loc[10:15, 'Revenue'] = np.nan # Add missing values
df = pd.concat([df, df.iloc[0:5]]) # Add duplicate rows

# Save the raw data
raw_csv_path = 'raw_marketing_data.csv'
df.to_csv(raw_csv_path, index=False)
print(f"Successfully created: {raw_csv_path}")

# ---------------------------------------------------------
# 2. CLEAN THE DATASET (cleaned_marketing_data.csv)
# ---------------------------------------------------------
# Create a copy to clean
df_clean = df.copy()

# Step A: Remove duplicates
df_clean = df_clean.drop_duplicates()

# Step B: Handle missing revenue data by filling it with the median of that specific channel
df_clean['Revenue'] = df_clean['Revenue'].fillna(
    df_clean.groupby('Channel')['Revenue'].transform('median')
)

# Save the cleaned data
clean_csv_path = 'cleaned_marketing_data.csv'
df_clean.to_csv(clean_csv_path, index=False)
print(f"Successfully created: {clean_csv_path}")


# In[3]:


# Import necessary libraries
import pandas as pd             # Used for data manipulation and creating DataFrames (tables)
import matplotlib.pyplot as plt # The core plotting library in Python
import seaborn as sns           # Built on top of matplotlib, makes charts look much more professional with less code

# Load the raw dataset we generated earlier
# We use pd.read_csv because our data is stored in a Comma Separated Values file.
df = pd.read_csv('raw_marketing_data.csv')

# Display the first 5 rows to ensure it loaded correctly
df.head()


# In[4]:


# 1. Remove Duplicates
# WHY: If ad platforms accidentally log a campaign twice, our spend and revenue metrics will be inflated.
df_clean = df.drop_duplicates().copy()

# 2. Handle Missing Revenue Data
# WHY: Sometimes revenue tracking breaks. If we drop the rows with missing revenue entirely, 
# we lose valuable data about Impressions and Clicks for those campaigns. 
# Instead, we "impute" (fill in) the missing data. 
# WHY MEDIAN?: We use the median (middle value) of that specific channel instead of the mean (average). 
# The median is resistant to extreme outliers (like one massive $50,000 sale skewing the average).
df_clean['Revenue'] = df_clean['Revenue'].fillna(
    df_clean.groupby('Channel')['Revenue'].transform('median')
)

print("Data cleaning complete. Missing values and duplicates handled.")


# In[5]:


# Group the data by Marketing Channel and sum up all the numerical metrics
# WHY: Budget decisions are made at the channel level (e.g., "Give more money to Facebook"), not the campaign level.
agg_df = df_clean.groupby('Channel').agg({
    'Spend': 'sum',
    'Impressions': 'sum',
    'Clicks': 'sum',
    'Conversions': 'sum',
    'Revenue': 'sum'
}).reset_index()

# Calculate Funnel Metrics (The "Why")
# WHY CTR: Click-Through Rate tells us if the ad copy/image was actually engaging.
agg_df['CTR (%)'] = (agg_df['Clicks'] / agg_df['Impressions'] * 100).round(2)

# WHY Conv. Rate: Tells us if the landing page actually convinced them to buy after they clicked.
agg_df['Conv. Rate (%)'] = (agg_df['Conversions'] / agg_df['Clicks'] * 100).round(2)

# Calculate Business Profitability
# WHY ROI: Return on Investment is the ultimate metric. It doesn't matter if a channel gets a million clicks 
# if it costs more than the revenue it brings in. Formula: (Net Profit / Cost) * 100
agg_df['ROI (%)'] = ((agg_df['Revenue'] - agg_df['Spend']) / agg_df['Spend'] * 100).round(2)

# Sort the table by ROI so the best channel is at the top
agg_df = agg_df.sort_values('ROI (%)', ascending=False)

# Display the aggregated table
agg_df


# In[6]:


# Set the visual style to look professional
sns.set_theme(style="whitegrid")

# Create a figure (canvas)
plt.figure(figsize=(10, 6))

# Create a bar plot using Seaborn
# WHY Bar Plot: Bar charts are the absolute best way to compare categorical data (Channels) against a numerical value (ROI).
ax = sns.barplot(x='Channel', y='ROI (%)', data=agg_df, palette='viridis')

# Add titles and labels for clarity
plt.title('Return on Investment (ROI) by Marketing Channel', fontsize=16, fontweight='bold')
plt.xlabel('Marketing Channel', fontsize=12)
plt.ylabel('ROI (%)', fontsize=12)

# Add the exact percentage numbers on top of each bar so stakeholders don't have to guess
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}%', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points')

# Display the chart
plt.tight_layout()
plt.show()


# In[ ]:




