from pytest import mark
import from_outline
import graphviz


@mark.parametrize(
    ["graph", "edges"],
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
def test_graph_to_edges(graph, edges):
    assert from_outline.graph_to_edges(graph) == edges


linked_list_outline = """\
a
 b
  c
   d
    e""".splitlines()
linked_list_graph = {"a": ["b"], "b": ["c"], "c": ["d"], "d": ["e"]}
linked_list_edges = from_outline.graph_to_edges(linked_list_graph)

tree_outline = """\
1
 2
  3
  4
   5
 6
  7""".splitlines()
tree_graph = {
    "1": ["2", "6"],
    "2": ["3", "4"],
    "4": ["5"],
    "6": ["7"],
}
tree_edges = [
    ("1", "2"),
    ("1", "6"),
    ("2", "3"),
    ("2", "4"),
    ("4", "5"),
    ("6", "7"),
]


@mark.parametrize(
    ["outline_lines", "graph"],
    [
        ("", {}),
        (linked_list_outline, linked_list_graph),
        (tree_outline, tree_graph),
    ],
)
def test_from_outline(outline_lines, graph):
    assert from_outline.from_outline(outline_lines) == graph


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
    assert from_outline.line_re.match(line).groups() == groups


@mark.parametrize(
    ["outline_lines", "edges"],
    [
        ("", []),
        (linked_list_outline, linked_list_edges),
        (tree_outline, tree_edges),
    ]
)
def test_outline_to_edges(outline_lines, edges):
    assert from_outline.outline_to_edges(outline_lines) == edges
