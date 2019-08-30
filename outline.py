import collections
import re


def tree_to_edges(tree):
    """
    tree: a dict representing a tree's adjacency lists
    output: a list of the tree's edges as (src, dst) tuples
    """
    return [(node, child) for node, children in tree.items() for child
            in children]


line_re = re.compile(r'^(\s*)(.*)')


def tree_from_outline(outline_lines):
    """
    outline_lines: a list of strings representing an outline
    output: a tree constructed from the outline
    """
    print(outline_lines)
    tree = collections.defaultdict(list)
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
        tree[parent].append(content)
    return dict(tree)


def outline_to_edges(outline_lines):
    """
    tree: a dict representing a tree's adjacency lists
    output: a list of the tree's edges as (src, dst) tuples
    """
    return tree_to_edges(tree_from_outline(outline_lines))
