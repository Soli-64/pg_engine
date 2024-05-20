import json


def load_json(file_path: str):

    with open(file_path, 'r+') as file:
        content = ''
        for x in file.readlines():
            x.replace('\n', '')
            content += x
        print(content)
        return json.loads(content)
