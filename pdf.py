# Python program to create
# a pdf file


from re import X
from this import s
from fpdf import FPDF

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
pdf.y = 24

pdf.set_font("OpenSansBold", size = 10)
pdf.cell(90, 4.5, txt = "90", border = 0, ln = 1, align = 'C')


pdf.set_font("OpenSansLight", size = 8)
pdf.set_text_color(r=138, g=149, b=156)
pdf.cell(90, 4.5, txt = "80", border = 0, ln = 2, align = 'C')
# pdf.cell(90, 3, txt = "", border = 1, ln = 2, align = 'C')

pdf.set_fill_color(r=138, g=149, b=156)
pdf.rect(x=5.5, y=36, w=94, h=23.5, style="F")

pdf.set_fill_color(r=210, g=10, b=16)
pdf.rect(x=38.7, y=36, w=27.2, h=23.5, style="F")


pdf.set_fill_color(r=57, g=74, b=89)
pdf.rect(x=5.5, y=47.5, w=94, h=12, style="F")

pdf.set_fill_color(r=134, g=16, b=1)
pdf.rect(x=38.7, y=47.5, w=27.2, h=12, style="F")

print(pdf.y)
pdf.y = 38.5
top = 38.5


offset = pdf.x + 31.5
pdf.set_font("OpenSans", size = 8)
pdf.set_text_color(r=255, g=255, b=255)
pdf.multi_cell(31.5, 3, txt = "90 \n dalsi radek", border = 0, align = 'C')

pdf.y=top
pdf.x = offset
pdf.multi_cell(27, 3, txt = "90 \n dalsi radek", border = 0, align = 'C')

pdf.y=top
pdf.x = offset+27
pdf.multi_cell(31.5, 3, txt = "90 \n dalsi radek", border = 0, align = 'C')


# save the pdf with name .pdf
pdf.output("GFG.pdf")
