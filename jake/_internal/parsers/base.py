from abc import ABC, abstractmethod
from typing import List
from cyclonedx.model.component import Component


class BaseJakeParser(ABC):

    @abstractmethod
    def get_components(self) -> List[Component]:
        pass
