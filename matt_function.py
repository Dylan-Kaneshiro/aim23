from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader

from dotenv import load_dotenv
load_dotenv()

import os
os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')



def create_VSI(files, index):   #add vsi and filepaths
    
    pathnames = [file.name for file in files]

    documents = SimpleDirectoryReader(input_files=pathnames).load_data()

    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()

    return query_engine, "Upload complete"
