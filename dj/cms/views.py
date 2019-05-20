from django.shortcuts import render,HttpResponse
# Create your views here.f
from cms import models
from django.core.serializers import serialize
import json
from django.core.paginator import Paginator



def lists(request):
    page = request.GET.get('page',None)
    print('page:',page)
    obj = models.Test.objects.all().order_by()
    paginator = Paginator(obj,2)
    if int(page) > paginator.num_pages:
        return HttpResponse('400')
    obj = paginator.page(page)
    json_data = serialize('json',obj)
    json_data = json.loads(json_data)

    return HttpResponse(json.dumps(json_data),content_type="application/json")

def detail(request,uid):
    print(uid)
    obj = models.Test.objects.filter(id=uid)
    json_data = serialize('json',obj)
    json_data = json.loads(json_data)

    return HttpResponse(json.dumps(json_data),content_type="application/json")