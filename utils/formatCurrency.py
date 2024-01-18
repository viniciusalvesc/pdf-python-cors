import locale

def formatCurrency(value):
    # Configuração local para o Brasil
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf-8')

    # Formatando o valor como moeda brasileira e adicionando o símbolo "R$"
    formated_value = locale.currency(value, grouping=True, symbol="R$ ")

    return formated_value