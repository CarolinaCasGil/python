import requests

url = "https://fakestoreapi.com/docs"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    # Assuming the categories are available in the response JSON
    categories = response.json()

    print("Available Categories:")
    for category in categories:
        print(category)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
