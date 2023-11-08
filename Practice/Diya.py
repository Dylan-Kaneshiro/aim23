import gradio as gr

css_path = "aim23/Practice/stylesheet.css"


def chatbot_response(text):
    return text

examples = [
    ['Hello'],
    ['How are you?'],
    ['What is your name?']
]


chatbot = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(),
    outputs=gr.Textbox(),
    examples=examples,
    title="CHATBOT",
    css= "file={css_path}"
)

chatbot.launch()
