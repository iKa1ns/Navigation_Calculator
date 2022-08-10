from fpdf import FPDF
import parse

def do_a_pdf(air1, air2, hdg):
    headings = ['WPT','FREQ','HDG', 'DIST', 'X', 'Y', 'COORDS', 'NAME']
    rows = parse.arr_of_wpt(air1, air2, hdg)
    
    col_widths=(16, 15, 13, 13, 13, 13, 55, 52)
    pdf = FPDF()
    pdf.set_font("helvetica", size=10)
    pdf.add_page()
    pdf.set_line_width(0.0)
    pdf.rect(5.0, 5.0, 200.0,287.0)

    pdf.set_xy(0.0,2.0)
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(220, 50, 50)
    pdf.cell(w=210.0, h=16, align='C', txt="Navigation calculator", border=0)

    pdf.set_xy(0.0,10.0)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(w=210.0, h=10.0, align='C', txt='Plan may be used only in PC flight simulators - NOT FOR REAL WORLD NAVIGATION', border=0)

    pdf.set_line_width(0.0)
    pdf.line(10, 17, 200, 17)

    pdf.set_xy(10.0, 20.0)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(w=210.0, h=8.0, align='L', txt=f'Computed flight plan from {air1.upper()} to {air2.upper()}', border=0)
    
    pdf.set_fill_color(255, 100, 0)
    pdf.set_text_color(255)
    pdf.set_draw_color(255, 0, 0)
    pdf.set_line_width(0.3)
    pdf.set_font(style="B")

    pdf.set_y(30)
    for col_width, heading in zip(col_widths, headings):
        pdf.cell(col_width, 7, heading, border=1, align="C", fill=True)
    pdf.ln()
    
    pdf.set_fill_color(224, 235, 255)
    pdf.set_text_color(0)
    pdf.set_font()
    fill = False
    for row in rows:
        pdf.cell(col_widths[0], 6, row[0], border="LR", align="C", fill=fill)
        pdf.cell(col_widths[1], 6, row[1], border="LR", align="C", fill=fill)
        pdf.cell(col_widths[2], 6, row[2], border="LR", align="C", fill=fill)
        pdf.cell(col_widths[3], 6, row[3], border="LR", align="C", fill=fill)
        pdf.cell(col_widths[4], 6, row[4], border="LR", align="C", fill=fill)
        pdf.cell(col_widths[5], 6, row[5], border="LR", align="C", fill=fill)
        pdf.cell(col_widths[6], 6, row[6]+' '+row[7], border="LR", align="C", fill=fill)
        pdf.cell(col_widths[7], 6, row[8], border="LR", align="C", fill=fill)
        pdf.ln()
        fill = not fill
    pdf.cell(sum(col_widths), 0, "", "T")
    pdf.output("route.pdf")

