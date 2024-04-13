from django import forms


class PhotoProduct(forms.Form):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form__photo'}))


# attrs={'onchange': 'submit()'}
