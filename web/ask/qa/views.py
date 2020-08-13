from django.shortcuts import render
from django.http import HttpResponse 


def test(request, *args, **kwargs):
	"""Simple test view"""
    return HttpResponse('OK')

