from django import forms

DUCK_TYPES = (
    ('Duck1', "Duck1"),
    ('Duck2', "Duck2"),
    ('Duck3', "Duck3"),
    ('Duck4', "Duck4"),
    ('Duck5', "Duck5"),
)

class ducks_form(forms.Form):
    ducks_field = forms.ChoiceField(choices=DUCK_TYPES)

DUCK_RATING = (
    ('1', "1"),
    ('2', "2"),
    ('3', "3"),
    ('4', "4"),
    ('5', "5"),
)

class ducks_rating(forms.Form):
    ducks_rating = forms.ChoiceField(choices=DUCK_RATING)


class user_description(forms.Form):
    user_input = forms.CharField(
        label="Duck description",
        max_length=300, 
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your text here...'})
        )




    