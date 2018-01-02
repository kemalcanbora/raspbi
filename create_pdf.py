import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("form_letter.pdf", pagesize=letter,rightMargin=72, leftMargin=72,topMargin=72, bottomMargin=18)

Story = []
logo = "python.png"
issueNum = 12

def create_pdf_page(full_name,address_parts,metin):
    formatted_time = time.ctime()
    # address_parts = ["411 State St.", "Marshalltown, IA 50158"]

    im = Image(logo, 2 * inch, 2 * inch)
    Story.append(im)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=12>%s</font>' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '<font size=12>%s</font>' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))
    for part in address_parts:
        ptext = '<font size=12>%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(Spacer(1, 12))
    # ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
    ptext=" "
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ##paragraf_N
    for i in range(len(metin)):
        #metin
        ptext = '<font size=9>'+str(metin["text"][i])+'</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))
        ##link

        # ptext = '<font size=7>' + str(metin["pdf_link"][i]) + '</font>'

        link_pdf='http://kbora.xyz/'+str(metin.pdf_link[i])
        print(link_pdf)
        ptext = '<link href="' + link_pdf + '">' + link_pdf+ '</link>'

        Story.append(Paragraph(ptext, styles["Code"]))
        Story.append(Spacer(1, 10))


    ##sabit page##
    ##paragraf_3
    ptext = '<font size=9>Thank you very much and we look forward to serving you.</font>'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    ##paragraf_4
    ptext = '<font size=9>Sincerely,</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))

    ptext = '<font size=9>Howard.ai</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)


