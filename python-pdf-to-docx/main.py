from pdf2docx import Converter
import PySimpleGUI as sg

# Create the GUI layout
layout = [
    [sg.Text('Select PDF file:'), sg.Input(key='-FILE-', enable_events=True), sg.FileBrowse()],
    [sg.Button('Convert to DOCX'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('PDF to DOCX Converter', layout)

# Event loop
while True:
    event, values = window.read()

    # Exit if the window is closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    # Convert the PDF to DOCX if the 'Convert to DOCX' button is clicked
    if event == 'Convert to DOCX':
        pdf_file_path = values['-FILE-']
        doc_file_path = pdf_file_path.replace('.pdf', '.docx')

        try:
            cv = Converter(pdf_file_path)
            cv.convert(doc_file_path)
            cv.close()

            sg.popup('Conversion complete!', 'DOCX file saved as: {}'.format(doc_file_path))
        except Exception as e:
            sg.popup('Error during conversion:', str(e))

# Close the window
window.close()
