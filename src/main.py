from fetcher import fetch_jobs
from database import connect_database, create_jobs_table ,insert_jobs, get_all_jobs, insert_job_skills,create_job_skills_table
from skill_extractor import extract_skills
from analysis import get_top_skills, count_jobs, count_unique_skills, get_jobs_by_skill,get_top_companies, export_to_csv
from datetime import datetime

connection = connect_database()
create_jobs_table(connection)
create_job_skills_table(connection)

try:
    jobs = fetch_jobs(
    keyword="python",
    country="in",
    results_per_page=10,
    page=1
    )
except Exception as e:
    print(e)


insert_jobs(connection, jobs)

for job in jobs:
    description = job["description"]
    skills = extract_skills(description)
    insert_job_skills(connection, job["id"], skills, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

all_jobs = get_all_jobs(connection)

# print(get_top_skills(connection))
# print(count_jobs(connection))
# print(count_unique_skills(connection))
# print(get_jobs_by_skill(connection, "python"))
# print(get_top_companies(connection))

top_skills = get_top_skills(connection)
top_companies = get_top_companies(connection)
export_to_csv(top_skills, "top_skills.csv", ["skill", "job_count"])
export_to_csv(top_companies, "top_companies.csv", ["company", "job_count"])

connection.close()