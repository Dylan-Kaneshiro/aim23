import os
from sqlalchemy import create_engine, MetaData
from llama_index import LLMPredictor, ServiceContext, SQLDatabase, VectorStoreIndex
from llama_index.indices.struct_store import SQLTableRetrieverQueryEngine
from llama_index.objects import SQLTableNodeMapping, ObjectIndex, SQLTableSchema
from langchain import OpenAI

def create_obj_idx(user, password, host, port, myDB, SQLidx):
    cxn_key = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{myDB}"
    engine = create_engine(cxn_key)

    # load all table definitions
    metadata_obj = MetaData()
    metadata_obj.reflect(engine)

    sql_database = SQLDatabase(engine)

    table_node_mapping = SQLTableNodeMapping(sql_database)

    table_schema_objs = []
    for table_name in metadata_obj.tables.keys():
        table_schema_objs.append(SQLTableSchema(table_name=table_name))

    # We dump the table schema information into a vector index. The vector index is stored within the context builder for future use.
    obj_index = ObjectIndex.from_objects(
        table_schema_objs,
        table_node_mapping,
        VectorStoreIndex,
    )

    SQLidx = SQLTableRetrieverQueryEngine(
        sql_database,
        obj_index.as_retriever(similarity_top_k=1),
        service_context=service_context,
    )
    
    return SQLidx


