from datetime import datetime
from utils.formatDate import format_date

def extract_data_period(data_json, template):
    data_periods = set(data_json.get(template, {}).get('period', []))

    extracted_periods = [format_date(period) for period in data_periods if period != 'all']

    return sorted(extracted_periods, key=lambda x: datetime.strptime(x, '%d/%m/%Y'))
