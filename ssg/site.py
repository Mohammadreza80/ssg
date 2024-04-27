from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path: Path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)
        return directory


# Create instances of the Site class
source = Path("./home/user/source")
dest = Path("./home/user/destination")
site = Site(source, dest)

# Example usage of create_dir() method
# Let's say we have a path "/home/user/source/dir1/file.txt"
path = Path("./home/user/source/dir1/file.txt")

# Call create_dir() method
directory = site.create_dir(path)

# Print the result
print("Full path to destination folder:", directory)
