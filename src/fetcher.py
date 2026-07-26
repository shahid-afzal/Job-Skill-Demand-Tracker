import requests
import os
from dotenv  import load_dotenv

load_dotenv()
def build_request(keyword, country, results_per_page, page):
    base_url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"
    query_params = {
        "app_id" : os.getenv("APP_ID"),
        "app_key" : os.getenv("APP_KEY"),
        "what" : keyword,
        "results_per_page" : results_per_page
    }

    return base_url, query_params

def send_request(base_url, query_params):
    response = requests.get(url=base_url, params=query_params, timeout=10)
    response.raise_for_status()  
    return response

def validate_response(response):
    data = response.json()

    if "error" in data:
        raise Exception(f"API Error: {data['error']}")

    if "results" not in data:
        raise Exception("Invalid API response: results field missing")

    return data["results"]

def fetch_jobs(keyword, country, results_per_page, page):
    base_url, query_params = build_request(keyword, country, results_per_page, page)
    response = send_request(base_url, query_params)
    return validate_response(response)