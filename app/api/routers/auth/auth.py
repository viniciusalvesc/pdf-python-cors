"""
Nome do arquivo: authRoute.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo responsável pela rota de login do usuário.
"""
from app.api.models.ft_user import UserRepository
from fastapi import APIRouter, Depends, HTTPException
from app.api.schemas.auth_route import LoginRequest
from app.api.services.pusherService import PusherService
from app.api.utils.helpers import password_check
from sqlalchemy.orm import Session
from app.api.utils.tokenHandler import generate_jwt
from app.db.sqlalchemy import get_db

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
import io

auth_router = APIRouter(prefix="/auth")

@auth_router.post('/login')
async def login(request_data: LoginRequest, db: Session = Depends(get_db)):
    try:
        email = request_data.email
        password = request_data.password
        _session = request_data.session

        if not email or not password:
            raise HTTPException(status_code=400, detail='Por favor, informe o email e senha.')

        user = await UserRepository.get_user_by_email(email, db)
        is_password_valid = await password_check(password, user.password)

        if not user or not is_password_valid:
            raise HTTPException(status_code=401, detail='Email ou senha inválidos')

        user.password = None

        data_response = {
            'msg': 'Usuário autenticado com sucesso',
            'data': {
                'token': generate_jwt({'id': user.id, 'email': user.email, 'role': user.role}),
                'user': user
            }
        }

        data_session = {
            'status': 'connected',
            'message': 'Nova sessão iniciada!',
            'session': {
                'id': _session,
            },
        }

        PusherService().send_trigger(
            f'session_user_{user.id}',
            'created_session',
            data_session
        )

        return data_response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f'Ocorreu um erro ao realizar login.\nDescrição: {e}')


def create_pdf_content(data_json, fileName):
    buffer = io.BytesIO()

    # Extraindo informações da empresa (razão social e CNPJ)
    company_info = get_company_info(data_json)

    # DADOS EMPRESA
    company_name = company_info['company_name']
    company_CNPJ = company_info['company_cnpj']

    # Extraindo data_records
    data_records_efd = extract_data_records(
        data_report=data_json, template='efd')
    data_records_ecf = extract_data_records(
        data_report=data_json, template='ecf')
    data_records_icms_ipi = extract_data_records(
        data_report=data_json, template='icms_ipi')

    # Extraindo data_reports
    data_reports_efd = extract_data_reports(data_records=data_records_efd)
    data_reports_ecf = extract_data_reports(data_records=data_records_ecf)
    data_reports_icms_ipi = extract_data_reports(
        data_records=data_records_icms_ipi)

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

    # Criando as tabelas com as ocorrências
    table_efd = create_table(data_report=data_reports_efd, template='efd') if len(
        data_reports_efd) > 0 else []
    table_ecf = create_table(data_report=data_reports_ecf, template='ecf') if len(
        data_reports_ecf) > 0 else []
    table_icms_ipi = create_table(data_report=data_reports_icms_ipi, template='icms_ipi') if len(
        data_reports_icms_ipi) > 0 else []

    # PÁGINAS PDF
    document_pages = [
        *introduction(periods=periods, block_ids=register_ids,
                    company_name=company_name, company_CNPJ=company_CNPJ),

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

    # Criando um objeto PDF em memória
    margin = 40
    pdf = SimpleDocTemplate(fileName, pagesize=letter, topMargin=margin,
                            rightMargin=margin, bottomMargin=margin, leftMargin=margin)

    # Adicionando a numeração de páginas com PageTemplate e Frame
    def add_footer_page_info(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 9)

        # Adicionando o nome da empresa que foi processada alinhado à esquerda
        canvas.drawString(
            margin, margin // 1.2, f'{company_name}   /   {format_cnpj(company_CNPJ)}   -   ( {datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S")} )')

        # Adicionando o número da página à direita
        canvas.drawRightString(
            letter[0] - margin, margin // 1.2, f'Página {doc.page}')

        canvas.restoreState()

    # Adicionando a função add_footer_page_info diretamente ao SimpleDocTemplate
    pdf.build(document_pages, onFirstPage=add_footer_page_info,
                onLaterPages=add_footer_page_info)

    print('Finalizou gerar...')

    # Retorne o conteúdo binário do PDF
    return buffer.getvalue()


@auth_router.post('/teste_victor')
async def teste_victor(request_data: dict):

    try:
        print('Iniciando...')
        # Recuperando o JSON do corpo da solicitação.
        print(type(request_data))
        request_body = request_data
        # print('request_body: ', request_body)

        # Inicializando variáveis com valores
        fileName = 'finly_tax.pdf'

        # Carregando linhas de texto do data.json
        data_json = request_body
        print('data_json: ', data_json)
        # exit()
        # Criando um objeto PDF em memória
        pdf_content = create_pdf_content(data_json, fileName)


        print('pdf_content: ', pdf_content)

        # Retorna um resultado e o conteúdo binário do PDF
        result = {'status': 'success', 'message': 'PDF gerado com sucesso.'}

        return pdf_content.decode('latin-1')

        with open('file.pdf', 'wb') as f:
            f.write(bytes)

        # return {
        #     'statusCode': 200,
        #     'body': json.dumps(result),
        #     'headers': {
        #         'Access-Control-Allow-Origin': '*',
        #         'Access-Control-Allow-Headers': 'Content-Type',
        #         'Access-Control-Allow-Methods': 'POST',
        #         'Content-Type': 'application/pdf',
        #         'Content-Disposition': f'attachment; filename="{fileName}"'
        #     },
        #     'isBase64Encoded': True,
        #     'body': pdf_content.decode('latin-1')  # Alteração aqui
        # }

    except Exception as e:
        error_message = str(e)
        result = {'status': 'error', 'message': error_message}
        return {
            'statusCode': 500,
            'body': json.dumps(result)
        }
    
    