from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import User, Scenario


class ScenarioList(APIView):
    def get(self, request):
        try:
            response = Scenario.objects.filter(deleted=False).order_by('-createdAt')
            list = [
                {
                    'id': r.id,
                    'title': r.title,
                }
                for r in response
            ]
            return Response(list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ScenarioDetail(APIView):
    def get(self, request, id):
        try:
            try:
                response = Scenario.objects.get(id=id)
            except:
                error_msg = "そんなidの日報はないよ！"
                return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
            res = {
                'id': response.id,
                'title': response.title
            }
            return Response(res)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class CategoryDairy(APIView):
#     def get(self, request, cat):
#         try:
#             daily = Daily.objects.filter(isOpen=True).values_list(
#                 'date', cat).order_by('-date')

#             res_list = [
#                 {
#                     'date': d[0],
#                     'content': d[1],
#                 }
#                 for d in daily
#             ]

#             return Response(res_list) 
#         except:
#             return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)