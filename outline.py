import collections
import re


def tree_to_edges(tree):
    """
    tree: a dict representing a tree's adjacency lists
    output: a list of the tree's edges as (src, dst) tuples
    """
    return [(node, child) for node, children in tree.items() for child
            in children]


LINE_RE = re.compile(r'^(\s*)(.*)')


def tree_from_outline(outline_lines):
    """
    outline_lines: a list of strings representing an outline
    output: a tree constructed from the outline
    """
    tree = collections.defaultdict(list)
    parent_at_depth = {}
    for line in filter(bool, outline_lines):
        indent, content = LINE_RE.fullmatch(line).groups()

        depth = len(indent)
        parent_at_depth[depth] = content

        if depth == 0:
            continue

        parent_depth = depth - 1
        parent = parent_at_depth[parent_depth]
        tree[parent].append(content)
    return dict(tree)


def outline_to_edges(outline_lines):
    """
    tree: a dict representing a tree's adjacency lists
    output: a list of the tree's edges as (src, dst) tuples
    """
    return tree_to_edges(tree_from_outline(outline_lines))
