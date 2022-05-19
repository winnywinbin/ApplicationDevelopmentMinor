from django.core.exceptions import ValidationError

from .models import Highscore, Woord
from django import forms

SPELMODUS = [
    ('', ''),
    ('tijd', 'Tijd'),
    ('woorden', 'Woorden'),
]

TIJD = [
    ('', ''),
    ('60', '1 minuut'),
    ('120', '2 minuten'),
    ('300', '5 minuten'),
]

WOORDEN = [
    ('', ''),
    ('50', '50 woorden'),
    ('100', '100 woorden'),
    ('150', '150 woorden'),
]

TALEN = [
    ('', ''),
    ('nederlands', 'Nederlands'),
    ('engels', 'Engels'),
]

MOEILIJKHEID = [
    ('', ''),
    ('makkelijk', 'Makkelijk'),
    ('gemiddeld', 'Gemiddeld'),
    ('moeilijk', 'Moeilijk'),
]

class InstellingenForm(forms.Form):
    naam = forms.CharField(label="Naam",
                           max_length=10,
                           required=False,
                           widget=forms.TextInput(
                               attrs={'class': 'input-container'}))
    spelmodus = forms.ChoiceField(label="Spelmodus",
                                  choices=SPELMODUS,
                                  required=False,
                                  widget=forms.Select(
                                      attrs={'class': 'input-container', 'id': 'spelmodus', 'onchange': 'hideShow(this.value)', }))
    tijd = forms.ChoiceField(label="",
                             choices=TIJD,
                             required=False,
                             widget=forms.Select(
                                 attrs={'class': 'input-container', 'id': 'tijdClass'}))
    woorden = forms.ChoiceField(label="",
                                choices=WOORDEN,
                                required=False,
                                widget=forms.Select(
                                    attrs={'class': 'input-container', 'id': 'woordenClass'}))
    taal = forms.ChoiceField(label="Taal",
                             choices=TALEN,
                             required=False,
                             widget=forms.Select(
                                 attrs={'class': 'input-container'}))
    moeilijkheid = forms.ChoiceField(label="Moeilijkheid",
                                     choices=MOEILIJKHEID,
                                     required=False,
                                     widget=forms.Select(
                                         attrs={'class': 'input-container'}))

class CustomForm(forms.Form):
    naam = forms.CharField(label="Naam",
                           max_length=10,
                           required=False,
                           widget=forms.TextInput(
                               attrs={'class': 'input-container'}))
    spelmodus = forms.ChoiceField(label="Spelmodus",
                                  choices=SPELMODUS,
                                  required=False,
                                  widget=forms.Select(
                                      attrs={'class': 'input-container',
                                             'id': 'spelmodus',
                                             'onchange': 'customHideShow(this.value)', }))
    tijd = forms.ChoiceField(label="",
                             choices=TIJD,
                             required=False,
                             widget=forms.Select(
                                 attrs={'class': 'input-container',
                                        'id': 'tijdClass'}))
    woorden = forms.CharField(label='Woorden',
                              required=False,
                              widget=forms.Textarea(
                                  attrs={'id': 'textarea'}))

    file = forms.FileField(label="Upload file met woorden",
                           required=False,
                           widget=forms.FileInput(
                               attrs={'video_file': forms.FileInput(
                                   attrs={'accept': '.csv,.txt'}
                               )}))

