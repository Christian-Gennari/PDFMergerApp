import tkinter
from tkinter import filedialog as fd

from plyer import filechooser

import PyPDF2
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextFieldRound, MDTextField
from kivy.lang.builder import Builder

pdfSaveFileNameTextInput = """
MDTextField:
    hint_text: "Insert name of new PDF file"
    pos_hint: {'center_x': 0.5, 'center_y': 0.35}
    size_hint_x: None
    width: 200

"""

class PDFMergeApp(MDApp):
    def build(self):
        application_window = Screen()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        label = MDLabel(text="Simple PDF Merger",
                        halign="center",
                        pos_hint={'center_x': 0.5, 'center_y': 0.7},
                        font_style="H3")
        application_window.add_widget(label)

        self.textInput = Builder.load_string(pdfSaveFileNameTextInput)
        application_window.add_widget(self.textInput)

        btn_flat = MDRectangleFlatButton(text="Merge PDFs",
                                         pos_hint={'center_x': 0.5, 'center_y': 0.2}
                                         )
        btn_flat.bind(on_release=self.pressed)
        application_window.add_widget(btn_flat)

        return application_window

    def pressed(self, instance):
        filename = filechooser.open_file(title="Choose pdfs to merge",
                                         multiple=True,
                                         filters=[("PDF Files (.pdf)", "*.pdf")])
        pdfOutputFileDirectory = filechooser.choose_dir()
        pdfOutputFileDirectory = ''.join(pdfOutputFileDirectory)

        pdfOutputFileName = self.textInput.text

        pdfOutputFile = open(pdfOutputFileDirectory + "\\" + pdfOutputFileName + ".pdf",
                             "wb")  # fd.asksaveasfile(mode='wb', defaultextension=".pdf")
        pdfWriter = PyPDF2.PdfFileWriter()

        for x in filename:
            pdfFiles = open(x, "rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFiles)
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
                pdfWriter.write(pdfOutputFile)

        self.textInput.text = ""
        pdfOutputFile.close()


PDFMergeApp().run()
