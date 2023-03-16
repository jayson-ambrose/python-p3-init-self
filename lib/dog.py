#!/usr/bin/env python3
import ipdb

class Dog:
    
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed
    
    def bark (self):
        print('Woof!')
    
    def get_adopted (self, owner_name):
        self.owner = owner_name

    pass

chewy = Dog("Fido")