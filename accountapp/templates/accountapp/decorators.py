from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            # 금지된 곳에 접근
            return HttpResponseForbidden()

    # 호출한 것이 아닌 함수자체를 리턴턴
    return decorated