from django import forms
from core.models import Endereco



class EnderecoForms(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'endereco', 'numero_endereco', 'complemento', 'bairro', 'cidade', 'uf', 'descricao']

