# Python program to create
# a pdf file

from re import X
from this import s
from fpdf import FPDF

class Card:
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF("L", "mm", (65, 105))
    pdf.set_margins(left=7.5, top=7.5, right=7.5)
    pdf.set_auto_page_break(auto=False, margin=0)
    # Add a page
    pdf.add_page()

    pdf.add_font('OpenSans', '', 'OpenSans-Regular.ttf', uni=True)
    pdf.add_font('OpenSansBold', '', 'OpenSans-Bold.ttf', uni=True)
    pdf.add_font('OpenSansLight', '', 'OpenSans-Light.ttf', uni=True)
    # set style and size of font
    # that you want in the pdf

    def writeName(self):
        self.pdf.y = 24
        self.pdf.set_text_color(r=0, g=0, b=0)
        self.pdf.set_font("OpenSansBold", size=10)
        self.pdf.cell(90, 4.5, txt="Jmeno", border=0, ln=1, align='C')

    def writeFunc(self):
        self.pdf.y = 28.5
        self.pdf.set_text_color(r=138, g=149, b=156)
        self.pdf.set_font("OpenSansLight", size=8)
        self.pdf.cell(90, 4.5, txt="Funkce", border=0, ln=2, align='C')

    def loadFonts(self):
        self.pdf.add_font('OpenSans', '', 'OpenSans-Regular.ttf', uni=True)
        self.pdf.add_font('OpenSansBold', '', 'OpenSans-Bold.ttf', uni=True)
        self.pdf.add_font('OpenSansLight', '', 'OpenSans-Light.ttf', uni=True)
    
    def buildBackground(self):
        self.pdf.set_fill_color(r=138, g=149, b=156)
        self.pdf.rect(x=5.5, y=36, w=94, h=23.5, style="F")

        self.pdf.set_fill_color(r=210, g=10, b=16)
        self.pdf.rect(x=38.7, y=36, w=27.2, h=23.5, style="F")

        self.pdf.set_fill_color(r=57, g=74, b=89)
        self.pdf.rect(x=5.5, y=47.5, w=94, h=12, style="F")

        self.pdf.set_fill_color(r=134, g=16, b=1)
        self.pdf.rect(x=38.7, y=47.5, w=27.2, h=12, style="F")

    def writeBlock(self, offset, width, line1, line2):
        self.pdf.y = 38.5
        self.pdf.x = offset + 7.5
        self.pdf.set_font("OpenSans", size=8)
        self.pdf.set_text_color(r=255, g=255, b=255)
        print(line1 + "\n" + line2)
        self.pdf.multi_cell(width, 3, txt=line1 + "\n" + line2, border=0, align='C')

    def printCard(self):
        self.loadFonts()
        self.writeName()
        self.writeFunc()
        self.buildBackground()
        self.writeBlock(0, 31.5, "Ahoj", "Dajo")
        self.writeBlock(31.5, 27, "Ahoj", "Druhy")
        self.writeBlock(58.5, 31.5, "Ahoj", "Treti")
        self.pdf.output("GFG.pdf")

card = Card()
#card.writeBlock(0, 31.5, "Ahoj", "Svete")
card.printCard()