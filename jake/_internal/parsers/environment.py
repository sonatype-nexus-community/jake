import importlib.metadata
from typing import List
from cyclonedx.model.component import Component, ComponentType
from packageurl import PackageURL  # type: ignore[import-untyped]
from .base import BaseJakeParser


class EnvironmentParser(BaseJakeParser):

    def get_components(self) -> List[Component]:
        components = []
        seen: set = set()
        for dist in importlib.metadata.distributions():
            name = dist.metadata.get('Name')
            version = dist.metadata.get('Version')
            if not name or not version:
                continue
            key = name.lower()
            if key in seen:
                continue
            seen.add(key)
            purl = PackageURL('pypi', None, key.replace('_', '-'), version)
            components.append(Component(
                type=ComponentType.LIBRARY,
                name=name,
                version=version,
                purl=purl,
            ))
        return components
