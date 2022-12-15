import random
import json


class FiltraIPMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        print('request: ', response.content)

        data = {'valor': random.randrange(0, 100)}

        response.content = json.dumps(data)

        return response
