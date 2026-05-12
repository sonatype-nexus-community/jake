import json
from typing import List
from cyclonedx.model.component import Component, ComponentType
from packageurl import PackageURL  # type: ignore[import-untyped]
from .base import BaseJakeParser


class PipenvParser(BaseJakeParser):

    def __init__(self, pipenv_contents: str) -> None:
        self._content = pipenv_contents

    def get_components(self) -> List[Component]:
        data = json.loads(self._content)
        components = []
        for section in ('default', 'develop'):
            for name, info in data.get(section, {}).items():
                if not isinstance(info, dict):
                    continue
                version = info.get('version', '').lstrip('=')
                if version:
                    purl = PackageURL('pypi', None, name.lower().replace('_', '-'), version)
                    components.append(Component(
                        type=ComponentType.LIBRARY,
                        name=name,
                        version=version,
                        purl=purl,
                    ))
        return components


class PipenvFileParser(BaseJakeParser):

    def __init__(self, pipenv_lock_filename: str) -> None:
        self._path = pipenv_lock_filename

    def get_components(self) -> List[Component]:
        with open(self._path, encoding='utf-8') as f:
            return PipenvParser(f.read()).get_components()
