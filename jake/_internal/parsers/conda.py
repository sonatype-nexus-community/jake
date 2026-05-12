import json
import re
from typing import List
from cyclonedx.model.component import Component, ComponentType
from packageurl import PackageURL  # type: ignore[import-untyped]
from .base import BaseJakeParser

_EXT_RE = re.compile(r'\.(tar\.bz2|conda)$')


class CondaListExplicitParser(BaseJakeParser):

    def __init__(self, conda_data: str) -> None:
        self._content = conda_data

    def get_components(self) -> List[Component]:
        components = []
        for line in self._content.splitlines():
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('@'):
                continue
            basename = line.split('/')[-1]
            basename = _EXT_RE.sub('', basename)
            parts = basename.split('-')
            if len(parts) >= 2:
                name, version = parts[0], parts[1]
                purl = PackageURL('conda', None, name.lower(), version)
                components.append(Component(
                    type=ComponentType.LIBRARY,
                    name=name,
                    version=version,
                    purl=purl,
                ))
        return components


class CondaListJsonParser(BaseJakeParser):

    def __init__(self, conda_data: str) -> None:
        self._content = conda_data

    def get_components(self) -> List[Component]:
        data = json.loads(self._content)
        components = []
        for pkg in data:
            name = pkg.get('name', '')
            version = pkg.get('version', '')
            if name and version:
                purl = PackageURL('conda', None, name.lower(), version)
                components.append(Component(
                    type=ComponentType.LIBRARY,
                    name=name,
                    version=version,
                    purl=purl,
                ))
        return components
