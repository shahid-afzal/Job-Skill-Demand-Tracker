import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/top_skills.csv")
df_sorted = df.sort_values(by="job_count", ascending=False)

plt.figure(figsize=(10,6))

plt.barh(
    df_sorted["skill"],
    df_sorted["job_count"]
)

plt.title("Top Skills Demand")
plt.xlabel("Job Count")
plt.ylabel("Skills")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig("results/top_skills.png")

plt.close()


company_df = pd.read_csv("results/top_companies.csv")
company_df_sorted = company_df.sort_values(by="job_count", ascending=False)


plt.figure(figsize=(10,6))

plt.barh(
    company_df_sorted["company"],
    company_df_sorted["job_count"]
)

plt.title("Top Companies Demand")
plt.xlabel("Job Count")
plt.ylabel("Companies")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig("results/top_companies.png")

plt.close()




