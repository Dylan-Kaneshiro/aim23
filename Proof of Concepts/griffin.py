import gradio as gr
from langchain.document_loaders import PyPDFLoader

def upload_file(file):
    file_path = file.name
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()

    pdfText = ""
    for page in pages:
      pdfText += page.page_content
    return pdfText

with gr.Blocks() as demo:
  upload_button = gr.UploadButton("Upload a PDF file", file_types=["pdf"], file_count="single")
  output = gr.Textbox(label="Text loaded from PDF using PyPDFLoader")
  upload_button.upload(upload_file, upload_button, output)

demo.launch()