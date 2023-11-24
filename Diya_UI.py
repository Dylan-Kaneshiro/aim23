import random
import time
import gradio as gr
from create_query_engine import *

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


def respond(message, chat_history, query_engine, sql_engine):
    response = query_engine.query(message)
    bot_message = response.response  
    chat_history.append((message, bot_message))
    time.sleep(2)
    return "", chat_history, display_question_and_answer(chat_history), query(sql_engine, response.metadata['sql_query']), response.metadata['sql_query']

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

                    
                    SQLidx = gr.State()
                    sql_engine = gr.State()

                    # Connect to database + give context pane
                    with gr.Accordion("Command String Details"):
                        gr.Markdown("Enter command string details here")
                        with gr.Row():
                            user = gr.Textbox(label="Username")
                            password = gr.Textbox(label="Password")
                        with gr.Row():
                            host = gr.Textbox(label="Host")
                            port = gr.Textbox(label="Port")
                            myDB = gr.Textbox(label="mydatabase")
                            upload_status = gr.Textbox(value="Database not connected yet", label="Connect Status")
                        submit_SQL_btn = gr.Button("Submit postgre details")
                    submit_SQL_btn.click(fn=create_query_engine, inputs = [file, user, password, host, port, myDB], outputs=[SQLidx, sql_engine, upload_status])
                    
                    robot = gr.Image(value=robot_filepath, type='pil', show_label=False, show_download_button=False, container=False, width=125, height=125, elem_classes='column_el')
                
                with gr.Column(scale=3, elem_classes='column'):
                    df = gr.Dataframe()
                    chatbot = gr.Chatbot(elem_classes='column_el')
                    msg = gr.Textbox(show_label=False, elem_classes='column_el')
                    with gr.Accordion("Executed SQL Query"):
                        sql_statement = gr.Textbox(label="", lines=5)

    with gr.Tab("Chat History"):
        history = gr.HTML()
        msg.submit(respond, [msg, chatbot, SQLidx, sql_engine], [msg, chatbot, history, df, sql_statement])

demo.launch()
