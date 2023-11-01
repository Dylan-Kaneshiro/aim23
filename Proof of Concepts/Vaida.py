#!pip install -q gradio
#!pip install langchain openai pypdf chromadb tiktoken


import gradio as gr



## I tried making a session state of objects but not sure how effectively it is working.
## It works with __init__ method, but when I try returning something or try using a non-constructor the program breaks.
## might work with more experimentations. 

# Define a custom class for objects with a 'name' attribute
class ObjectWithName:
    def __init__(self, name):
        self.name = name
        
with gr.Blocks() as demo:
    NamesList = gr.State([])

    with gr.Row():
        name_input = gr.Textbox(label="Enter Name:")
    output_box = gr.Textbox(label="Names:", value="Name1, Name2, ...")
    btn = gr.Button("Submit")

    def session_state(name, names_list):
        new_object = ObjectWithName(name)
        names_list.append(new_object)
        
        names = ", ".join(obj.name for obj in names_list)
        return {name_input: "", NamesList: names_list, output_box: names}

    btn.click(fn=session_state,
              inputs=[name_input, NamesList],
              outputs=[name_input, NamesList, output_box])



demo.launch()