from django import forms
class NewBookForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    price = forms.FloatField(label="Price")
    author = forms.CharField(label="Author", max_length=50)
    publisher = forms.CharField(label="Publisher", max_length=50)

class SearchForm(forms.Form):
    title = forms.CharField(label="Search", max_length=50)

class AddBookForm(forms.Form):
    title = forms.CharField(label="Add book", max_length=50)
