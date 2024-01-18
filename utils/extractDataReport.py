def extract_data_reports(data_records):
    """
    Extraindo dados do data_report a partir do template, esses dados são utilizados
    para gerar as tabelas de ocorrências do PDF
    """
    if data_records:
        last_record = data_records[-1]
        return last_record.get('data_report', [])

    return []
