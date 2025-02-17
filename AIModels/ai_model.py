import AIModels.ModelHelpers.ollama as ollama_interface
import AIModels.ModelHelpers.gemini as gemini_interface
from AIModels.utils import resolve_model_source

from Common.enums import AIModelSources
import configparser
import yaml

class AIModel:
    def __init__(self):
        with open('configs/model.yml') as stream:
            config = yaml.safe_load(stream)

        self.llm_model_source = resolve_model_source(config["llm_source"])
        self.embedding_model_source = resolve_model_source(config["embedding_model_source"])

    def get_embedding_model(self):
        if self.embedding_model_source == AIModelSources.ollama.value:
            return ollama_interface.get_embedding_model()
        
        if self.embedding_model_source == AIModelSources.gemini.value:
            return gemini_interface.get_embedding_model()
    
    def get_llm(self):
        if self.llm_model_source == AIModelSources.ollama.value:
            return ollama_interface.get_llm()
        
        if self.llm_model_source == AIModelSources.gemini.value:
            return gemini_interface.get_llm()


if __name__ == "__main__":
    aim = AIModel()
