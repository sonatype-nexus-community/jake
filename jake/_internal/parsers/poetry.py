from typing import List
from cyclonedx.model.component import Component, ComponentType
from packageurl import PackageURL  # type: ignore[import-untyped]
from .base import BaseJakeParser

try:
    import tomllib  # type: ignore[import-not-found]
except ImportError:
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ImportError as e:
        raise ImportError('tomli is required on Python < 3.11 for poetry.lock parsing') from e


class PoetryParser(BaseJakeParser):

    def __init__(self, poetry_lock_contents: str) -> None:
        self._content = poetry_lock_contents

    def get_components(self) -> List[Component]:
        data = tomllib.loads(self._content)
        components = []
        for pkg in data.get('package', []):
            name = pkg.get('name', '')
            version = pkg.get('version', '')
            if name and version:
                purl = PackageURL('pypi', None, name.lower().replace('_', '-'), version)
                components.append(Component(
                    type=ComponentType.LIBRARY,
                    name=name,
                    version=version,
                    purl=purl,
                ))
        return components


class PoetryFileParser(BaseJakeParser):

    def __init__(self, poetry_lock_filename: str) -> None:
        self._path = poetry_lock_filename

    def get_components(self) -> List[Component]:
        with open(self._path, 'rb') as f:
            return PoetryParser(f.read().decode('utf-8')).get_components()
