from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, resolve_url
from django.shortcuts import get_object_or_404
import json
import sys
sys.path.append('..')
from .models import Task


import home_work
context = {'result_1':'', 'input_string_1':''}
def index(request):
    
    if request.GET.get("input_string_1"):
        input_string_1 = request.GET["input_string_1"]  # Getting input string
        result_1 = home_work.len_str(input_string_1)  # 
        context = {'result_1':result_1, 'input_string_1':input_string_1}
    else:
        result_1 = None
        context = {'result_1':result_1, 'input_string_1':''}

    if request.GET.get("input_string_2"):
        input_string_2 = request.GET["input_string_2"]  # Getting input string
        result_2 = home_work.count_character_frequency(input_string_2)  # 
        context = {'result_2':result_2, 'input_string_2':input_string_2}

    if request.GET.get("input_string_3"):
        input_string_3 = request.GET["input_string_3"]  # Getting input string
        input_list = input_string_3.split(' ')
        result_3 = home_work.unique_words_sorted(input_list)  # 
        context = {'result_3':result_3, 'input_string_3':input_string_3}

    if request.GET.get("input_string_33"):
        input_string_33 = request.GET["input_string_33"]  # Getting input string
        result_33 = home_work.get_divisors_number(int(input_string_33))  # 
        context = {'result_33':result_33, 'input_string_33':input_string_33}
    
    if request.GET.get("input_string_4"):
        input_string_4 = request.GET["input_string_4"]  # Getting input string
        print(input_string_4, type(input_string_4))
        dict_input = json.loads(input_string_4)
        print(dict_input)
        result_4 = home_work.sort_dictionary_by_key(dict_input)  # 
        context = {'result_4':result_4, 'input_string_4':input_string_4}
    print(context)
    
    return render(request, 'home_work_2/homework_2.html', context)



def tasks(request):
    print(request)
    if request.GET.get("input_string_5"):
        input_string_5 = request.GET["input_string_5"]
        result_5 =input_string_5
        print('!!!!!!!!!!!!!!!!!')
        context.update({'result_5':result_5, 'input_string_5':input_string_5})
    return render(request, 'home_work_2/task.html', context)

def detail(request, task_id):
    context={'task_id': task_id}
    print(context)
    list_task = Task.objects.order_by('number')
    context['list_task'] = list_task 
    detail_task = get_object_or_404(Task, pk=task_id)
    print(detail_task)
    context['detail_task'] = detail_task
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'home_work_2/task.html', context)

