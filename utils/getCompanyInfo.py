def get_company_info(data):
    for key, values in data.items():
        company_name = values.get("company_name", None)
        company_cnpj = values.get("company_cnpj", None)
        
        if company_name is not None and company_cnpj is not None:
            return {"company_name": company_name, "company_cnpj": company_cnpj}
    
    # Se não encontrar em nenhuma chave
    return {"company_name": "Nome não encontrado", "company_cnpj": "CNPJ não encontrado"}