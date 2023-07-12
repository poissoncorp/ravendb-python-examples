from typing import Optional, List

from ravendb import DocumentStore


class DocumentStoreHolder:
    __urls: List[str] = ["http://127.0.0.1:8080"]
    __database_name = "DemoPython"
    __document_store: Optional[DocumentStore] = None

    @classmethod
    def store(cls) -> DocumentStore:
        if cls.__document_store is None:
            cls.__document_store = DocumentStore(cls.__urls, cls.__database_name)
            cls.__document_store.initialize()
        return cls.__document_store
