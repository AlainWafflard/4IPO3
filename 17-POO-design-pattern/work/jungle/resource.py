from jungle_element import JungleElement
from abc import ABC, abstractmethod


class Resource(JungleElement, ABC):
    _instance = None

    @classmethod
    def singleton(cls, position=0):
        if cls._instance is None:
            # If instance does not exist, then create it
            cls._instance = cls(position)
        # return the instance
        return cls._instance

    # def __init__(self):
    #     # If instance already exists, then exception
    #     if self.__instance is not None:
    #         raise Exception("This class is a singleton!")
