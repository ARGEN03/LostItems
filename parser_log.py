import requests

# BOT_API = 
class Products:
    def get_all_post(self ,url):
        data = requests.get(url+'/post/').json()
        return data

    
class Login:
    def login(self, url , email , password):
        data = {
            'email': email,
            'password': password
        }

        response = requests.post(url+'/account/login/', data=data)
        if response.status_code == 200:
            return response.json().get('access')
        else:
            return 'Неверный логин или пароль'