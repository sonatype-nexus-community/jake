import re
from typing import List
from cyclonedx.model.component import Component, ComponentType
from packageurl import PackageURL  # type: ignore[import-untyped]
from .base import BaseJakeParser

_PIN_RE = re.compile(r'^([A-Za-z0-9_.-]+(?:\[.*?\])?)[ \t]*==[ \t]*([^\s;#,]+)')


class RequirementsParser(BaseJakeParser):

    def __init__(self, requirements_content: str) -> None:
        self._content = requirements_content

    def get_components(self) -> List[Component]:
        components = []
        for line in self._content.splitlines():
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('-'):
                continue
            m = _PIN_RE.match(line)
            if m:
                name = m.group(1).split('[')[0]
                version = m.group(2)
                purl = PackageURL('pypi', None, name.lower().replace('_', '-'), version)
                components.append(Component(
                    type=ComponentType.LIBRARY,
                    name=name,
                    version=version,
                    purl=purl,
                ))
        return components


class RequirementsFileParser(BaseJakeParser):

    def __init__(self, requirements_file: str) -> None:
        self._path = requirements_file

    def get_components(self) -> List[Component]:
        with open(self._path, encoding='utf-8') as f:
            return RequirementsParser(f.read()).get_components()
