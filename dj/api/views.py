from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from api import models
from plugin.LoginValidate import session
from django.contrib.auth import authenticate

# from django.contrib.sessions import models
# Create your views here.
import json


@csrf_exempt
def index(request):
    if request.method == 'GET':
        obj = models.Test.objects.all()
        from django.core import serializers
        json_data = serializers.serialize('json',obj)
        json_data = json.loads(json_data)
        return HttpResponse(json.dumps(json_data),content_type="application/json")


@csrf_exempt
def login(request):
    response = HttpResponse()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(username=username,password=password)
        if not user:
            data = json.dumps({'status':400})
            response.write(data)
            return response
        sessionid = session(username).session_key

        response.set_cookie('sessionid', sessionid, 600000)
        data = json.dumps({'status': '200', 'sessionid': sessionid})
        response.write(data)
        return response

    return HttpResponse('400')

@csrf_exempt
def change(request,uid):
    if request.method == 'GET':
        obj = models.Test.objects.filter(id=uid)
        print(uid)
        from django.core import serializers
        json_data = serializers.serialize('json',obj)
        json_data = json.loads(json_data)
        return HttpResponse(json.dumps(json_data),content_type="application/json")
    if request.method == 'POST':
        obj = models.Test.objects.filter(id=uid)
        updata_dict = {}
        for key,val in request.POST.items():
            if not val:continue
            if key in ('id','model','date') :continue
            updata_dict[key] = val
        obj.update(**updata_dict)
        return HttpResponse('200')
