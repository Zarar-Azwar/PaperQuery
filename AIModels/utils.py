from Common.enums import AIModelSources

def resolve_model_source(model_source_str):
    if model_source_str == "ollama":
        return AIModelSources.ollama.value

    if model_source_str == "gemini":
        return AIModelSources.gemini.value