# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import Http404

from .serializers import CampaignSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Campaign
import datetime


class UserList(APIView):
    """
List all campaign, or create a new campaign.
# """
    def get(self, request, format=None):

        users = Campaign.objects.all()
        serializer = CampaignSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_object(self, partner_id):
        try:
            return Campaign.objects.get(partner_id=partner_id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, partner_id, format=None):

        user = self.get_object(partner_id)
        user = CampaignSerializer(user)
        con_time = user.data["creation_time"]
        time_in_seconds = (int(con_time.split(':')[0]) * 3600) + (int(con_time.split(':')[1]) * 60) + float(
            con_time.split(':')[2])
        current_time = str(datetime.datetime.now().time())
        time_in_seconds1 = (int(current_time.split(':')[0]) * 3600) + (int(current_time.split(':')[1]) * 60) + float(
            current_time.split(':')[2])
        camp_duration = int(user.data["duration"])

        if (time_in_seconds1) < (time_in_seconds + camp_duration):
            return Response(user.data)
        else:

            return Response("""{"status":"Campaign is not Active"}""")