from core import *


def test_lines_to_edges():
    lines = """
a
 b
  c
  d: e
 f
g
 h""".splitlines()
    lines.pop(0)
    edges = [
        Edge("a", "b"),
        Edge("b", "c"),
        Edge("b", "e").with_label("d"),
        Edge("a", "f"),
        Edge("g", "h"),
    ]
    assert edges == lines_to_edges(lines)


def test_edges_to_dot():
    edges = [Edge("a", "b"), Edge("b", "c").with_label("d")]
    assert 'digraph outmind {a -> b []; b -> c [label="d"];}' == edges_to_dot(
        edges
    )
