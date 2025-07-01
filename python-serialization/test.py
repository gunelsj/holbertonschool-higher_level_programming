#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Məlumat
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# JSON-a yaz
serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

# JSON-dan oxu
deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)
