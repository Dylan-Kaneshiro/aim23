import random
import time
import gradio as gr

app_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
logo_filepath = 'logo_image.jpg'
robot_filepath = 'robot_image.png'

custom_css = """
.column {
  align-items: center;
}

.column_el {
  flex-grow: 1;
}
"""

def respond(message, chat_history):
  bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
  chat_history.append((message, bot_message))
  time.sleep(2)
  return "", chat_history

with gr.Blocks(css=custom_css) as demo:
  with gr.Row(variant='compact'):
    with gr.Column(scale=1, elem_classes='column'):
      logo = gr.Image(value=logo_filepath, type='filepath', show_label=False, show_download_button=False, container=False, width=75, height=75, elem_classes='column_el')
      file = gr.File(file_types=['pdf'], file_count='multiple', show_label=False, elem_classes='column_el', height=75)
      description = gr.Textbox(value=app_description, show_label=False, elem_classes='column_el', )
      submit_button = gr.Button(value='Submit', elem_classes='column_el')
      robot = gr.Image(value=robot_filepath, type='filepath', show_label=False, show_download_button=False, container=False, width=125, height=125, elem_classes='column_el')
    with gr.Column(scale=3, elem_classes='column'):
      chatbot = gr.Chatbot(elem_classes='column_el')
      msg = gr.Textbox(show_label=False, elem_classes='column_el')
      msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()