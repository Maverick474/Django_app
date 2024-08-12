from django.shortcuts import render
from .models import DataPoint
# Create your views here.

def base(request):
    context = {}
    context['title'] = 'Home'
    return render(request, 'index.html', context)

def data(request):
    data_points = DataPoint.objects.all()
    return render(request, 'data.html', {'data_points': data_points, 'title': 'Data_page'})

def hist1(request):
    context = {}
    context['title'] = 'Histogram'
    return render(request, 'hist1.html', context)

def hist(request):
    context = {}
    context['title'] = 'Histogram'
    return render(request, 'histogram.html', context)

def scatter(request):
    context = {}
    context['title'] = 'Scatter Plot'
    return render(request, 'scatter.html', context)

def pie(request):
    context = {}
    context['title'] = 'Pie Chart'
    return render(request, 'pie.html', context)

def box(request):
    context = {}
    context['title'] = 'Box Plot'
    return render(request, 'box.html', context)

def frequency(request):
    context = {}
    context['title'] = 'Frequency'
    return render(request, 'frequency.html', context)