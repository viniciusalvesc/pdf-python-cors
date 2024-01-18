from reportlab.platypus import PageBreak

from pages.styles.pdf_text import RenderParagraph

render = RenderParagraph()

def efd_intro():
    elements = [
        PageBreak(),
        render.Text('DAS DISPOSIÇÕES LEGAIS', size=18, bold=True, spaceAfter=18),

        render.Text('MANUAL DO SPED EFD-CONTRIBUIÇÕES', size=12, bold=True),
        render.Text('Registro F600: Contribuição Retida na Fonte', size=12, bold=True),

        render.Text(
            """
            Neste registro devem ser informados pela pessoa jurídica beneficiária da retenção/recolhimento os valores
            da contribuição para o PIS/pasep e da Cofins retidos na Fonte, decorrentes de:
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>1</b>. Pagamentos efetuados por órgãos, autarquias e fundações da administração pública federal à pessoa
            jurídica titular da escrituração (art. 64 da Lei nº 9.430/96);
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>2</b>. Pagamentos efetuados por empresas públicas, sociedades de economia mista e demais entidades sob
            o controle direto ou indireto da União, à pessoa jurídica titular da escrituração (art. 34 da Lei nº 10.833/03);
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>3</b>. Pagamentos efetuados por outras pessoas jurídicas de direito privado, pela prestação de serviços
            de limpeza, conservação, manutenção, segurança, vigilância, transporte de valores e locação de mão-de-obra,
            pela prestação de serviços de assessoria creditícia, mercadológica, gestão de crédito, seleção e riscos,
            administração de contas a pagar e a receber, bem como pela remuneração de serviços profissionais, prestados
            pela à pessoa jurídica titular da escrituração (art. 30 da Lei nº 10.833/03);
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>4</b>. Pagamentos efetuados por associações, inclusive entidades sindicais, federações, confederações,
            centrais sindicais e serviços sociais autônomos, sociedades simples, inclusive sociedades cooperativas,
            fundações de direito privado ou condomínios edilícios, pela prestação de serviços de limpeza, conservação,
            manutenção, segurança, vigilância, transporte de valores e locação de mão-de-obra, pela prestação de
            serviços de assessoria creditícia, mercadológica, gestão de crédito, seleção e riscos, administração de
            contas a pagar e a receber, bem como pela remuneração de serviços profissionais, prestados pela à pessoa
            jurídica titular da escrituração (art. 30 da Lei nº 10.833/03);
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>5</b>. Pagamentos efetuados por órgãos, autarquias e fundações da administração pública estadual,
            distrital ou municipal, à pessoa jurídica titular da escrituração (art. 33 da Lei nº 9.430/96);
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>6</b>. Pagamentos efetuados por pessoa jurídica fabricante de veículos e peças, referentes à aquisição
            de autopeças junto à pessoa jurídica titular da escrituração (art. 3º da Lei nº 10.485/02);
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>7</b>. Outras hipóteses de retenção na fonte das referidas contribuições sociais, previstas na legislação tributária.
            """, size=10, spaceBefore=10),

        render.Text(
            """
            Além das hipóteses de retenção na fonte acima especificadas, devem também ser escriturados neste registro os
            valores recolhidos de PIS/Pasep e de Cofins, pelas sociedades cooperativas que se dedicam a vendas em comum,
            referidas no art. 82 da Lei nº 5.764/71, que recebam para comercialização a produção de suas associadas,
            conforme disposto no art. 66 da Lei nº 9.430/96.
            """, size=10, spaceBefore=10),

        render.Text(
            """
            A escrituração no registro F600 dos recolhimentos de PIS/Pasep e de Cofins, efetuados pelas sociedades
            cooperativas nos termos do art. 66 da Lei nº 9.430/96, deve ser efetuada: - Pela pessoa jurídica
            benefíciária do recolhimento (pessoa jurídica associada/cooperada), com base nos valores informados pela
            cooperativa quanto aos valores de PIS/Pasep e Cofins pagos. Neste caso, deve ser informado no Campo 11
            (IND_DEC) o indicador “0”;
            - Pela sociedade cooperativa responsável pelo recolhimento, decorrente da comercialização ou da entrega
            para revenda à central de cooperativas.
            Neste caso, deve ser informado no Campo 11 (IND_DEC) o indicador “1” Os valores efetivamente retidos na
            fonte de PIS/Pasep e de Cofins, escriturados neste registro, são passíveis de dedução da contribuição
            apurada nos Registros M200 (PIS/Pasep) e M600 (Cofins), respectivamente.
            """, size=10, spaceBefore=10),

        PageBreak(),
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
            De acordo com a nova redação do art. 12 da Lei nº 8.218, de 1991, a inobservância do disposto no artigo
            precedente acarretará a imposição das seguintes penalidades:
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>I</b> - multa equivalente a 0,5% (meio por cento) do valor da receita bruta da pessoa jurídica no
            período a que se refere a escrituração aos que não atenderem aos requisitos para a apresentação dos
            registros e respectivos arquivos;
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>II</b> - multa equivalente a 5% (cinco por cento) sobre o valor da operação correspondente, limitada a 1%
            (um por cento) do valor da receita bruta da pessoa jurídica no período a que se refere a escrituração, aos
            que omitirem ou prestarem incorretamente as informações referentes aos registros e respectivos arquivos;
            """, size=10, spaceBefore=10),

        render.Text(
            """
            <b>III</b> - multa equivalente a 0,02% (dois centésimos por cento) por dia de atraso, calculada sobre a
            receita bruta da pessoa jurídica no período a que se refere a escrituração, limitada a 1% (um por cento)
            desta, aos que não cumprirem o prazo estabelecido para apresentação dos registros e respectivos arquivos.
            (grifo nosso)
            """, size=10, spaceBefore=10),

        render.Text(
            """
            SOLUÇÃO DE CONSULTA Nº 224 – COSIT 4 DE DEZEMBRO DE 2018 ASSUNTO
            """, size=12, bold=True, spaceBefore=22, spaceAfter=5),
        render.Text(
            """
            Contribuição para o PIS/Pasep Os valores retidos na fonte a título de Contribuição para o PIS/Pasep somente
            podem ser deduzidos com o que for devido em relação à mesma contribuição e no mês de apuração a que se
            refere a retenção. O saldo por ventura existente referente ao montante retido que exceder o valor da
            respectiva contribuição a pagar no mesmo mês de apuração, poderá ser restituído ou compensado com débitos
            relativos a tributos administrados pela Secretaria da Receita Federal do Brasil, inclusive a própria
            Contribuição para o PIS/Pasep. Dispositivos Legais: Lei nº 11.727, de 2008, art. 5º; Instrução Normativa
            RFB nº 1.234, de 2012, art. 9º.
            """, size=10),

        render.Text(
            """
            CONTRIBUIÇÃO PARA O FINANCIAMENTO DA SEGURIDADE SOCIAL - COFINS
            """, size=12, bold=True, spaceBefore=22, spaceAfter=5),
        render.Text(
            """
            Os valores retidos na fonte a título de Cofins somente podem ser deduzidos com o que for devido em relação à
            mesma contribuição e no mês de apuração a que se refere a retenção. O saldo por ventura existente referente
            ao montante retido que exceder o valor da respectiva contribuição a pagar no mesmo mês de apuração, poderá
            ser restituído ou compensado com débitos relativos a tributos administrados pela Secretaria da Receita
            Federal do Brasil, inclusive a própria Cofins. Dispositivos Legais: Lei nº 11.727, de 2008, art. 5º;
            Instrução Normativa RFB nº 1.234, de 2012, art. 9º.(grifo nosso)
            """, size=10),
        
    ]

    return elements