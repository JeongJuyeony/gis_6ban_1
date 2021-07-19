from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

# 단순 view 만들기
# MVT 중 V
# def hello_world(request):
#     return HttpResponse('Hello World!') return 부분 변경
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

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

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

# 무슨 모델을 읽은것인가에 대한 클래스 선언 (profile page 로직?)
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    # 어떤 객체를 수정할 것인지
    model = User
    # 입력을 위한 창 만들기
    form_class = UserCreationForm
    # html내부에서 해당객체를 어떻게 불러올 것인가
    context_object_name = 'target_user'
    # 수정이 완료 되었을때 어디로 되돌아 가는지
    success_url = reverse_lazy('accountapp:hello_world')
    # 어떤 html기반으로 어떻게 렌더링 할 것인지
    template_name = 'accountapp/update.html'

# 회원탈퇴
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    # 탈퇴가 완료된 후 hello_world 페이지로 돌아간다.
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'


