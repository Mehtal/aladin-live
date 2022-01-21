from django import forms


class GetBroadcastForm(forms.Form):
    code = forms.CharField(max_length=20)
