import requests
import os
from dotenv  import load_dotenv

load_dotenv()
def build_request(keyword, country, results_per_page, page):
    """Builds the request URL and query parameters for the Adzuna API.

    Args:
        keyword (str): The keyword to search for in job titles or descriptions.
        country (str): The 2-letter country code (e.g., 'in').
        results_per_page (int): The number of job results to return per page.
        page (int): The page number of the search results to fetch.

    Returns:
        tuple: A tuple containing:
            - base_url (str): The constructed API endpoint URL.
            - query_params (dict): A dictionary of query parameters including API credentials.
    """
    base_url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"
    query_params = {
        "app_id" : os.getenv("APP_ID"),
        "app_key" : os.getenv("APP_KEY"),
        "what" : keyword,
        "results_per_page" : results_per_page
    }

    return base_url, query_params

def send_request(base_url, query_params):
    """Sends a GET request to the Adzuna API.

    Args:
        base_url (str): The API endpoint URL.
        query_params (dict): The query parameters for the API request.

    Returns:
        requests.Response: The API response object.
    """
    response = requests.get(url=base_url, params=query_params, timeout=10)
    response.raise_for_status()  
    return response

def validate_response(response):
    """Validates the API response structure and content.

    Args:
        response (requests.Response): The API response object to validate.

    Returns:
        list: A list of job results from the API response.

    Raises:
        Exception: If the API returned an error or if the 'results' field is missing.
    """
    data = response.json()

    if "error" in data:
        raise Exception(f"API Error: {data['error']}")

    if "results" not in data:
        raise Exception("Invalid API response: results field missing")

    return data["results"]

def fetch_jobs(keyword, country, results_per_page, page):
    """Fetches and validates job postings from the Adzuna API.

    Args:
        keyword (str): The search term/keyword for jobs.
        country (str): The 2-letter country code.
        results_per_page (int): The number of job results to return per page.
        page (int): The page number of search results to fetch.

    Returns:
        list: A list of validated job dictionaries.
    """
    base_url, query_params = build_request(keyword, country, results_per_page, page)
    response = send_request(base_url, query_params)
    return validate_response(response)
