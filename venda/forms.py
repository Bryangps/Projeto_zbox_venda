from django import forms

TIPO_BEBIDAS = (
    ('ALCOOLICO', 'Alcoólico'),
    ('NAO ALCOOLICO', 'Não Alcoólico')
)


class CadastroBebidaForm(forms.Form):
    category = forms.CharField(label='Categoria')
    nome_produto = forms.CharField(label='Nome do Produto', max_length=100)
    purchase_price = forms.DecimalField(label='Total Gasto', max_digits=10, decimal_places=2)
    sale_price = forms.DecimalField(label='Preço de Venda', max_digits=10, decimal_places=2)

