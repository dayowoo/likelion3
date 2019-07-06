from django import forms
from .models import Diary

# Diary 모델을 기준으로 title, content, image를 입력받을수 있는 form을 만들겠다
class DiaryPost(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ["title","content","image"] 