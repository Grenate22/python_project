from fpdf import FPDF
#
pdf=FPDF()
pdf.add_page()
pdf.set_font('Arial','B',size=25)
pdf.cell(0,20, txt='How is feasibility survey different from marketing.',ln=1,align='C')
f=open('feasibility.txt','r')
for x in f:
    print(x)
    pdf.set_font('Arial',size=18)
    pdf.cell(0,10,txt=x,ln=1,)

pdf.set_auto_page_break(auto=True,margin=30)
pdf.set_font('Arial','B',size=20)
pdf.cell(0,20, txt='How does a business plan solve or settle matter here.',ln=1,align='C')
b=open('business.txt','r')
for x in b:
    print(x)
    pdf.set_font('Arial',size=18)
    pdf.cell(0,10,txt=x,ln=1,)
pdf.output('abisola.pdf')