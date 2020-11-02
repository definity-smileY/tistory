from django.shortcuts import render

from .forms import RegisterForm

def register(request):
    if request.method == 'POST': # 정보들을 기입하고 서버로 데이터를 전달할경우
        user_form = RegisterForm(request.POST) # 유효성검사
        if user_form.is_valid():
            user = user_form.save(commit=False) # db에 저장하지않고 메모리상 객체를 만든다
            user.set_password(user_form.cleaned_data['password']) # 비밀번호를 정한다
            user.save() # db저장
            return render(request, 'registration/login.html', {'user':user}) # 회원가입 완료후 로그인창으로 이동
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'user_form': user_form})