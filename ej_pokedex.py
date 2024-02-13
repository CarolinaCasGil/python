import requests

# # Example: Fetch a list of products from a Fakestore API
# url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
# response = requests.get(url)


# if response.status_code == 200:
#     data = response.json()  # Parse JSON response
#     pokemon_list = [pokemon["name"] for pokemon in data["results"]] 

#     print(pokemon_list)
    
# else:
#     print(f"Error: {response.status_code}")

url = "https://pokeapi.co/api/v2/pokemon/132"
response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    print(data)
    
else:
    print(f"Error: {response.status_code}")