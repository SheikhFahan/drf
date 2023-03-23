from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    #request -> http request in django
    data = {}
    body = request.body #byte string of json data
    try: 
        data = json.loads(body) #string of json data ->py dict
    except:
        pass
    
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = request.GET
    return JsonResponse(data)