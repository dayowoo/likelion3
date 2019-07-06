from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import DiaryPost
from django.utils import timezone
import re

# Create your views here.
#적은 모든 글을 확인할 페이지를 보여줄 함수
def home(request):
    diarys=Diary.objects.all
    #diarys라는 이름(변수명)으로 템플릿에 전달
    return render(request, 'home.html',{"diarys":diarys})
 
#새로운 글을 입력받을 페이지를 보여주는 함수   
def new(request):
    return render(request, "new.html")

#여기서 글을 DB에 저장    
def create(request):
    if request.method == "POST":
#        title=request.POST["title"]
#        content=request.POST["content"]
#        #Diary빈틀을 만들고 그 안에 사용자에게 받은 데이터 넣고 저장
#        diary=Diary()
#        diary.title=title
#        diary.content=content
#        diary.time=timezone.now()
#        diary.save()
#        #redirect : 다른 url로 연결해주는 함수
         form = DiaryPost(request.POST, request.FILES)
         if form.is_valid():
             form.save()
         return redirect('home.html')
    elif request.method == "GET":
        form = DiaryPost()
        return render(request, "new.html", {"form":form})

def update_page(request, id):
    #글을 수정할 페이지를 보여줌
    diary=get_object_or_404(Diary, pk=id)
    return render(request, "update.html",{"diary":diary})

def update(request,id):
    #DB에 저장된 글을 수정
    diary = get_object_or_404(Diary, pk=id)
    diary.title = request.GET["title"]
    diary.content=request.GET["content"]
    diary.save()
    return redirect('home')
    
def delete(request,id):
    #DB에서 글 삭제
    diary=get_object_or_404(Diary, pk=id)
    diary.delete()
    return redirect("home")

def search(request):
    tag = Tag.objects.filter(name=request.GET["search"]).first()
    diarys = []
    for hashtag in HashTag.objects.filter(tag=tag):
        diarys.append(hashtag.diary)
    return render(request, "home.html", {"diarys": diarys})
    
    
def save_tag(blog):
    contents = diary.contents
    p = re.compile("#([^\s#]{1,20})")
    # list
    tag_list = p.findall(contents)
    for tag in tag_list:
        tag_obj = Tag.objects.filter(name=tag)
        if not tag_obj.exists():
            tag_obj = Tag(name=tag)
            tag_obj.save()
        #태그와 글을 연결
        HashTag(blog=blog, tag=tag_obj.first).save()    