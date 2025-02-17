import glob
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import PDFMinerLoader

class MultiDocumentLoader:
    def __init__(self, directory_path: str, glob_pattern: str = "*.pdf", mode: str = "single"):
        """
        Initialize the loader with a directory path and a glob pattern.
        :param directory_path: Path to the directory containing files to load.
        :param glob_pattern: Glob pattern to match files within the directory.
        :param mode: Mode to use with UnstructuredFileLoader ('single', 'elements', or 'paged').
        """
        self.directory_path = directory_path
        self.glob_pattern = glob_pattern
        self.mode = mode

    def load(self) -> List[Document]:
        """
        Load all files matching the glob pattern in the directory using UnstructuredFileLoader.
        :return: List of Document objects loaded from the files.
        """
        documents = []
        # Construct the full glob pattern
        full_glob_pattern = f"{self.directory_path}/{self.glob_pattern}"
        # Iterate over all files matched by the glob pattern
        for file_path in glob.glob(full_glob_pattern):
            # Use UnstructuredFileLoader to load each file
            loader = PDFMinerLoader(file_path=file_path)
            docs = loader.load()

            print(docs)

            documents.extend(docs)
        return documents


if __name__ == "__main__":
    mdl = MultiDocumentLoader("Papers")
    mdl.load()