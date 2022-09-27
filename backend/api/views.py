import json
from django.http import JsonResponse


def home(request):
    data = dict()
    try:
        body = request.body
        data = json.loads(body)  # string of json data -> python dictionary
    except:
        pass

    print(data)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
