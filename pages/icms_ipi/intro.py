from reportlab.platypus import Paragraph, PageBreak

from pages.styles.pdf_text import RenderParagraph

render = RenderParagraph()

def icms_ipi_intro():

    elements = [
        PageBreak(),
        render.Text('DAS DISPOSIÇÕES LEGAIS', size=18, bold=True, spaceAfter=18),

        render.Text('LEI Nº 8.218, DE 29 DE AGOSTO DE 1991:', size=12, bold=True, spaceBefore=22, spaceAfter=5),
        render.Text(
            """
            A Lei nº 13.670, de 30 de maio de 2018, veio dar nova redação aos artigos 11 e 12 da Lei nº 8.218, de 1991,
            que dispõe sobre a utilização de sistemas de processamento eletrônico de dados para registrar negócios e
            atividades econômicas ou financeiras, escriturar livros ou elaborar documentos de natureza contábil ou
            fiscal, e a manter, à disposição da Secretaria da Receita Federal, os respectivos arquivos digitais e
            sistemas. Dessa forma, de acordo com o art. 12 da Lei temos a seguinte aplicação:
            """, size=10),

        render.Text(
            """
            Art. 12. A inobservância do disposto no artigo precedente acarretará a imposição das seguintes penalidades:
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            <b>II</b> - multa equivalente a 5% (cinco por cento) sobre o valor da operação correspondente, limitada a 1%
            um por cento) do valor da receita bruta da pessoa jurídica no período a que se refere a escrituração, aos
            que omitirem ou prestarem incorretamente as informações referentes aos registros e respectivos arquivos.
            """, size=10, spaceBefore=10),
    ]

    return elements