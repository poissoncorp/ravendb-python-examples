from typing import Optional, List

from ravendb import DocumentStore


class DocumentStoreHolder:
    __document_store:Optional[DocumentStore] = None

    @classmethod
    def document_store(cls, urls: Optional[List[str]]) -> DocumentStore:
        if cls.__document_store is None:
            cls.__document_store = DocumentStore(urls)
            cls.__document_store.initialize()
        return cls.__document_store

