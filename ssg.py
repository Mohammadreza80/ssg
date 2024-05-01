import typer

from ssg.site import Site
import ssg.parsers


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest, "parsers": [ssg.parsers.ResourceParser()]}
    Site(**config).build()


# main("./testsrc", "./dest/one/two")

typer.run(main)
