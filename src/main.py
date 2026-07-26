from fetcher import fetch_jobs

print(fetch_jobs(
    keyword="python",
    country="gb",
    results_per_page=5,
    page=1
))