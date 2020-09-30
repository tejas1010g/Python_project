# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models


class Campaign(models.Model):

    partner_id=models.CharField(max_length=100,primary_key=True,null=False)
    duration=models.IntegerField()
    ad_content=models.TextField(max_length=1000)
    creation_time=models.TimeField(default=datetime.datetime.now().time())


    def __str__(self):
        return self.ad_content,self.partner_id