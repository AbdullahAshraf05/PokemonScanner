import tensorflow as tf
from tensorflow.keras import layers, models
import cv2
import numpy as np
import requests
from pokemontcgsdk import Card
from pokemontcgsdk import RestClient
from .key import API_KEY

RestClient.configure(API_KEY)

def process_image(image_url):

    url = f'https://api.pokemontcg.io/v2/cards'
    params = {
        'q': f'name:{card_name}',
        "page": 1,
        "pageSize": 10
    }
    headers = {
        'X-Api-Key': 
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f"Found {data['count']} cards matching the query '{card_name}':\n")
        for card in data['data']:
            card_name = card.get('name', 'Unknown')
            hp = card.get('hp', 'N/A')
            rarity = card.get('rarity', 'N/A')
            image_url = card['images'].get('small', 'No image available')

            print(f"Card Name: {card_name}")
            print(f"HP: {hp}")
            print(f"Rarity: {rarity}")
            print(f"Image URL: {image_url}")
            print()
    else:
         print(f"Error: {response.status_code}, Unable to retrieve data.")

card_name = "hydreigon"
get_card(card_name)

data = pd.read_csv('pokemon-tcg-data-master 1999-2023.csv')
print(data.head())