import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from utils.config_loaders import load_config


class ModelLoader:
    """
    A utility class to load embedding models and LLM models.
    """
    def __init__(self):
        load_dotenv()
        self.config= load_config()
        self._validate_env()
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        

    def _validate_env(self):
        """
        Validate necessary environment variables.
        """    
        required_variables = ['GROQ_API_KEY',"HF_TOKEN"]
        missing_vars=[ var for var in required_variables if not os.getenv(var)]

        if missing_vars:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
    def load_embedding(self):
        """
        Load and return the embedding model.
        """    
        print("Loading Embedding model")
        embedding_model_name = self.config["embeddings_model"]["model_name"]

        return HuggingFaceEmbeddings(model=embedding_model_name)
    
    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        llm_model_name = self.config["llm"]["model_name"]
        temperature = self.config["llm"]["temperature"]

        return ChatGroq(model=llm_model_name, api_key=self.groq_api_key, temperature=temperature)