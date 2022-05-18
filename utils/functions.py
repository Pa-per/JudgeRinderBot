"""import os to allow accessing files within the system."""
import asyncio
import logging
import os
import pprint

import requests
from bs4 import BeautifulSoup


async def load_cogs(client):
    """
    Load all the cogs within the specified directory.

    Args:
        client: The client object.
    """
    for filename in os.listdir('commands'):
        if filename.endswith('.py'):
            file_name = filename[:-3]
            await client.load_extension(f'commands.{file_name}')
            logging.info(f'Loaded {file_name}')
    for event_name in os.listdir('events'):
        if event_name.endswith('.py'):
            event_file_name = event_name[:-3]
            await client.load_extension(f'events.{event_file_name}')
            logging.info(f'Loaded {event_file_name}')


async def heart_now_playing(client):
    """
    Get the current song playing.

    Args:
        client: The client object.
    """
    url = 'https://www.radio-uk.co.uk/heart-fm'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'referer': 'https://www.google.com/',
    }
    page = requests.get(url, headers=header, stream=True)
    await asyncio.sleep(3)
    soup = BeautifulSoup(page.text, 'html.parser')
    soup_2 = BeautifulSoup(page.content, 'html.parser')
    radio_image = soup.find(
        'div',
        {'id': 'player_table_container'},
    ).find(
        'div',
        {'id': 'player_image_container'},
    ).find(
        'img',
    )['src']

    radio_name = soup.find(
        'div',
        {'id': 'player_table_container'},
    ).find(
        'div',
        {'id': 'player_image_container'},
    ).find(
        'img',
    )['alt']

    song_img = soup_2.find(
        'div',
        {'id': 'player_table_container'},
    ).find(
        'div',
        {'id': 'song_history'},
    ).find(
        'div',
        {'class': 'latest-song'},
    ).find(
        'div',
        {'class': 'history-song'}
    )
    # ).find(
    #     'div',
    #     {'class': 'latest-song'},
    # ).find(
    #     'img',
    #     {'class': 'lazy'},
    # )['src']
    print(song_img)
    return radio_name, radio_image, song_img
