#pip install langchain chromadb openai tiktoken
#pip install -q gradio

import gradio as gr
import os
from langchain.embeddings import OpenAIEmbeddings

# Import vector store stuff
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)
# Import chroma as the vector store
from langchain.vectorstores import Chroma


os.environ['OPENAI_API_KEY'] ='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'
embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_texts

with gr.Blocks() as demo:
  nameState = gr.State([])
  descState = gr.State([])

  with gr.Row():
    grName = gr.Textbox(label="Enter name:")
    grDesc = gr.Textbox(label="Enter description:")
  output_box = gr.Textbox(label="Name history:", value = "None yet!")
  btn = gr.Button("Submit")

  # you know i don't really know how state works or if it's working
  # but i'm going to trust that it is
  def save(name, nameArr, desc, descArr):
    nameArr.append(name)
    descArr.append(name)
    
    nameOut = ", ".join(name for name in nameArr)
    return {grName: name, grDesc: desc, nameState: nameArr, output_box: nameOut}

  btn.click(fn = save,
            inputs=[grName, nameState, grDesc, descState],
            outputs = [grName, nameState, grDesc, descState, output_box])

  name = grName.value
  desc = grDesc.value
  store = Chroma("langchain_store", embeddings)

# Create vectorstore info object
vectorstore_info = VectorStoreInfo(
    name=name,
    description=desc,
    vectorstore=store
)

demo.launch()
