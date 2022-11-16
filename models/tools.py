import json
from fastapi import HTTPException, status

def read_data(file):
    with open(file, 'r+', encoding= 'utf-8') as f:
        return json.loads(f.read())

def overwrite_data(file, results):
    with open(file, 'w', encoding= 'utf-8') as f:
        f.seek(0)
        f.write(json.dumps(results)) 


def show_a_element(file, element_id, info): 
    results = read_data(file)
    id = str(element_id)    
    for data in results:    
        if data[f'{info}_id'] == id:
            return data    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"This {element_id} does'nt exist!"
        )

def delete_a_element(file, element_id, info):
    results = read_data(file)
    id = str(element_id)
    for data in results:
        if data[info] == id:
            results.remove(data)
            with open(file, 'w', encoding= 'utf-8') as f:
                f.seek(0)
                f.write(json.dumps(results)) 
            return data
        
        else:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"This {element_id} doesn't exist! "
                )
