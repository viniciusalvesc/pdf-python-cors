def extract_data_report_ids(data_report):
    extracted_reports = []

    if len(data_report) > 0:
        for report in data_report:
            register_id = report['register_id']
            splited_report = register_id.split()

            report_id = splited_report[0]

            if len(report_id) == 4 and report_id not in extracted_reports:
                extracted_reports.append(report_id)
    
        extracted_reports_sorted = sorted(extracted_reports)

        return extracted_reports_sorted

    else:
        return []