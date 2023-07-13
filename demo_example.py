import abc
from abc import abstractmethod

from database import DocumentStoreHolder


class RunParamsBase(abc.ABC):
    pass


class Example(abc.ABC):
    def __init__(self):
        self.document_store_holder = DocumentStoreHolder()

    @abstractmethod
    def run(self, run_params: RunParamsBase):
        pass
