def format_cnpj(cnpj):
    # Remove caracteres não numéricos do CNPJ
    cnpj = ''.join(filter(str.isdigit, str(cnpj)))

    # Formata o CNPJ (XX.XXX.XXX/YYYY-ZZ)
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"