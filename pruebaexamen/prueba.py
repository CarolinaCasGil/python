# import requests

# API = "eC4iRt6Lqa2Y4-PoR62q"

# def getcaracters():
#     url ="https://the-one-api.dev/v2/character"
#     headers = {"Authorization" : f"Bearer {API}"}
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     print(data)
    
# # getcaracters()


# def get_characters_by_race_and_gender(race, gender):
#     url = "https://the-one-api.dev/v2/character"
#     headers = {"Authorization": f"Bearer {API}"}
#     params = {"race": race, "gender": gender}
    
#     response = requests.get(url, headers=headers, params=params)
#     data = response.json()

#     characters = data.get("docs", [])
#     for character in characters:
#         name = character.get("name", "Unknown")
#         race = character.get("race", "Unknown")
#         gender = character.get("gender", "Unknown")
#         print(f"Name: {name}, Race: {race}, Gender: {gender}")
    

# #get_characters_by_race_and_gender("Human", "Male")



# def get_characters_by_race(race):
#     url = "https://the-one-api.dev/v2/character"
#     headers = {"Authorization": f"Bearer {API}"}
#     raza = {"race": race}
    
#     response = requests.get(url, headers=headers, params=raza)
#     data = response.json()

#     characters = data.get("docs", [])
#     for character in characters:
#         print(f"Name: {character.get('name')}, Race: {character.get('race')}")
        
        
# get_characters_by_race("Elf")


import requests

API_KEY = "eC4iRt6Lqa2Y4-PoR62q"
API_ENDPOINT = "https://the-one-api.dev/v2/character"

def get_characters():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(API_ENDPOINT, headers=headers)

    if response.status_code == 200:
        data = response.json()
        characters = [
            {
                'name': item['name'],
                'race': item['race'],
            } if 'gender' not in item else {
                'name': item['name'],
                'race': item['race'],
                'gender': item['gender']
            } for item in data['docs']
        ]
        return characters
    else:
        print(f"Error: {response.status_code}")
        return None


def display_character_info(characters):
    for character in characters:
        print(f"Name: {character['name']}, Race: {character['race']}, Gender: {character['gender']}")

characters = get_characters()
if characters is not None:
    display_character_info(characters)