from string import whitespace
import json


class Box:
    def __init__(self, body: str, headline: str = None, width: int = 80, style: str = "simple"):
        self.width = width - 4
        self.body = body
        self.headline = headline
        self.style = style


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, content: int):
        if not isinstance(content, int):
            raise TypeError("width must be a intiger")
        if content < 20:
            raise ValueError("width can't be less than 24")
        self._width = content


    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, content: str):
        if not isinstance(content, str):
            raise TypeError("body must be a string")
        if len(content) <= 0:
            raise ValueError("body can't be empty")
        self._body = content


    @property
    def headline(self):
        return self._headline

    @headline.setter
    def headline(self, content: str):
        if content is not None:
            if not isinstance(content, str):
                raise TypeError("headline must be a string")
            if len(content) >= self.width:
                raise ValueError("headline must fit in width of box")
        self._headline = content


    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, content):
        if not isinstance(content, str):
            raise TypeError("style must be a string")
        with open("./pyboxes/borders.json", "r", encoding="utf-8") as borders:
            if content not in json.load(borders).keys():
                raise ValueError("style is not defined")
        self._style = content


    def __centralize__(self, content: str, length: int) -> str:
        space = (length - len(content)) / 2
        if space % 1 == 0:
            return f"{' ' * int(space)}{content}{' ' * int(space)}"
        return f"{' ' * int(space)}{content}{' ' * (int(space) + 1)}"

    
    def __split_body__(self) -> list:
        if not any(x in self.body for x in whitespace):
            return [self.__centralize__(self.body[i:i+self.width], self.width) for i in range(0, len(self.body), self.width)]

        content = self.body.split(" ")
        storage = []
        j = 0

        for i in range(len(content)+1):
            if sum([len(x) for x in content][j:i]) + len(content[j:i])-1 >= self.width:
                storage.append(" ".join(content[j:i-1]))
                j = i-1
        storage.append(" ".join(content[j:]))

        return [self.__centralize__(x, self.width) for x in storage]


    def __str__(self):
        splited_body = self.__split_body__()

        with open("./pyboxes/borders.json", "r", encoding="utf-8") as borders:
            chars = json.load(borders)[self.style][0]

        content = f"{chars.get('leftUpperCorner')}{chars.get('horizontalConnector')*(self.width+2)}{chars.get('rightUpperCorner')}\n"

        if self.headline is not None:
            content += f"{chars.get('verticalConnector')} {self.__centralize__(self.headline, self.width)} {chars.get('verticalConnector')}\n"
            content += f"{chars.get('headBodyConnectorLeft')}{chars.get('horizontalConnector')*(self.width+2)}{chars.get('headBodyConnectorRight')}\n"

        for x in splited_body:
            content += f"{chars.get('verticalConnector')} {x} {chars.get('verticalConnector')}\n"

        content += f"{chars.get('leftLowerCorner')}{chars.get('horizontalConnector')*(self.width+2)}{chars.get('rightLowerCorner')}"

        return content

