import json
my_dictionary = {
    "name": "Alexander Graham Bell",
    "job_title": "CEO",
    "company_name": "Bell System",
    "age": 75,
    "emails": [{"email": "alex@bell.com", "type": "work"}],
    "my_neighbor": False
}
print(my_dictionary)
unformatted_json = json.dumps(my_dictionary)
print(unformatted_json)
formated_json = json.dumps(my_dictionary, indent=4,
                           sort_keys=True, separators=(",", "="))
print(formated_json)
# convert json into a dictionary
dict1 = json.loads(unformatted_json)
# print all keys and their values
for key, value in dict1.items():
    print("key : ", key, "value : ", value)
