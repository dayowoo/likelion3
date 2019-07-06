from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from diary.models import Diary
from django.contrib.auth.models import User
from .models import Like


# 일단은 함수로 작성
def like(request, blog_id):
    diary = get_object_or_404(Diary, pk=blog_id)
    if request.method == "POST" and request.user.is_authenticated:
        user = request.user
        if len(Like.objects.filter(diary=diary, user=user)) == 0:
            like = Like()
            like.diary = diary
            like.user = user
            like.save()
            return HttpResponse("like")
        else:
            like = get_object_or_404(Like, user=user, diary=diary)
            like.delete()
            return HttpResponse("unlike")
        # TODO : ajax로 처리
    return HttpResponse("")
