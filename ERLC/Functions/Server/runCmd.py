import httpx
import asyncio
import logging
from .requests import request

async def run_command(self, async_client,*, command: str):
    """Runs a ERLC server command as "Virtual Server Management"
                
    Parameters:
        None
                
    Returns:
        JSON Data
        """
    if command is None or not str:
        return logging.error("That is not a valid command.")
    headers = {"Server-Key": async_client.server_key}
    response = await request(headers=headers, endpoint="server/commandlogs", data={"command": command})

    if response:
        return response.json()
    else:
        return None