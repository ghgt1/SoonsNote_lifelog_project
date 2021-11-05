from django.shortcuts import render
import numpy as np
import pandas as pd
from .forms import PostForm
from django.http import HttpResponse
import plotly
import plotly.graph_objs as go


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
    id = int(pk)
    context["graph"] = plot_graph(id)
    context["graph2"] = plot_graph2(id)
    return render(request, 'profiles/life_env.html', context= context)

def ai_talk(request, pk):
    context={}
    context["user_id"] = pk
    context["name"] = getperson(df, pk)['NAME'].values[0]
    context["ai_anal_max1"] = getperson(df, pk)['Favorite_1'].values[0]
    context["ai_anal_max2"] = getperson(df, pk)['Favorite_2'].values[0]
    res_rate = float(getperson(df, pk)['Response_Rate'].values[0])
    context["response_rate"] = res_rate
    context["ai_rec_max1"] = getperson(df, pk)['Recommendation_1'].values[0]
    context["ai_rec_max2"] = getperson(df, pk)['Recommendation_2'].values[0]
    return render(request, 'profiles/ai_talk.html',context=context)

def plot_graph(id):
    data = [
        go.Bar(
            x=[getperson(df, id)['Analysis_MAX1'].values[0],getperson(df, id)['Analysis_MAX2'].values[0],getperson(df, id)['Analysis_MAX3'].values[0]],
            y=[getperson(df, id)['MAX1_Count'].values[0],getperson(df, id)['MAX2_Count'].values[0],getperson(df, id)['MAX3_Count'].values[0]]
        )
    ]
    
    layout = plotly.graph_objs.Layout(
        title='Bar-chart'
    )
    
    figure = plotly.graph_objs.Figure(
        data=data, layout=layout
    )
    
    return figure.to_html(full_html=False)

def plot_graph2(id):
    data = [
        go.Bar(
            x=[getperson(df, id)['Analysis_MIN1'].values[0],getperson(df, id)['Analysis_MIN2'].values[0],getperson(df, id)['Analysis_MIN3'].values[0]],
            y=[getperson(df, id)['MIN1_Count'].values[0],getperson(df, id)['MIN2_Count'].values[0],getperson(df, id)['MIN3_Count'].values[0]]
        )
    ]
    
    layout = plotly.graph_objs.Layout(
        title='Bar-chart'
    )
    
    figure = plotly.graph_objs.Figure(
        data=data, layout=layout
    )
    
    return figure.to_html(full_html=False)