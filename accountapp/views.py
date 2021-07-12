from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# 단순 view 만들기
# MVT 중 V
# def hello_world(request):
#     return HttpResponse('Hello World!') return 부분 변경

def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')
        return render(request, 'accountapp/hello_world.html', context={'text': temp})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text':'GET METHOD!'})
