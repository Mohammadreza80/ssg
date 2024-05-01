from typing import List
from pathlib import Path
import shutil


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path: Path, dest: Path, content: str, ext=".html"):
        """
        Writes content to a file with the specified extension.

        Args:
            path (Path): Path to the original file (for reference).
            dest (Path): Destination directory for the new file.
            content (str): Content to be written to the file.
            ext (str, optional): File extension. Defaults to ".html".
        """

        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        super().copy(path, source, dest)