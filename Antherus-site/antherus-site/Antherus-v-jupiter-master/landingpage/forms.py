from django import forms
from .models import Formulario, Perfil, CadastroClientes, Produto


class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'


class StatusForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = (
            'status',
        )


class AnotacoesForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = (
            'anotacoes',
        )


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class CadastroClientesForm(forms.ModelForm):
    class Meta:
        model = CadastroClientes
        fields = (
                  'tipo_juridico',
                  'cnpj',
                  'nome_empresa',
                  'cpf',
                  'nome_usuario',
                  'ramo_atividade',
                  'telefone',
                  'cep',
                  'endereco',
                  'num_endereco',
                  'bairro',
                  'cidade',
                  'estado',
                  'status_cliente',
                  )


class ContratacaoForm(forms.ModelForm):
    class Meta:
        model = CadastroClientes
        fields = (
            'produto',

        )