import requests

class user_wrapper:
    api_url = "https://jsonplaceholder.typicode.com/users/"

    def list_user(self):
        response = requests.get(self.api_url)
        return response.json()

    def create_user(self, user_data):
        response = requests.post(self.api_url, json=user_data)
        return response.status_code

    def delete_user(self, id):
        response = requests.delete(self.api_url + f"{id}")
        return response.status_code

    def read_user(self, id):
        response = requests.get(self.api_url + f"{id}")
        return response.json()
    
    def update_user(self, id, user_data):
        user = self.api_url + f"{id}"
        response = requests.patch(user, json=user_data)
        return response.status_code