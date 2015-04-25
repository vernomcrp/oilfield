from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from moneyflow.models import MoneyFlowRecord
from moneyflow.serializers import MoneyFlowSerializer
from rest_framework import viewsets

class MoneyFlowViewSet(viewsets.ModelViewSet):
    queryset = MoneyFlowRecord.objects.all()
    serializer_class = MoneyFlowSerializer
    


# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
# @csrf_exempt
# def moneyflowrecord_list(request):
#     if request.method == 'GET':
#         records = MoneyFlowRecord.objects.all()
#         mfs = MoneyFlowSerializer(records, many=True)
#         return JSONResponse(mfs.data)
#
#     elif request.method == 'POST':
#         print request.POST
#         data = JSONParser().parse(request)
#         mfs = MoneyFlowSerializer(data=data)
#         if mfs.is_valid():
#             mfs.save()
#             return JSONResponse(mfs.data, status=201)
#         return JSONResponse(mfs.errors, status=400)
#
# @csrf_exempt
# def moneyflowrecord_detail(request, pk):
#     try:
#         record = MoneyFlowRecord.objects.get(pk=pk)
#     except MoneyFlowRecord.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         mfs = MoneyFlowSerializer(record)
#         return JSONResponse(mfs.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         mfs = MoneyFlowSerializer(record, data=data)
#         if mfs.is_valid():
#             mfs.save()
#             return JSONResponse(mfs.data)
#         return JSONResponse(mfs.errors, status=400)
#
#     elif request.method == 'DELETE':
#         record.delete()
#         return HttpResponse(status=204)
