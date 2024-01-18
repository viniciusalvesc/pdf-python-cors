import requests

def get_company_cnae_info(cnpj):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        response_json = response.json()

        cnae_fiscal = response_json.get('cnae_fiscal')
        cnae_fiscal_descricao = response_json.get('cnae_fiscal_descricao')

        if cnae_fiscal and cnae_fiscal_descricao:
            return f"{cnae_fiscal} - {cnae_fiscal_descricao}"
        else:
            print("As informações necessárias não estão presentes na resposta da API.")
            return None

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        return None

    except requests.exceptions.RequestException as req_err:
        print(f"Erro na requisição: {req_err}")
        return None
