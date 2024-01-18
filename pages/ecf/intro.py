from reportlab.platypus import PageBreak

from pages.styles.pdf_text import RenderParagraph

render = RenderParagraph()

def ecf_intro():
    elements = [
        PageBreak(),
        render.Text('DAS DISPOSIÇÕES LEGAIS', size=18, bold=True, spaceAfter=18),
        render.Text(
            """
            De acordo com o inciso II do art. 6° da Instrução normativa RFB n° 2.004/2021, os contribuintes que apuram
            o Imposto sobre a Renda da Pessoa Jurídica por qualquer sistemática que não o Lucro Real que deixarem de
            apresentar a ECF nos prazos fixados no art 3° ou a apresentar com incorreções ou omissões, ficam sujeito a
            aplicação de multas previstas no art. 12 da lei n° 8.218, de 29 de agosto de 1991.
            """, size=10, spaceBefore=10),

        render.Text("LEI Nº 8.218, DE 29 DE AGOSTO DE 1991", size=10, spaceBefore=10),
        
        render.Text(
            """
            Art. 12. A inobservância do disposto no artigo precedente acarretará a imposição das seguintes penalidades:
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            <b>II</b> - multa equivalente a 5% (cinco por cento) sobre o valor da operação correspondente, limitada a 1%
            (um por cento) do valor da receita bruta da pessoa jurídica no período a que se refere a escrituração,
            aos que omitirem ou prestarem incorretamente as informações referentes aos registros e respectivos arquivos;
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            <b>III</b> - multa equivalente a 0,02% (dois centésimos por cento) por dia de atraso, calculada sobre a receita
            bruta da pessoa jurídica no período a que se refere a escrituração, limitada a 1% (um por cento) dessa, aos
            que não cumprirem o prazo estabelecido para apresentação dos registros e respectivos arquivos.
            """, size=10, spaceBefore=10),

        
        render.Text('DAS DEDUÇÕES DO IMPOSTO SOBRE A RENDA', size=12, bold=True, spaceBefore=22, spaceAfter=5),
        render.Text(
            """
            Art. 599. Para fins de pagamento, a pessoa jurídica poderá deduzir do imposto sobre a renda devido no
            período de apuração, o imposto pago ou retido na fonte sobre as receitas que integraram a base de cálculo,
            vedada qualquer dedução a título de incentivo fiscal(Lei nº 8.981, de 1995, art. 34 ; Lei nº 9.430, de 1996,
            art. 51, parágrafo único ; e Lei nº 9.532, de 1997, art. 10 )
            """, size=10),
        render.Text(
            """
            Parágrafo único. Na hipótese em que o imposto sobre a renda retido na fonte ou pago seja superior ao devido,
            a diferença poderá ser utilizada na compensação de débitos próprios, nos termos estabelecidos no art. 940
            (Lei nº 9.430, de 1996, art. 74 ). (grifo nosso)
            """, size=10, spaceBefore=10),
          
        render.Text('IN 1700/2017 ART. 44.', size=12, bold=True, spaceBefore=22, spaceAfter=5),
        render.Text(
            """
            Para determinação do valor do IRPJ a pagar a pessoa jurídica poderá ainda deduzir do imposto devido, apurado
            conforme os arts. 42 e 43, o imposto pago ou retido na fonte sobre as receitas que integraram a respectiva
            base de cálculo.
            """, size=10),
        
        render.Text("(...)", size=10, spaceBefore=20),
        render.Text("Art. 47. A pessoa jurídica poderá:", size=10, spaceBefore=20),
        render.Text("(...)", size=10, spaceBefore=20),
        
        PageBreak(),
        render.Text(
            """
            § 5º Para determinação do valor do IRPJ a pagar no mês a pessoa jurídica poderá deduzir do imposto devido
            no período em curso:
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            <b>I</b> - o valor do IRPJ devido por estimativa em meses anteriores do ano-calendário, seja com base na receita
            bruta e acréscimos ou em balanço ou balancete de redução;
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            <b>II</b> - o IRPJ pago ou retido na fonte sobre as receitas auferidas no mês, que integraram a respectiva
            base de cálculo;
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            Atenção: As retenções efetivamente sofridas pela PJ no mês da escrituração, informadas neste registro, nos
            campos 09 (PIS/Pasep) e 10 (Cofins), não são recuperadas de forma automática nos respectivos registros
            apuração das contribuições M200 (PIS/Pasep) e M600 (Cofins), devendo ser sempre informados pela própria
            pessoa jurídica no arquivo importado pelo PVA ou complementado pela edição, no próprio PVA, dos registros
            M200 e M600.
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            § 6º Para determinação do valor da CSLL a pagar no mês a pessoa jurídica poderá deduzir da contribuição
            devida no período em curso:
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            <b>I</b> - o valor da CSLL devida por estimativa em meses anteriores do ano-calendário, seja com base na
            receita bruta e acréscimos ou em balanço ou balancete de redução;
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            <b>II</b> – a CSLL retida na fonte sobre as receitas auferidas no mês, que integraram a respectiva base de cálculo;
            """, size=10, spaceBefore=10),
        
        render.Text(
            """
            <b>III</b> - a CSLL retida na fonte sobre receitas auferidas nos meses anteriores do período em curso, que
            não tenha sido deduzida no pagamento por estimativa daqueles meses. (grifo nosso)
            """, size=10, spaceBefore=10),
    ]

    return elements