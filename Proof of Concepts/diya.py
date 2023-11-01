import gradio as gr

def echo(message, history):
    return message


demo = gr.Interface(fn=echo, inputs=gr.Textbox(),
    outputs=gr.Textbox(), title="CHATBOT")
demo.launch()