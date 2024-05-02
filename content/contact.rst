    def parse(self, path: Path, source: Path, dest: Path):
        content = Content.load(self.read(path))
