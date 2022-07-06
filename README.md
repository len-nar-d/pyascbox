# pyascbox
## Installation

Install the package via pip:

```
pip install pyascbox
```

## Class Box

- width > 20
- style -> simple, double, dashed

```python
Box(body: str, headline: str, width: int, style: str)
```

## Example Code

### Code:
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

### Output:

```txt
╔════════════════════════════════════════════════════════════════════╗
║                            Lorem Ipsum                             ║
╠════════════════════════════════════════════════════════════════════╣
║ Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam  ║
║  nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam  ║
║    erat, sed diam voluptua. At vero eos et accusam et justo duo    ║
║  dolores et ea rebum. Stet clita kasd gubergren, no sea takimata   ║
║   sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit    ║
║  amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor  ║
║     invidunt ut labore et dolore magna aliquyam erat, sed diam     ║
║    voluptua. At vero eos et accusam et justo duo dolores et ea     ║
║   rebum. Stet clita kasd gubergren, no sea takimata sanctus est    ║
║                    Lorem ipsum dolor sit amet.                     ║
╚════════════════════════════════════════════════════════════════════╝
```