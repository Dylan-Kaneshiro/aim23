import random
import time
import gradio as gr
from matt_function import *


logo_filepath = 'Practice/images/logo_image.png'
robot_filepath = 'Practice/images/robot_image.png'

custom_css = """
.column {
  align-items: center;
}

.column_el {
  flex-grow: 1;
}
"""

def respond(message, chat_history, agent):
  bot_message = agent.run(message)
  chat_history.append((message, bot_message))
  time.sleep(2)
  return "", chat_history, display_question_and_answer(chat_history)

def display_question_and_answer(tuple_list):
    qa_history = ""
    for i, (q, a) in enumerate(tuple_list):
        qa_history += f"<details><summary>Q: {q}</summary><p>A: {a}</p></details>"
    return qa_history

with gr.Blocks(css=custom_css) as demo:
  with gr.Tab("Home"):  
    with gr.Row(variant='compact'):
      with gr.Column(scale=1, elem_classes='column'):
        logo = gr.Image(value=logo_filepath, type='filepath', show_label=False, show_download_button=False, container=False, width=75, height=175, elem_classes='column_el')
        
        agent = gr.State()
        file = gr.File(file_types=['pdf'], file_count='single', show_label=False, elem_classes='column_el', height=75)
        name = gr.Textbox(label="Name", elem_classes='column_el')
        description = gr.Textbox(label="Description", elem_classes='column_el')
        create_agent_btn = gr.Button(value='Submit', elem_classes='column_el')
        create_agent_btn.click(fn=create_agent, inputs = [name, description, file, agent], outputs = agent)

        robot = gr.Image(value=robot_filepath, type='filepath', show_label=False, show_download_button=False, container=False, width=125, height=125, elem_classes='column_el')
      with gr.Column(scale=3, elem_classes='column'):
        chatbot = gr.Chatbot(elem_classes='column_el')
        msg = gr.Textbox(show_label=False, elem_classes='column_el')
        
  with gr.Tab("Chat History"):
    history = gr.HTML()

  msg.submit(respond, [msg, chatbot, agent], [msg, chatbot, history])
    

demo.launch()