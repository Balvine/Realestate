from django import forms
from .models import UserProfile,Post,Comment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','bio','email')


class PostForm(forms.ModelForm):
    CHOICES = (('1', 'Amber',), ('2', 'Normal',))
    type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    class Meta:
        model = Post
        fields = ('title','content','type')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
