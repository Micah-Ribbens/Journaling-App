from django import forms
from writing.models import notes


class ProductForm(forms.ModelForm):
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"rows": 30,
            "cols": 60
            }
        )
    )
    class Meta:
        model = notes
        fields = ('description',)
    
    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get("description")
        if isValidInput(description):
            #It's returning something because a future function (lets call it creator) can't take a NoneType. 
            # So that function (creator) checks to make that the description (see line 6 of this module) isn't a error
            return forms.ValidationError('Please enter a valid title: You could be getting this message because the form is blank or is just "*"')
            
        return description




def isValidInput(description):
    enterCommand = "*"
    blank = ["", " "]
    for ch in description:
        if ch != enterCommand and not blank.__contains__(ch):
            return False
    return True