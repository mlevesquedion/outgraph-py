import sys

import graphviz

import core


def usage(script_name):
    return f"Usage: {script_name} <outline_filepath>"


if __name__ == "__main__":
    try:
        outline_filepath = sys.argv[1]
    except IndexError:
        print(usage(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    with open(outline_filepath) as outline_file:
        lines = map(lambda s: s.rstrip(), outline_file.readlines())
        source = core.edges_to_dot(core.lines_to_edges(lines))
        graphviz_file = outline_filepath.split(".")[0]
        dot = graphviz.Source(source)
        format = sys.argv[2] if len(sys.argv) > 2 else "pdf"
        dot.render(graphviz_file, format=format)
