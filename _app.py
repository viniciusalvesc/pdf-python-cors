import json
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate

from utils.getCompanyInfo import get_company_info
from utils.extractDataRecords import extract_data_records
from utils.extractDataReport import extract_data_reports
from utils.extractDataPeriods import extract_data_period
from utils.extractDataReportIds import extract_data_report_ids

from utils.createTable import create_table
from utils.formatCNPJ import format_cnpj

from pages.introduction.page import introduction

from pages.efd.intro import efd_intro
from pages.ecf.intro import ecf_intro
from pages.icms_ipi.intro import icms_ipi_intro

from pages.last_page.page import last_page

class App:
    def __init__(self) -> None:
        actual_date = datetime.utcnow()
        self.rendered_date = actual_date.strftime("%d-%m-%Y %H:%M:%S")

    def load_data(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def createDoc(self):
        # Inicializando variáveis com valores
        fileName = 'finly_tax.pdf'

        # Carregando linhas de texto do data.json
        # data_json = self.load_data('./assets/json/largeData.json')
        data_json = self.load_data('./assets/json/dataReport.json')

        # Extraindo informações da empresa ( razão social e cnpj )
        company_info = get_company_info(data_json)

        # DADOS EMPRESA
        company_name = company_info['company_name']
        company_CNPJ = company_info['company_cnpj']

        # Extraindo data_records
        data_records_efd = extract_data_records(data_report=data_json, template='efd')
        data_records_ecf = extract_data_records(data_report=data_json, template='ecf')
        data_records_icms_ipi = extract_data_records(data_report=data_json, template='icms_ipi')

        # Extraindo data_reports
        data_reports_efd = extract_data_reports(data_records=data_records_efd)
        data_reports_ecf = extract_data_reports(data_records=data_records_ecf)
        data_reports_icms_ipi = extract_data_reports(data_records=data_records_icms_ipi)

        # Extraindo datas dos arquivos processados
        periods = {
            "efd": extract_data_period(data_json=data_json, template='efd'),
            "ecf": extract_data_period(data_json=data_json, template='ecf'),
            'icms_ipi': extract_data_period(data_json=data_json, template='icms_ipi')
        }
        print('periods: ', periods)

        # Extraindo IDs de ocorrências dos arquivos processados
        register_ids = {
            "efd": extract_data_report_ids(data_reports_efd),
            "ecf": extract_data_report_ids(data_reports_ecf),
            'icms_ipi': extract_data_report_ids(data_reports_icms_ipi)
        }
        print('register_ids: ', register_ids)

        # Criando um objeto PDF
        margin = 40
        pdf = SimpleDocTemplate(fileName, pagesize=letter, topMargin=margin, rightMargin=margin, bottomMargin=margin, leftMargin=margin)

        # Criando as tabelas com as ocorrencias
        table_efd = create_table(data_report=data_reports_efd, template='efd') if len(data_reports_efd) > 0 else []
        table_ecf = create_table(data_report=data_reports_ecf, template='ecf') if len(data_reports_ecf) > 0 else []
        table_icms_ipi = create_table(data_report=data_reports_icms_ipi, template='icms_ipi')  if len(data_reports_icms_ipi) > 0 else []

        # PÁGINAS PDF
        document_pages = [
            *introduction(periods=periods, block_ids=register_ids, company_name=company_name, company_CNPJ=company_CNPJ),

            # Tabela EFD
            *(table_efd if table_efd else []),
            *(efd_intro() if table_efd else []),

            # Tabela ECF
            *(table_ecf if table_ecf else []),
            *(ecf_intro() if table_ecf else []),

            # Tabela ICMS_IPI
            *(table_icms_ipi if table_icms_ipi else []),
            *(icms_ipi_intro() if table_icms_ipi else []),

            *last_page(company_name=company_name)
        ]

        # Adicionando a numeração de páginas com PageTemplate e Frame
        def add_footer_page_info(canvas, doc):
            canvas.saveState()
            canvas.setFont('Helvetica', 9)

            # Adicionando o nome da empresa que foi processada alinhado à esquerda
            canvas.drawString(margin, margin // 1.2, f'{company_name}   /   {format_cnpj(company_CNPJ)}   -   ( {self.rendered_date} )')

            # Adicionando o número da página à direita
            canvas.drawRightString(letter[0] - margin, margin // 1.2, f'Página {doc.page}')

            canvas.restoreState()


        # Adicionando a função add_footer_page_info diretamente ao SimpleDocTemplate
        pdf.build(document_pages, onFirstPage=add_footer_page_info, onLaterPages=add_footer_page_info)

    # def run(self):
    #     print('Iniciando app...')
    #     self.createDoc()

# app = App()
# app.run()
