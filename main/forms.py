from django import forms

class RecForm(forms.Form):
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":"5"}))
    share = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":"5"}))
    """title = forms.CharField()
    url = forms.URLField(label="AO3 link", max_length=42)
    author = forms.CharField()
    word_count = forms.IntegerField(required=True)
    summary = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":"5"}))"""