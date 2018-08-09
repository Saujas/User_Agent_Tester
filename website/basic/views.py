# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BasicUser
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

def index(request):
	var = False
	if request.POST:
		name=request.POST['name']
		email=request.POST['email']
		ip_address = request.META['REMOTE_ADDR']
		obj = BasicUser(name=name, email=email, ip=ip_address)
		obj.save()
		var = True
	return render(request, 'basic/index.html', {'yes': var})