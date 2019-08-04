# Outgraph

Produce a graph visualization from an outline.

## Usage
```
python3 outgraph.py <outline_file>
```

## Outline format

The outline is assumed to describe a tree, with a single "root" element.
The indentation is assumed to be a single space per level.

### Valid outline
```
Root
 Child1
  Subchild11
  Subchild12
 Child2
  Subchild21
```

#### Output
![Valid outline](valid_outline.png)

### Invalid outline (two roots)
```
Root1
 Child
Root2
 Child
```

### Invalid outline (two spaces for indentation instead of 1)
```
Root
  ChildTwoSpaces
```
