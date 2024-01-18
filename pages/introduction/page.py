from reportlab.platypus import Image

from pages.styles.pdf_text import RenderParagraph

from utils.getCNAE import get_company_cnae_info
from utils.formatCNPJ import format_cnpj

finly_logo_img = 'assets/img/fytax_blue.png'

render = RenderParagraph()

def introduction(periods, block_ids, company_name, company_CNPJ):
    # Criando string com os periodos processados
    periods_efd_str = ', '.join(periods['efd'])
    periods_ecf_str = ', '.join(periods['ecf'])
    periods_icms_ipi_str = ', '.join(periods['icms_ipi'])

    # Criando string com os números de registro das ocorrências
    block_ids_efd_str = ', '  .join(block_ids['efd'])
    block_ids_ecf_str = ', '  .join(block_ids['ecf'])
    block_ids_icms_ipi_str = ', '  .join(block_ids['icms_ipi'])

    # TODO: Aplicar lógica para identificar tipo de regime
    company_regimes = ["Cumulativo"]
    company_regimes_str = ' / ' .join(company_regimes)

    # Obtendo o CNAE a partir do CNPJ
    company_cnae = get_company_cnae_info(company_CNPJ)

    # Inicializando variável com os textos
    elements = [
        Image(finly_logo_img, width=100, height=50),

        render.Space(),
        render.Text('RELATÓRIO PDF - (LEITURA SISTÊMICA DOS ARQUIVOS)', size=16, bold=True, spaceAfter=18),
        
        render.Space(),
        render.Text('ID DO PROCESSO:', size=12, bold=True, spaceAfter=5),
        render.Text('2dfb218a95ef5b7852f4c5f43a75c3', size=10, spaceAfter=10),

        render.Space(),
        render.Text('PERÍODOS ANÁLISADOS', size=12, bold=True, spaceAfter=5) if periods_efd_str or periods_ecf_str or periods_icms_ipi_str else None ,
        render.Text(
            f"""
            EFD: {periods_efd_str}
            """, size=10, spaceAfter=5) if periods_efd_str else None,
        render.Text(
            f"""
            ECF: {periods_ecf_str}
            """, size=10, spaceAfter=5) if periods_ecf_str else None,
        render.Text(
            f"""
            ICMS/IPI: {periods_icms_ipi_str}
            """, size=10, spaceAfter=5) if periods_icms_ipi_str else None,

        render.Space(),        
        render.Text('REGISTROS GERADORES DE OCORRÊNCIAS', size=12, bold=True, spaceAfter=5) if block_ids_efd_str or block_ids_ecf_str or block_ids_icms_ipi_str else None,
        render.Text(
            f"""
            EFD: {block_ids_efd_str}
            """, size=10, spaceAfter=5) if block_ids_efd_str else None,
        render.Text(
            f"""
            ECF: {block_ids_ecf_str}
            """,  size=10, spaceAfter=5) if block_ids_ecf_str else None,
        render.Text(
            f"""
            ICMS/IPI: {block_ids_icms_ipi_str}
            """, size=10, spaceAfter=5) if block_ids_icms_ipi_str else None,

        render.Space(),
        render.Text('REGIME DE TRIBUTAÇÃO NO(S) PERÍODO(S) ANALISADO(S):', size=12, bold=True, spaceAfter=5),
        render.Text(f'[ {company_regimes_str} ]', size=10, spaceAfter=10),

        render.Space(),
        render.Text('CONSIDERAÇÕES PRELIMINARES:', size=12, bold=True, spaceAfter=5),
        render.Text('Caro cliente,', size=10, spaceAfter=10),
        render.Text(
            """
            O objetivo principal desta auditoria foi avaliar a conformidade da empresa com as leis e regulamentações
            tributárias vigentes, bem como identificar eventuais riscos e oportunidades de melhoria relacionados à
            Gestão Tributária eletrônica.
            """, size=10, spaceAfter=10),
        render.Text(
            """
            As informações são geradas com base nos arquivos entregues dentro da plataforma Finly Tax.
            """, size=10, spaceAfter=10),
        render.Text(
            f"""
            Primeiramente, cumpre-nos destacar que o(a) <b>{company_name} ( {format_cnpj(company_CNPJ)} )</b>
            tem como principal atividade: <b>{company_cnae}</b>.
            """, size=10, spaceAfter=10)
    ]

    return elements