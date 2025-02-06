from django import forms

class RecForm(forms.Form):
    url = forms.URLField(label="AO3 link", max_length=42)
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))