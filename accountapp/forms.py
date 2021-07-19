from django.contrib.auth.forms import UserCreationForm


# UserCreationForm 상속받음
class AccountCreationForm(UserCreationForm):
    # 초기화 메서드
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
