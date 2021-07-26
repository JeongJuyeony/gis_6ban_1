

from django.forms import ModelForm

# 장고에서 제공해주는 ModleForm : 상속
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
