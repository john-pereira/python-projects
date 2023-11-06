from fpdf import FPDF
import pandas as pd

# orientation portrait, unit mm
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set Header
    pdf.set_font(family="Times", size=24 )
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # Set Footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=12 )
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="C")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=12 )
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="C")

pdf.output("output.pdf")
