# pyascbox

Pyascbox creates boxes of ascii characters around the specified strings. The style and width can be determined. A heading above the box is optional and is created automatically if desired.

## Installation

Install the package via pip:

```
pip install pyascbox
```

## Parameters

- `body` can't be empty
- `headline`  can be empty
- `width` > 20
- `style`: simple, double, dashed

```python
Box(body: str, headline: str, width: int, style: str)
```

## Example Code

Creates an ascii box with a width of 70 characters and double borders:
```python
from pyascbox import Box

head = "Lorem Ipsum"
body = ("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed "
        "diam nonumy eirmod tempor invidunt ut labore et dolore magna "
        "aliquyam erat, sed diam voluptua. At vero eos et accusam et "
        "justo duo dolores et ea rebum. Stet clita kasd gubergren, no "
        "sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem "
        "ipsum dolor sit amet, consetetur sadipscing elitr, sed diam "
        "nonumy eirmod tempor invidunt ut labore et dolore magna "
        "aliquyam erat, sed diam voluptua. At vero eos et accusam "
        "et justo duo dolores et ea rebum. Stet clita kasd gubergren, "
        "no sea takimata sanctus est Lorem ipsum dolor sit amet.")

    width = 70
    style = "double"


    asciibox = Box(body, head, width=width, style=style)
    print(asciibox)
```
