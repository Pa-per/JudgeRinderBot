"""import os to allow accessing files within the system."""
import logging
import os


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
