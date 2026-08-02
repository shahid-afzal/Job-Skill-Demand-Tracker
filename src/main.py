"""
Main driver script for the Job Skill Demand Tracker application.
This script orchestrates the fetching of job data from the Adzuna API, database insertion,
skill extraction, metrics generation, and exporting of reports.
"""

from fetcher import fetch_jobs
from database import connect_database, create_jobs_table ,insert_jobs, get_all_jobs, insert_job_skills,create_job_skills_table
from skill_extractor import extract_skills
from analysis import get_top_skills, count_jobs, count_unique_skills, get_jobs_by_skill,get_top_companies, export_to_csv
from datetime import datetime

# Connect to the SQLite database and initialize required tables
connection = connect_database()
create_jobs_table(connection)
create_job_skills_table(connection)

try:
    # Fetch job listings matching search parameters
    jobs = fetch_jobs(
    keyword="python",
    country="in",
    results_per_page=10,
    page=1
    )
except Exception as e:
    print(e)


# Bulk insert fetched job postings into the database
insert_jobs(connection, jobs)

# Extract and store skill keywords found in each job posting's description
for job in jobs:
    description = job["description"]
    skills = extract_skills(description)
    insert_job_skills(connection, job["id"], skills, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Retrieve all jobs from the database (for inspection/verification)
all_jobs = get_all_jobs(connection)

# print(get_top_skills(connection))
# print(count_jobs(connection))
# print(count_unique_skills(connection))
# print(get_jobs_by_skill(connection, "python"))
# print(get_top_companies(connection))

# Analyze data and write reports
top_skills = get_top_skills(connection)
top_companies = get_top_companies(connection)
export_to_csv(top_skills, "top_skills.csv", ["skill", "job_count"])
export_to_csv(top_companies, "top_companies.csv", ["company", "job_count"])

# Close connection to release resource locks
connection.close()
