# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import AddForm
from django.http import HttpResponse
from pprint import pprint

from .zabbixtools import ZabbixApi
import configparser, os
import json

########################################################################
#由配置文件引入所需变量值
########################################################################
proDir = os.path.dirname(os.path.realpath(__file__))
print(proDir)
configPath = os.path.join(proDir, "configs.txt")

cp = configparser.ConfigParser()
cp.read(configPath)

url=cp.get('zabbix1', 'zabbix_url')
user=cp.get('zabbix1', 'zabbix_user')
password=cp.get('zabbix1', 'zabbix_pass')
header=cp.get('zabbix1', 'zabbix_header')

#将str转为dict
header=json.loads(header)
# print(header)
# pprint(url, user)

# Create your views here.
# url = "http://xxxxx/zabbix/api_jsonrpc.php"
# header = {"Content-Type": "application/json"}
# user = "Admin"
# password = ""
host = ZabbixApi(url, header, user, password)

def get_host(request):
    host_list = host.host_get()
    return render(request, 'zabbixapps/host_list.html', {'host_list':host_list})

def get_template(request):
    template_list = host.template_get()
    # pprint(template_list)
    # return  HttpResponse(template_list)
    return render(request, 'zabbixapps/template_list.html', {'template_list': template_list})

def get_hostgroup(request):
    hostgroup_list = host.hostgroup_get()
    # pprint(hostgroup_list)
    # return HttpResponse(hostgroup_list)
    return render(request, 'zabbixapps/hostgroup_list.html', {'hostgroup_list': hostgroup_list})

def echarts(request):
    return render(request,'echarts.html')

def index(request):
    return render(request, 'index.html')

def form_post(request):
    #当提交表单时使用POST方式
    if request.method == 'POST':
        form = AddForm(request.POST)
        #如果提交的数据合法
        if form.is_valid():
            a = form.cleaned_data['a']
            b =  form.cleaned_data['b']
            ab = sum([a, b])
            return HttpResponse(ab)
    else:
        form = AddForm()
    return render(request, 'zabbixapps/host_manage.html', {'form':form})