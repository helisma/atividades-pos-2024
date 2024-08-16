import requests

api_url = "https://jsonplaceholder.typicode.com"

def list():
    return requests.get(api_url+"/users").json()

def read(user_id):
    response = requests.get(api_url+"/users"+user_id)
    if response.status_code == 200:
        return response.json()
    else:
        return False
    
def delete(user_id):
    response = requests.delete(api_url+"/users"+user_id)
    if response.status_code == 200:
        return True
    else:
        return False
    
def create(user_data):
    response = requests.post(api_url+"/users", json=user_data)
    if response.status_code == 201:
        return True
    else:
        return False
    
def update(user_id, user_data):
    response = requests.patch(api_url+"/users/"+user_id, json=user_data)
    if response.status_code == 200:
        return True
    else:
        return False