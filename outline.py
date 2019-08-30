import collections
import re


def graph_to_edges(graph):
    """
    graph: a dict representing a graph's adjacency lists
    output: a list of the graph's edges as (src, dst) tuples
    """
    return [(node, child) for node, children in graph.items() for child
            in children]


line_re = re.compile(r'^(\s*)(.*)')


def graph_from_outline(outline_lines):
    """
    outline_lines: a list of strings representing an outline
    output: a graph constructed from the outline
    """
    print(outline_lines)
    graph = collections.defaultdict(list)
    level_to_parent = {}
    for i, line in enumerate(outline_lines):
        if not line:
            continue
        indent, content = line_re.fullmatch(line).groups()
        if not content:
            continue
        current_indent = len(indent)
        parent_indent = current_indent - 1
        level_to_parent[current_indent] = content
        if parent_indent not in level_to_parent:
            continue
        parent = level_to_parent[parent_indent]
        graph[parent].append(content)
    return dict(graph)


def outline_to_edges(outline_lines):
    """
    graph: a dict representing a graph's adjacency lists
    output: a list of the graph's edges as (src, dst) tuples
    """
    return graph_to_edges(graph_from_outline(outline_lines))
