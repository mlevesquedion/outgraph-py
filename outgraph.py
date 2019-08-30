import sys

import graphviz

import outline


def usage(script_name):
    return f'Usage: {script_name} <outline_filename>'


if __name__ == '__main__':
    try:
        outline_file = sys.argv[1]
    except IndexError:
        script_name = sys.argv[0]
        print(usage(script_name), file=sys.stderr)
        sys.exit(1)

    with open(outline_file) as outline:
        lines = map(lambda s: s.rstrip(), outline.readlines())
        edges = outline.outline_to_edges(lines)
        graphviz_file = outline_file.split('.')[0]
        dot = graphviz.Digraph(name=graphviz_file, format='pdf')
        dot.edges(edges)
        dot.render()
