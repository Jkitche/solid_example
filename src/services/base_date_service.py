from abc import ABC, abstractmethod
from datetime import datetime


class BaseDateService(ABC):
    @abstractmethod
    def get_now(self) -> datetime:
        raise NotImplementedError("Not Implemented!")
