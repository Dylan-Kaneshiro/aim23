import sqlalchemy

from langchain.document_loaders import PyPDFLoader

import pandas as pd

from llama_index.objects import (
    SQLTableNodeMapping,
    ObjectIndex,
    SQLTableSchema,
)
from llama_index import SQLDatabase
from llama_index.indices.vector_store.base import VectorStoreIndex
from llama_index.indices.struct_store import SQLTableRetrieverQueryEngine

from dotenv import load_dotenv
load_dotenv()
import os
os.environ['OPENAI_API_KEY'] = os.getenv('API_KEY')

def read_context_pdf(file):
    filepath = file.name
    loader = PyPDFLoader(filepath)
    pages = loader.load()
    content = "".join([page.page_content for page in pages])
    content = [c.lstrip() for c in content.split(";")]
    content = [c.split(":") for c in content]
    return content

def query(engine, sql_query):
    with engine.begin() as conn:
        df = pd.read_sql_query(sqlalchemy.text(sql_query), conn)
    return df

def create_query_engine(context_pdf, username, password, host, port, mydatabase):
    
    # Parse context pdf
    context = read_context_pdf(context_pdf)

    # create sql engine
    pg_uri = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{mydatabase}"
    engine = sqlalchemy.create_engine(pg_uri)
    sql_database = SQLDatabase(engine)

    # create context mapping
    table_node_mapping = SQLTableNodeMapping(sql_database)
    table_schema_objs = [(SQLTableSchema(table_name=c[0], context_str=c[1])) for c in context]

    obj_index = ObjectIndex.from_objects(
        table_schema_objs,
        table_node_mapping,
        VectorStoreIndex,
    )

    query_engine = SQLTableRetrieverQueryEngine(
        sql_database, obj_index.as_retriever(similarity_top_k=3)
    )

    return query_engine, engine, "Connection good"


