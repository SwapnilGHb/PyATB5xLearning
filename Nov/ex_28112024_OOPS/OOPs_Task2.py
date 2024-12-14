# Create a Class Name API - RestfulBooker
# Name, list_of_api, links{}
# print_apis, print_set()

class RestfulBooker():
    name = None
    list_of_api = []
    se_of_links = {}

    def __init__(self, name, list_of_api, set_of_links):
        self.name = name
        self.list_of_api = list_of_api
        self.set_of_links = set_of_links

    def api_list(self):
        print(f"List of APIs is {self.list_of_api}")

    def links_set(self):
        print(f"Set of Links is {self.set_of_links}")

print_api_links = RestfulBooker("API1", ['Intellexer', 'API2Cart', 'Delion.lo'], {"www.astrology.com", "www.animation.com","www.avator.com"})
print_api_links.api_list()
print_api_links.links_set()


