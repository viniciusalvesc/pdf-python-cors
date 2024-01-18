from reportlab.platypus import Paragraph, PageBreak

from pages.styles.pdf_text import RenderParagraph

render = RenderParagraph()
def last_page(company_name):
    # Inicializando variável com os textos
    elements = [
        PageBreak(),

        render.Text("CONSIDERAÇÕES FINAIS", size=18, bold=True, spaceAfter=18),
        
        render.Text(
            f"""
            Finalmente, a partir das constatações do presente trabalho, bem como das sugestões a(o)
            <b>{company_name.upper()}</b>, julgamos pertinente destacar:
            """, size=10, spaceBefore=10),

        render.Text(
            """
            * Retificação das <b>ECF - Escrituração Contábil Fiscal</b> e seus controles auxiliares de apuração do
            <b>IRPJ</b> e <b>CSLL</b> dos <b>Anos Calendários</b> auditados e <b>competências subsequentes</b>,
            se houver;
            """, size=10, spaceBefore=10),

        render.Text(
            """
            * Aproveitamento correto e conciliado do crédito apurado se houver;
            """, size=10, spaceBefore=10),

        render.Text(
            """
            *Acompanhamento mensal ou trimestral das apurações do <b>IRPJ</b>, <b>CSLL</b>, <b>PIS</b> e <b>COFINS</b>,
            bem como do aproveitamento do crédito apurado junto ao fisco para minimizar o número de intimações e
            consequentes glosas.
            """, size=10, spaceBefore=10),

        render.Text(
            f"""
            Vale ainda destacar que os pontos levantados no presente trabalho, além de representarem possibilidades de
            recuperações fiscais e de mitigação de riscos, muito contribuirão para a continuidade do aprimoramento, em
            curso, dos controles e rotinas fiscais do(a) <b>{company_name.upper()}</b>. Nesse aspecto, alertamos que
            recuperações tributárias dependem de retificação de informações já enviadas ao Fisco, inclusive atentando
            para eventuais reflexos no <b>IRPJ</b>, <b>CSLL</b>, <b>PIS</b> e <b>COFINS</b>.
            """, size=10, spaceBefore=10),
            
        render.Text(
            f"""
            Por fim, agradecemos a colaboração e disponibilidade dos profissionais representantes do(a)
            <b>{company_name.upper()}</b>, que foi fundamental para a realização dos trabalhos.
            """, size=10, spaceBefore=10),
        
        render.Text("Atenciosamente,", size=10, align='center', spaceBefore=300),
        render.Text("FINLY TECH", size=12, bold=True, align='center', spaceBefore=10),
    ]

    return elements