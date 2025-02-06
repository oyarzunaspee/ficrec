from django import forms

class RecForm(forms.Form):
    url = forms.URLField(label="AO3 link", max_length=42)
    title = forms.CharField()
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":"5"}))
    author = forms.CharField()
    word_count = forms.IntegerField(required=True)
    summary = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":"5"}))