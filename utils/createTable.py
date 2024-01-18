from reportlab.platypus import Table, TableStyle, PageBreak
from reportlab.lib import colors

from pages.styles.pdf_text import RenderParagraph

from utils.formatStatus import formatStatus
from utils.formatCurrency import formatCurrency

render = RenderParagraph()

def create_table(data_report, template):
    # [ ] TODO: Remover print ao finalizar as alterações
    print('report_size: ', len(data_report))

    # Conteudo da primeira linha da tabela
    table_title = [f"LISTA DE OCORRÊNCIAS - {template.upper()}"]

    # Conteudo da segunda linha da tabela
    table_headers = ["Registro", "Status", "Qtd.", "Tipo", "Valor"]

    # Lista de linhas da tabela
    table_data = [
        table_title,
        table_headers
    ]

    if len(data_report) > 0:
        # Preparando dados das linhas e adicionando a lista
        for item in data_report:
            row_data = [
                render.Text(item.get("register_id", ""), size=7),
                render.Text(formatStatus(item.get("status", "")), size=7),
                render.Text(str(item.get("hit_count", "")), size=7),
                render.Text(item.get("message", ""), size=7),
                render.Text(formatCurrency(item.get("value", "")), size=7),
            ]
            table_data.append(row_data)

        # Criando lista de cores alternadas para as linhas
        row_colors = [colors.white, colors.gainsboro]

        # Criando a tabela
        table = Table(table_data, repeatRows=2, colWidths=[100, 80, 50, 220, 80])

        # Aplicando estilo ao titulo e cabeçalho da tabela ( primeira e segunda linha )
        table_style = [
            # Estilo para a primeira linha (fundo azul e letras brancas)
            ('BACKGROUND', (0, 0), (-1, 0), colors.midnightblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            # Estilo para a segunda linha (fundo cinza e letras brancas)
            ('BACKGROUND', (0, 1), (-1, 1), colors.steelblue),
            ('TEXTCOLOR', (0, 1), (-1, 1), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, 1), 3),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]

        # Formatando as linhas dos registros intercalando as cores do background ( branco e cinza )
        for i in range(2, len(table_data)):
            table_style.extend([
                ('BACKGROUND', (0, i), (-1, i), row_colors[i % 2]),
                ('VALIGN', (0, i), (-1, i), 'MIDDLE'),
            ])

        # Mesclando as células da primeira linha
        table_style.append(('SPAN', (0, 0), (-1, 0)))

        # Aplicando estilos
        table.setStyle(TableStyle(table_style))

        # Elementos a serem retornados
        elements = [
            PageBreak(),
            table
        ]

        return elements
    else:
        return []
