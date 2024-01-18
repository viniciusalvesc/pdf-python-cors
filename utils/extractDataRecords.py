def extract_data_records(data_report, template):
    """
    Extraindo os records a partir do template.
    """
    return data_report.get(template, {}).get('records', [])
