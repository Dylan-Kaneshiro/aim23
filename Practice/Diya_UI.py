import random
import time
import gradio as gr
from cheri_function import *

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


def respond(message, chat_history, query_engine):
    response = query_engine.query(message)
    bot_message = f"Response to: {message}"  
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
                    logo = gr.Image(value=logo_filepath, type='pil', show_label=False, show_download_button=False, container=False, width=75, height=175, elem_classes='column_el')
                    agent = gr.State()
                    file = gr.File(file_types=['pdf'], file_count='single', show_label=False, elem_classes='column_el', height=75)
                    # create_agent_btn = gr.Button(value='Submit', elem_classes='column_el')
                    # create_agent_btn.click(fn=lambda: None)  # Placeholder click function
                    
                    SQLidx = gr.State()

                    # Use gr.Accordion() for SQL query
                    with gr.Accordion("Command String Details"):
                        gr.Markdown("Enter command string details here")
                        with gr.Row():
                            user = gr.Textbox(label="Username")
                            password = gr.Textbox(label="Password")
                        with gr.Row():
                            host = gr.Textbox(label="Host")
                            port = gr.Textbox(label="Port")
                            myDB = gr.Textbox(label="mydatabase")
                        submit_SQL_btn = gr.Button("Submit postgre details")
                    submit_SQL_btn.click(fn=create_obj_idx, inputs = [user, password, host, port, myDB, SQLidx], outputs=SQLidx)
                    
                    robot = gr.Image(value=robot_filepath, type='pil', show_label=False, show_download_button=False, container=False, width=125, height=125, elem_classes='column_el')
                
                with gr.Column(scale=3, elem_classes='column'):
                    gr.Dataframe(scale=5)
                    chatbot = gr.Chatbot(elem_classes='column_el')
                    msg = gr.Textbox(show_label=False, elem_classes='column_el')

    with gr.Tab("Chat History"):
        history = gr.HTML()
        msg.submit(respond, [msg, chatbot, SQLidx], [msg, chatbot, history])

demo.launch()
