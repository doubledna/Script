#-*- codig:utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from models import DyModels
# Create your views here.
def index(request, page = 0):
    page = int(page)
    #template1 = loader.get_template('dy/index.html') #

    if page > 1:
        return render(request, 'dy/index.html', context = {'model_list': DyModels.objects.all()[(page - 1) * 15 : page * 15],'down' : page -1,'up': page + 1,})
    else:
        return render(request, 'dy/index.html',context = {'model_list': DyModels.objects.all()[:15],'up': page + 1})


def movie(request, id):
    '''
    #template2 = loader.get_template('dy/content.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))
    '''
    model = DyModels.objects.get(id = id)
    return render(request, 'dy/content.html', context={'name' : model.name, 'url': model.url})
