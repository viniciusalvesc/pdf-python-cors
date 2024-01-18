from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Spacer

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors


styles = getSampleStyleSheet()

text_styles = {
    'title': ParagraphStyle(
        'title',
        parent=styles['Title'],
        spaceBefore=18
    ),
    'sub_title': ParagraphStyle(
        'sub_title',
        parent=styles['Heading1'],
        spaceBefore=18
    ),
    'sub_title_2': ParagraphStyle(
        'sub_title_2',
        parent=styles['Heading1'],
        fontSize=14,
        spaceBefore=18
    ),
    'normal': {
        'justify': ParagraphStyle(
            'normal_justify',
            parent=styles['Normal'],
            alignment=TA_JUSTIFY,
            spaceAfter=18
        ),
        'center': ParagraphStyle(
            'normal_center',
            parent=styles['Normal'],
            alignment=TA_CENTER,
            spaceAfter=18
        ),
    },
    'bold': {
        'justify': ParagraphStyle(
            'bold_justify',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            alignment=TA_JUSTIFY,
            spaceBefore=0
        ),
        'center': ParagraphStyle(
            'bold_center',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            alignment=TA_CENTER,
            spaceAfter=18
        ),
    },
    'table_small': 
        ParagraphStyle(
            'table_small',
            parent=styles['Normal'],
            fontSize=7,
            leading=9,
        ),
}

class RenderParagraph():
    def __init__(self) -> None:
        pass

    def Space(self, size=12):
        return Spacer(1, size)

    def get_text_alignment(self, align):
        match (align):
            case 'left':
                return TA_LEFT
            case 'right':
                return TA_RIGHT
            case 'center':
                return TA_CENTER
            case _:
                return TA_JUSTIFY

    def Text(self, text, size=12, leading=None, color=colors.black, bold=False, align='justify', spaceBefore=0, spaceAfter=0):

        textAlign = self.get_text_alignment(align)

        text_style = ParagraphStyle(
            'text_style',
            parent=styles['Normal'],
            fontName='Helvetica-Bold' if bold else 'Helvetica',
            fontSize=size,
            leading=size + 2 if not leading else leading,
            textColor=color,
            alignment=textAlign,
            spaceBefore=spaceBefore,
            spaceAfter=spaceAfter,
        )

        return Paragraph(text, text_style)