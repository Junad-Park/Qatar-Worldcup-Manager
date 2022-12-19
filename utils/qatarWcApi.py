import requests

# Login
class QatarWcApi:
    def __init__(self):
        self.email = "qkrwnsgk1624@icloud.com"
        self.password = "1dpsrkdn"
        self.token = None
        self.latest_match = []
        
        self.login()
        self.getMatch()
    
    def register(self, name:str, email:str, password:str, password_confirm:str):
        headers = {
            'Content-Type': 'application/json',
        }

        json_data = {
            'name': name,
            'email': email,
            'password': password,
            'passwordConfirm': password_confirm,
        }

        response = requests.post('http://api.cup2022.ir/api/v1/user', headers=headers, json=json_data)

        register_status = response['status']
        register_token = response['data']['token']

        if register_status:
            return register_token
        else:
            return None

    def login(self):
        url = ' http://api.cup2022.ir/api/v1/user/login'

        headers = {
            'Content-Type': 'application/json',
        }
        json_data = {
            'email': self.email,
            'password': self.password,
        }
        response = requests.post(url, headers=headers, json=json_data)
        ret_dict = response.json()

        self.token = ret_dict['data']['token']

    def getMatch(self):
        match_headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json',
        }

        MAX_DAY = 23
        MAX_SIZE = 6
        while len(self.latest_match) < MAX_SIZE:
            response = requests.get(f'http://api.cup2022.ir/api/v1/bymatch/{MAX_DAY}' , headers=match_headers)
            ret_dict = response.json()
            for i in range(len(ret_dict['data'])):
                if len(self.latest_match) > MAX_SIZE:
                    return
                self.latest_match.append(ret_dict['data'][i])
            MAX_DAY -=1

    def getLatestMatch(self):
        return self.latest_match
