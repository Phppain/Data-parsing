"""task1.py"""

import os
import json
import requests

def download_and_save_with_requests(url, output_folder):
    response = requests.get(url)
    todos = response.json()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, todo in enumerate(todos):
        file_path = os.path.join(output_folder, f'todo_{i}.json')
        with open(file_path, 'w') as f:
            json.dump(todo, f, indent=4)

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos/'
    output_folder = 'todos_requests'
    download_and_save_with_requests(url, output_folder)
