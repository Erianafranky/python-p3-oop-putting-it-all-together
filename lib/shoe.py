#!/usr/bin/env python3
"""
Shoe has the brand and size passed to __init__, and values can be set to new instance.
Shoe in shoe.py prints "size must be an integer" if size is not an integer.
Shoe in shoe.py says that the shoe has been repaired.
Shoe in shoe.py creates an attribute on the instance called 'condition' and set equal to 'New' after repair.
"""

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        
        else:
            print("size must be an integer")
    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    