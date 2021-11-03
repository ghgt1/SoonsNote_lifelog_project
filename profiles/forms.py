from django import forms

class PostForm(forms.Form):
    input_id = forms.IntegerField(label = '아이디')
    