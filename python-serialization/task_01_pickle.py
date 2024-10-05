#!/usr/bin/python3
"""pickle module"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """initializing objects"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """displaying attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialization"""
        try:
            with open(filename, 'wb') as a:
                pickle.dump(self, a)
        except Exception as e:
            print(f"Error occured during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """deserialization"""
        try:
            with open(filename, 'rb') as a:
                return pickle.load(a)
        except Exception as e:
            print(f"Error occured during deserialization: {e}")
            return None
