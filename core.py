import random
from dataclasses import dataclass, field
import re


@dataclass
class Edge:
    _from: str = ""
    _to: str = ""

    def from_(self, from_):
        self._from = from_
        return self

    def to(self, to):
        self._to = to
        return self

    def label(self, label):
        return LabeledEdge(self._from, self._to, label)

    def __str__(self):
        return f'"{self._from}" -> "{self._to}";'


@dataclass
class LabeledEdge:
    _from: str
    _to: str
    _label: str

    def __str__(self):
        return f'"{self._label}" [shape=plaintext]; "{self._from}" -> "{self._label}" [arrowhead=none]; "{self._label}" -> "{self._to}";'


SPACES_CONTENT_RE = re.compile(r"^(\s*)(.*)")


def lines_to_edges(lines):
    def make_edge(from_, content):
        edge = Edge().from_(from_)
        if ":" in content:
            label, to = [part.strip() for part in content.split(":")]
            return edge.to(to).label(label)
        else:
            return edge.to(content)

    edges = []
    name_at_indent = {}

    for line in lines:
        spaces, content = SPACES_CONTENT_RE.fullmatch(line).groups()
        line_indent = len(spaces)
        if line_indent == 0:
            name_at_indent[line_indent] = content
            continue
        from_ = name_at_indent[line_indent - 1]
        edge = make_edge(from_, content)
        edges.append(edge)
        name_at_indent[line_indent] = edge._to

    return edges


def edges_to_dot(edges):
    return "digraph outmind {" + " ".join(map(str, edges)) + "}"
