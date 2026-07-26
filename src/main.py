from fetcher import fetch_jobs
from database import connect_database, create_jobs_table ,insert_jobs, get_all_jobs

connection = connect_database()
create_table = create_jobs_table(connection)

jobs = fetch_jobs(
    keyword="python",
    country="gb",
    results_per_page=5,
    page=1
)

insert_jobs = insert_jobs(connection, jobs)

all_jobs = get_all_jobs(connection)
print(len(all_jobs))
print(all_jobs[0])
