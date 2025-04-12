import json

file_path: str = '/Users/anurag/Desktop/python-idently-learning/_18_file_handling/data.json'

# load is used to read a json file format and convert it to a python dictionary
with open(file_path, 'r') as file:
    data: dict = json.load(file)
    print(data)

# loads is used to read a json string and convert it to a python dictionary
my_json: str = """
{
  "name": "Super Mario",
  "age" : 33,
  "friends": ["Luigi", "Toad"],
  "other_info": null
}
"""
data: dict = json.loads(my_json)
print(data)

data: dict = {'name': 'Super Mario', 'age': 33, 'friends': ['Luigi', 'Toad'], 'other_info': None}
# dump is used to convert a python dictionary to a json file format
with open('new_data.json', 'w') as f:
    json.dump(data, f)

# dumps is used to convert a python dictionary to a json string
with open(file_path, 'w') as file:
    json_string: str = json.dumps(data)
    print(json_string)
