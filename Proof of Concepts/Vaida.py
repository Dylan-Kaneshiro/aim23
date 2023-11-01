#!pip install -q gradio
#!pip install langchain openai pypdf chromadb tiktoken

# Import os to set API key
import os
import gradio as gr
# Import OpenAI as main LLM service
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

# Import chroma as the vector store
from langchain.vectorstores import Chroma

# Import vector store stuffSS
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

# Set APIkey for OpenAI Service
# Can sub this out for other LLM providers
os.environ['OPENAI_API_KEY'] = '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'

# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.1, verbose=True)
embeddings = OpenAIEmbeddings()


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


# Create vectorstore info object - metadata repo?
vectorstore_info = VectorStoreInfo(
    name="",
    description = "An object that returns name.",
    vectorstore=store
)

# Convert the document store into a langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# Add the toolkit to an end-to-end LC
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

demo.launch()