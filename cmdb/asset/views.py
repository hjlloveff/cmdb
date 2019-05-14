#encoding: utf-8

from datetime import timedelta
import time
from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from asset import models
import os,uuid
from django.utils import timezone
from .models import hostaccessinfo
import xlrd,xlwt,csv
def index(request):
    if not request.session.get('user'):
        return redirect('user:login')
    return render(request, 'asset/index.html')


def hostinfo(requests):
    all_hostinfo = models.hostinfo.objects.all()
    return render(requests, '/opt/cmdb/templates/index/hostinfo.html',{"all_hostinfo":all_hostinfo})


def detail(request, nid):
    obj = models.hostinfo.objects.filter(id=nid).first()
    # 鍘诲崟鎸戞暟鎹紝濡傛灉涓嶅瓨鍦紝鐩存帴鎶ラ敊
    # models.UserInfo.objects.get(id=nid)
    return render(request, '/opt/cmdb/templates/index/user_detail.html', {'obj': obj})

def alihost(requests):
    all_hostinfo = models.hostinfo.objects.all()
    return render(requests, '/opt/cmdb/templates/index/alihostinfo.html',{"all_hostinfo":all_hostinfo})

def edit(request, nid):
    if request.method == "GET":
       obj = models.hostinfo.objects.filter(id=nid).first()
    # 鍘诲崟鎸戞暟鎹紝濡傛灉涓嶅瓨鍦紝鐩存帴鎶ラ敊
    # models.UserInfo.objects.get(id=nid)
       return render(request, '/opt/cmdb/templates/index/edit.html', {'obj': obj})
    elif request.method == "POST":
       h = request.POST.get('username')
       n = request.POST.get('passsword')
       models.hostinfo.objects.filter(id=nid).update(hostname=h,name=n)
       return redirect('/asset/alihost/')


def jifang(requests):
     all_jifang = models.hostaccessinfo.objects.all()
     return render(requests,'/opt/cmdb/templates/index/jifang.html',{"all_jifang": all_jifang })


def jifangedit(request,nid):
    if request.method == "GET":
       obj = models.hostaccessinfo.objects.filter(id=nid).first()
       return render(request, '/opt/cmdb/templates/index/jifangedit.html', {'obj': obj})
    elif request.method == "POST":
       h = request.POST.get('feiyong')
       models.hostaccessinfo.objects.filter(id=nid).update(feiyong=h)
       return redirect('/asset/jifang/')


def upload(request):
     date= {}
     csv_file = request.FILES["csv_file"]
     file_data = csv_file.read().decode("utf-8")
     lines = file_data.split("\n")
        # loop over the lines and save them in db. If error , store as string and then display
     for line in lines:
          fields = line.split(",")
          data_dict = {}
          print (type(fields))
     return redirect('/asset/jifang/')






