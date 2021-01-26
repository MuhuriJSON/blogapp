from django import forms
from . models import PostComment

class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea( 
    attrs ={ 
        'class':'form-control', 
        'placeholder':'Comment here !', 
        'rows':5, 
        'cols':56
    })) 
    class Meta: 
        model = PostComment 
        fields =['content']