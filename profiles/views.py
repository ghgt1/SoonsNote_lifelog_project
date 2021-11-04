from django.shortcuts import render
import numpy as np
import pandas as pd
from .forms import PostForm
from django.http import HttpResponse


df = pd.read_excel("export.xlsx", engine='openpyxl').drop('Unnamed: 0', axis=1)
# Create your views here.
def getperson(df, code):
    return df[df['NUM'] == code]

def home(request):
    post_form = PostForm()
    return render(request, 'profiles/index.html', {'form':post_form})

def index(request):
    id = request.GET.get('input_id','')
    print(id)
    post_form = PostForm()
    if id=='':
        return render(request, 'profiles/index.html', {'form':post_form})

def detail(request):
    id = request.GET.get('input_id','')
    post_form = PostForm()
    if id=='':
        return render(request, 'profiles/index.html', {'form':post_form})
    else:
        id = int(id)
    context={}
    context["name"] = getperson(df, id)['NAME'].values[0]
    context["sex"] = getperson(df, id)['SEX'].values[0]
    context["age"] = getperson(df, id)['AGE'].values[0]
    context["user_id"] = id
    context["form"] = post_form
    return render(request, 'profiles/detail.html',context= context)

def life_env(request, pk):
    post_form = PostForm()
    context={}
    context["user_id"] = pk
    context["name"] = getperson(df, pk)['NAME'].values[0]
    context["anal_max1"] = getperson(df, pk)['Analysis_MAX1'].values[0]
    context["anal_max2"] = getperson(df, pk)['Analysis_MAX2'].values[0]
    context["anal_min1"] = getperson(df, pk)['Analysis_MIN1'].values[0]
    context["anal_min2"] = getperson(df, pk)['Analysis_MIN2'].values[0]
    context["form"] = post_form
    return render(request, 'profiles/life_env.html', context= context)

def ai_talk(request, pk):
    context={}
    context["user_id"] = pk
    return render(request, 'profiles/ai_talk.html',context=context)
