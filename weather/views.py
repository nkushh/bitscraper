from django.shortcuts import render
from .models import Reading

# Create your views here.
def home(request):
	data = Reading.objects.last()
	temp = data.temp
	# convert to degrees celsius
	temp_celsius = (temp-32)/1.8
	context = {
		'data' : data,
		'temp_celsius' : temp_celsius,
	}

	return render(request, 'weather/index.html', context)
