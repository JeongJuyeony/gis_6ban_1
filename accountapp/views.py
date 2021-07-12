from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

# 단순 view 만들기
# MVT 중 V
# def hello_world(request):
#     return HttpResponse('Hello World!') return 부분 변경
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        # new_hello_world : 단일객체
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # Redirect
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
