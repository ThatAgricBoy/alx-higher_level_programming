#!/usr/bin/python3

"""
    This function returns the the list 
    of available attributes and methods of an object
"""
def lookup(obj):
    # Get the object's class
    cls = obj.__class__
    
    # Get the object's instance dictionary
    instance_dict = obj.__dict__
    
    # Get the class dictionary
    class_dict = cls.__dict__
    
    # Combine the instance and class dictionaries
    attr_dict = {**class_dict, **instance_dict}
    
    # Filter out private and special attributes
    attrs = [attr for attr in attr_dict.keys() if not attr.startswith("__")]
    
    # Sort the attributes alphabetically
    attrs.sort()
    
    # Return the list of attributes
    return attrs
