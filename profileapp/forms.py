

from django.forms import ModelForm

# 장고에서 제공해주는 ModleForm : 상속
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
        # 클라이언트가 user에 접근하지 못하도록 user을 확인한 후에 서버에서 요청에 응답을 할 예정