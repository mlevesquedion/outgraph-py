from pytest import mark
import outline


@mark.parametrize(
    ["tree", "edges"],
    [
        ({}, []),
        ({
            "a": ["b"]
        }, [("a", "b")]),
        ({
            "a": ["b", "c"]
        }, [("a", "b"), ("a", "c")]),
        ({
            "a": ["b"],
            "b": ["c"]
        }, [("a", "b"), ("b", "c")]),
    ],
)
def test_tree_to_edges(tree, edges):
    assert outline.tree_to_edges(tree) == edges


linked_list_outline = """\
a
 b
  c
   d
    e""".splitlines()
linked_list_tree = {"a": ["b"], "b": ["c"], "c": ["d"], "d": ["e"]}
linked_list_edges = [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e")]

tree_outline = """\
1
 2
  3
  4
   5
 6
  7""".splitlines()
tree_tree = {
    "1": ["2", "6"],
    "2": ["3", "4"],
    "4": ["5"],
    "6": ["7"],
}
tree_edges = outline.tree_to_edges(tree_tree)


@mark.parametrize(
    ["outline_lines", "tree"],
    [
        ("", {}),
        (linked_list_outline, linked_list_tree),
        (tree_outline, tree_tree),
    ],
)
def test_outline(outline_lines, tree):
    assert outline.tree_from_outline(outline_lines) == tree


TAB = ' ' * 4


@mark.parametrize(
    ["line", "groups"],
    [
        ('', ('', '')),
        ("a", ('', 'a')),
        (' a', (' ', 'a')),
        (TAB + 'asdf' + TAB, (TAB, 'asdf' + TAB))
    ]
)
def test_line_regex(line, groups):
    assert outline.LINE_RE.match(line).groups() == groups


@mark.parametrize(
    ["outline_lines", "edges"],
    [
        ("", []),
        (linked_list_outline, linked_list_edges),
        (tree_outline, tree_edges),
    ]
)
def test_outline_to_edges(outline_lines, edges):
    assert outline.outline_to_edges(outline_lines) == edges
