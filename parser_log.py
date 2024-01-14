import requests

# BOT_API = 
class Products:
    def get_all_post(self, url):
        data = requests.get(url + '/post/').json()
        return data

class Lostitems:
    def get_lost_items(self, url):
        data = requests.get(url + '/post/' + '?status=Lost').json()
        return data
    
# class Found_items:
#     def get_found_items(self, url):
#         data = requests.get(url + '/post/' + '?status=Found').json()
#         return data

