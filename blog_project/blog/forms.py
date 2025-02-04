from django import forms
from blog.models import Post, Comment

# class PostForm(forms.ModelForm):
    
#     class Meta():
#         model = Post
#         fields = ('author', 'title', 'text')
        
#         widgets = {
#             'title': forms.TextInput(attrs={'class':'textinputclass'}),
#             'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
#         }
        
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={
                'class': 'editable postcontent',  # Removed 'medium-editor-textarea' to prevent infinite expansion
                'rows': 20,  # Set fixed height of 5 lines
            }),
        }

class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author', 'text')
        
        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
        
