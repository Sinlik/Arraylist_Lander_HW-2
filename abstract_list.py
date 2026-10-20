# abstract_list.py
from abc import ABC, abstractmethod


class AbstractList(ABC):
    """The contract every list in this course satisfies."""

    
    @abstractmethod
    def add(self, element):
        pass

    @abstractmethod
    def remove(self, index):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def set(self, index, element):
        pass

    @abstractmethod
    def getIndex(self, element):
        pass

    @abstractmethod
    def size(self):
        pass