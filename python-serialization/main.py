#!/usr/bin/env python3
from task_01_pickle import CustomObject

obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

obj.serialize("object.pkl")

new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()
