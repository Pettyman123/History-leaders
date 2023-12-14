from django import forms

class leaderform(forms.Form):
    search_leader = forms.CharField(label = 'Person name', max_length= 200)
    