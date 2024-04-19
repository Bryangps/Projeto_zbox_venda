from django import forms

TIPO_BEBIDAS = (
    ('ALCOOLICO', 'Alcoólico'),
    ('NAO ALCOOLICO', 'Não Alcoólico')
)


class CadastroBebidaForm(forms.Form):
    nome_produto = forms.CharField(label='Nome do Produto', max_length=100)
    tipo = forms.CharField(label='Tipo')
    qtd_caixas = forms.IntegerField(label='Quantidade de Caixas')
    Unidade = forms.IntegerField(label='Unidade')
    valor_gasto = forms.FloatField(label='Valor Gasto')
    valor_venda = forms.FloatField(label='Valor Venda')


