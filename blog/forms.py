from django import forms
from .models import Post,Comment

attrs = {"class":'form-control'}

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','content','category']
        widgets = {
            'title':forms.TextInput(attrs=attrs),
            'content':forms.Textarea(attrs=attrs),
            'category':forms.Select(attrs=attrs),
        }
class UpdatePostForm(forms.ModelForm):
        
    class Meta:
        model = Post
        fields = ['title','content']
        widgets = {
            'title':forms.TextInput(attrs=attrs),
            'content':forms.Textarea(attrs=attrs),
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        widget={
            "content":forms.Textarea(attrs=attrs)
        }


