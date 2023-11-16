from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from dotenv import load_dotenv
load_dotenv()

# Import OpenAI as main LLM service
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

# Import PDF document loaders...there's other ones as well!
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator

import os

os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')



def create_VSI(files, index):   #add vsi and filepaths
    
    pathnames = [file.name for file in files]

    loaders = []
    for pdf in pathnames:
        loader = PyPDFLoader(pdf)
        loaders.append(loader)

    index = VectorstoreIndexCreator().from_loaders(loaders)

    return index
