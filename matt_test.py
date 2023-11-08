import gradio as gr
from matt_function import *

def talk(agent, prompt):
    return agent.run(prompt)

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            name = gr.Textbox(label="Name")
            description = gr.Textbox(label="Description")
            uploaded_file = gr.File()
            agent = gr.State()
            create_agent_btn = gr.Button("Create Agent")
            # use create_agent_btn.click() to apply ur function to name, description, uploaded file, agent as inputs and agent as output
            create_agent_btn.click(fn=create_agent, inputs = [name, description, uploaded_file, agent], outputs = agent)
        with gr.Column():
            prompt = gr.Textbox(label="prompt")
            output = gr.Textbox(label="output")
            prompt_btn = gr.Button("Submit Prompt")
            prompt_btn.click(talk, 
                             inputs=[agent, prompt],
                             outputs=[output])

demo.launch()