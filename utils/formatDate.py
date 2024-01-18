from datetime import datetime

def format_date(date_str):
    # Convertendo a string para um objeto de data
    date = datetime.strptime(date_str, "%d%m%Y")

    # Formatando a data como string no formato desejado
    formated_date = date.strftime("%d/%m/%Y")

    return formated_date