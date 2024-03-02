from abc import ABC, abstractmethod


class ProactivePlugin(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def invoke(self, event):
        pass
