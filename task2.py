"""task2.py"""

import os
import json
import aiohttp
import aiofiles
import asyncio

async def download_and_save_with_aiohttp(url, output_folder):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            todos = await response.json()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    tasks = []
    for i, todo in enumerate(todos):
        file_path = os.path.join(output_folder, f'todo_{i}.json')
        tasks.append(save_json_file(file_path, todo))

    await asyncio.gather(*tasks)

async def save_json_file(file_path, data):
    async with aiofiles.open(file_path, 'w') as f:
        await f.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos/'
    output_folder = 'todos_aiohttp'
    asyncio.run(download_and_save_with_aiohttp(url, output_folder))
