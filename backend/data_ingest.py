import requests

def fetch_nasa_data(api_url: str, params: dict) -> dict:
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()
