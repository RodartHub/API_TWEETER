#Python

from typing import Dict
from uuid import UUID
from datetime import date, datetime

types = [UUID, date, datetime]

#This function convert each key in STR

def serialize(input: Dict):
    for key in input:
        val = input[key]
        # For nested objects
        if type(val) is dict:
            serialize(val)
            continue
        if type(val) in types:
            input[key] = str(val)
        
    return input