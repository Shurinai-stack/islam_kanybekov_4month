from django import forms
from posts.models import Categorys, Post, Tag
 
class PostForm(forms.Form):
    image = forms.ImageField(label="Image", )
    title = forms.CharField(label="Title", max_length=250)
    content = forms.CharField(label="Content", max_length=1000)
    rate = forms.IntegerField(label="Rate")

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title.lower() == "javascript":
            raise forms.ValidationError("Js is bad")
        return title
    
class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'content', 'rate')

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title.lower() == "javascript":
            raise forms.ValidationError("Js is bad")
        return title
    
class SearchForm(forms.Form):
    search = forms.CharField(label='Search', required=False)
    category_id = forms.ModelChoiceField(queryset=Categorys.objects.all(), required=False)
    tags_ids = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    orderings = (('rate', 'По оценкам'), ('-rate', 'По оценкам убывания'), ('title', 'По названию'), ("-title", "По названию убывания"), ('', 'без содержания'), ('created_at', 'по дате создания'), ('-created_at', 'по дате убывания'), ('updated_at', 'по дате обновления'), ('-updated_at', 'по дате обновления убывания')) 
    ordering = forms.ChoiceField(choices=orderings, required=False)