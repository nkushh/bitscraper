from django.core.paginator import Paginator
from django.db.models import Avg, Min, Max
from django.shortcuts import render
from .models import BitcoinPrice
import datetime, calendar

# Create your views here.
def home(request):
	leo = datetime.date.today()
	today = datetime.datetime.now()
	mwaka = today.year

	months_choices = []
	for i in range(1,13):
	    months_choices.append((i, datetime.date(mwaka, i, 1).strftime('%B')))

	price_list = BitcoinPrice.objects.filter(time_added__year=leo.year, time_added__month=leo.month).order_by('-time_added')
	price_graph = BitcoinPrice.objects.filter(time_added__year=leo.year, time_added__month=leo.month).extra(select={'day': 'date(time_added)'}).values('day').annotate(top_price=Max('usd'), low_price = Min('usd'))
	price_range = BitcoinPrice.objects.filter(time_added__year=leo.year, time_added__month=leo.month).aggregate(max_price = Max('usd'), min_price = Min('usd'))

	page = request.GET.get('page', 1)

	paginator = Paginator(price_list, 15)

	try:
		prices = paginator.page(page)
	except PageNotAnInteger:
		prices = paginator.page(1)
	except EmptyPage:
		prices = paginator.page(paginator.num_pages)



	context = {
		'months_choices' : months_choices,
		'prices' : prices,
		'price_graph' : price_graph,
		'price_range' : price_range,
	}
	return render(request, 'bitprice/index.html', context)



# Query by month
def monthly_records(request, month):
	today = datetime.datetime.now()
	mwaka = today.year
	if not month:
		month = today.month

	months_choices = []
	for i in range(1,13):
	    months_choices.append((i, datetime.date(mwaka, i, 1).strftime('%B')))


	price_list = BitcoinPrice.objects.filter(time_added__year=mwaka, time_added__month=month).order_by('-time_added')
	price_graph = BitcoinPrice.objects.filter(time_added__year=mwaka, time_added__month=month).extra(select={'day': 'date(time_added)'}).values('day').annotate(top_price=Max('usd'), low_price = Min('usd'))
	price_range = BitcoinPrice.objects.filter(time_added__year=mwaka, time_added__month=month).aggregate(max_price = Max('usd'), min_price = Min('usd'))
	query_month = calendar.month_name[int(month)]

	page = request.GET.get('page', 1)

	paginator = Paginator(price_list, 15)

	try:
		prices = paginator.page(page)
	except PageNotAnInteger:
		prices = paginator.page(1)
	except EmptyPage:
		prices = paginator.page(paginator.num_pages)



	context = {
		'months_choices' : months_choices,
		'prices' : prices,
		'price_graph' : price_graph,
		'price_range' : price_range,
		'query_month' : query_month,
	}
	return render(request, 'bitprice/index.html', context)














