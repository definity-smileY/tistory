from django import forms

from .models import User


class RegisterForm(forms.ModelForm):
    # 회원가입 폼
    # 장고에서는 HTML 입력요소를 widget(위젯)이라고 말한다.
    password = forms.CharField(label='password', widget=forms.PasswordInput) # 비밀번호
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput) # 비밀번호확인

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'email']
        
    def clean_confirm_password(self): # 각 필드의 호출 후 유효성검사할때 사용
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

        return cd['confirm_password']