from django import forms
from publico.widgets import CustomFileInput, CustomSelect
from . import models
from enum import Enum


class Estado(Enum):
    AC = "Acre"
    AL = "Alagoas"
    AP = "Amapá"
    AM = "Amazonas"
    BA = "Bahia"
    CE = "Ceará"
    DF = "Distrito Federal"
    ES = "Espírito Santo"
    GO = "Goiás"
    MA = "Maranhão"
    MT = "Mato Grosso"
    MS = "Mato Grosso do Sul"
    MG = "Minas Gerais"
    PA = "Pará"
    PB = "Paraíba"
    PR = "Paraná"
    PE = "Pernambuco"
    PI = "Piauí"
    RJ = "Rio de Janeiro"
    RN = "Rio Grande do Norte"
    RS = "Rio Grande do Sul"
    RO = "Rondônia"
    RR = "Roraima"
    SC = "Santa Catarina"
    SP = "São Paulo"
    SE = "Sergipe"
    TO = "Tocantins"

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


class ClienteCadastroForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['nome', 'cpf', 'data_nascimento', 'email']


class ContatoCadastroForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = ["tipo", "valor"]
        widgets = {
            "valor": forms.TextInput(attrs={
                'class': 'input',
            }),
            "tipo": forms.Select(attrs={
                "class": "select"
            })
        }


# https://dontpad.com/franciscosensaulas/exemploclasses
class EnderecoCadastroForm(forms.ModelForm):
    class Meta:
        model = models.Endereco
        fields = ["uf", "cidade", "bairro", "cep", "rua", "numero", "complemento"]
        widgets = {
            "uf": CustomSelect(choices=Estado.choices()),
            "cidade": forms.TextInput(attrs={
                "class": "input"
            }),
            "bairro": forms.TextInput(attrs={
                "class": "input",
            }),
            "cep": forms.TextInput(attrs={
                "class": "input"
            }),
            "rua": forms.TextInput(attrs={
                "class": "input"
            }),
            "numero": forms.TextInput(
                attrs={
                    "class": "input"
                }),
            "complemento": forms.Textarea(attrs={
                "class": "textarea", "required": False
            }),
        }


class ClienteEditarDetalheForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ["nome", "rg", "genero", "foto_perfil"]
        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "input"
            }),
            "rg": forms.TextInput(attrs={
                "class": "input"
            }),
            "genero": CustomSelect(attrs={"class": "seiLa"}),
            "foto_perfil": CustomFileInput
        }
