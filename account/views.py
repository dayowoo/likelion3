from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

# 회원가입
def sign_up(request):
    if request.method == "GET":
        return render(request, "sign_up.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pw"]
        password_check = request.POST["pw_check"]
        # 비밀번호 재확인 불일치
        if password != password_check:
            return render(request, "sign_up.html")
        # 새로운 유저 생성
        user = User.objects.create_user(username=username, password=password)
        auth.login(request,user)
    return redirect("home")
    
# 로그인
def sign_in(request):
    if request.method == "GET":
        return render(request, "sign_in.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pw"]
        user = auth.authenticate(request, username=username, password=password)
        # 존재하지 않는 user
        if user is None:
            return render(request, "sign_in.html")
        #로그인 처리
        auth.login(request, user)
    return redirect("home")
    
# 로그아웃
def sign_out(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            auth.logout(request)
    return redirect("home")