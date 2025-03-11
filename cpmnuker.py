import requests
from time import sleep

BASE_URL: str = "https://cpmnuker.anasov.ly/v2/api"

class CPMNuker:

    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
    
    def get_key_data(self) -> any:
        params = { "key": self.access_key }
        response = requests.get(f"{BASE_URL}/get_key_data", params=params)
        response.encoding = 'utf-8'
        response_decoded = response.json()
        return response_decoded

    def login(self, email, password) -> int:
        payload = { "account_email": email.encode('utf-8'), "account_password": password.encode('utf-8') }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/account_login", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return -1
        
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password) -> int:
        payload = { "account_email": email.encode('utf-8'), "account_password": password.encode('utf-8') }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/account_register", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return -1
        
        return response_decoded.get("error")
    
    def delete(self):
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            requests.post(f"{BASE_URL}/account_delete", params=params, data=payload)
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
    
    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/get_data", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return None
        return response_decoded
    
    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/set_rank", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")
    
    def set_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/set_money", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")
    
    def set_player_id(self, id) -> bool:
        payload = { "account_auth": self.auth_token, "id": id }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/set_id", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")

    def set_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name.encode('utf-8') }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/set_name", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")
    
    def delete_player_friends(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/delete_friends", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")
    
    def maximize_drag_wins(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/maximize_drag_wins", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")

    def complete_missions(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/complete_missions", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")

    def unlock_apartments(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/unlock_apartments", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")

    def unlock_slots(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/unlock_slots", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")
    
    def unlock_brakes(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/unlock_brakes", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")
    
    def unlock_wheels(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/unlock_wheels", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")

    def unlock_clothes(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/unlock_equipments", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")
    
    def unlock_cars(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        try:
            response = requests.post(f"{BASE_URL}/unlock_cars", params=params, data=payload)
            response.encoding = 'utf-8'
            response_decoded = response.json()
        except UnicodeEncodeError:
            print("Encoding error with UTF-8. Please check your input.")
            return False
        return response_decoded.get("ok")