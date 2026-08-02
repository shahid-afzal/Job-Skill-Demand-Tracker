"""
Visualization script for the Job Skill Demand Tracker application.
This script reads compiled CSV report files from the results directory and generates
horizontal bar charts representing the top skills and hiring companies.
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- Chart 1: Top Skills Demand Visualization ---

# Read and sort skills by frequency in descending order
df = pd.read_csv("results/top_skills.csv")
df_sorted = df.sort_values(by="job_count", ascending=False)

plt.figure(figsize=(10,6))

# Construct horizontal bar chart
plt.barh(
    df_sorted["skill"],
    df_sorted["job_count"]
)

# Set chart labels and titles
plt.title("Top Skills Demand")
plt.xlabel("Job Count")
plt.ylabel("Skills")

# Invert visual axis to place the highest frequency skill at the top of the chart
plt.gca().invert_yaxis()

plt.tight_layout()

# Export chart image to the results directory
plt.savefig("results/top_skills.png")

plt.close()


# --- Chart 2: Top Hiring Companies Visualization ---

# Read and sort companies by hiring demand in descending order
company_df = pd.read_csv("results/top_companies.csv")
company_df_sorted = company_df.sort_values(by="job_count", ascending=False)


plt.figure(figsize=(10,6))

# Construct horizontal bar chart for companies
plt.barh(
    company_df_sorted["company"],
    company_df_sorted["job_count"]
)

# Set chart labels and titles for companies
plt.title("Top Companies Demand")
plt.xlabel("Job Count")
plt.ylabel("Companies")

# Invert visual axis to place the company with most listings at the top
plt.gca().invert_yaxis()

plt.tight_layout()

# Export chart image to the results directory
plt.savefig("results/top_companies.png")

plt.close()




