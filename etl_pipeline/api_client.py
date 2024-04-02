import requests

base_url = "https://jsonplaceholder.typicode.com"

def fetch_posts():
    """
    Fetches posts data from the JSONPlaceholder API.

    Returns:
        list: A list of dictionaries representing posts data.
    """
    response = requests.get(f"{base_url}/posts")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching posts:", response.status_code)
        return None

def fetch_users():
    """
    Fetches users data from the JSONPlaceholder API.

    Returns:
        list: A list of dictionaries representing users data.
    """
    response = requests.get(f"{base_url}/users")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching users:", response.status_code)
        return None

