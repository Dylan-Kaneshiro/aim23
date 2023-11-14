def create_VSI(pdf_paths, index):   #add vsi and filepaths
    from langchain.llms import OpenAI
    from langchain.document_loaders import PyPDFLoader
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import Chroma

    from dotenv import load_dotenv
    load_dotenv()



    import os
    os.environ['OPENAI_API_KEY'] = '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'

    # Import OpenAI as main LLM service
    from langchain.llms import OpenAI
    from langchain.embeddings import OpenAIEmbeddings

    # Import PDF document loaders...there's other ones as well!
    from langchain.document_loaders import PyPDFLoader
    from langchain.indexes import VectorstoreIndexCreator

    # pdf_paths = ['sample_financial_report.pdf', 'sample_financial_report_2.pdf']

    loaders = []
    for pdf in pdf_paths:
        loader = PyPDFLoader(pdf)
        loaders.append(loader)

    index = VectorstoreIndexCreator().from_loaders(loaders)

    llm = OpenAI(temperature=0.1, verbose=True)
    embeddings = OpenAIEmbeddings()
    return index

    
    # Import vector store stuff
    #from langchain.agents.agent_toolkits import (
    #    create_vectorstore_agent,
    #    VectorStoreToolkit,
    #    VectorStoreInfo
    #)

    # set APIKey for OpenAI service
    #os.environ['OPENAI_API_KEY'] = os.getenv("API_KEY")

    # Create instance of OpenAI LLM

    '''

    #for file upload
    file_path = uploaded_file.name
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()

    #for file storage
    newFileName = name.replace(" ", "_")
    store = Chroma.from_documents(pages, embeddings, collection_name= newFileName)
    
    # Create vectorstore info object - metadata repo?
    vectorstore_info = VectorStoreInfo(
        name=name,
        description=description,
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

    return agent_executor
    '''

