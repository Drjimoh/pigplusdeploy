from django.shortcuts import render
from .models import PigHealth

# Create your views here.

def record_list(request):
	health = PigHealth.objects.all()
	return render(request, 'pigdata/post_list.html', {'health':health})