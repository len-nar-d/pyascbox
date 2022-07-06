import json
from string import whitespace
from textwrap import wrap


class Box:
    def __init__(
        self, body: str,
        headline: str = None,
        width: int = 80,
        style: str = "simple"
):
        self.width = width - 4
        self.body = body
        self.headline = headline
        self.style = style


    @property
    def width(self):
        """Width of the ascii box in characters."""
        return self._width

    @width.setter
    def width(self, content: int):
        """Checks if width is an intiger and over 20."""
        if not isinstance(content, int):
            raise TypeError("width must be a intiger")
        if content < 20:
            raise ValueError("width can't be less than 24")
        self._width = content


    @property
    def body(self):
        """String of the text in the body of the ascii box."""
        return self._body

    @body.setter
    def body(self, content: str):
        """Checks if body is an string and not empty."""
        if not isinstance(content, str):
            raise TypeError("body must be a string")
        if len(content) <= 0:
            raise ValueError("body can't be empty")
        self._body = content


    @property
    def headline(self):
        """String of the headline of the ascii box."""
        return self._headline

    @headline.setter
    def headline(self, content: str):
        """
        Checks if headline, if not None, is an string and not larger than the
        width.
        """
        if content is not None:
            if not isinstance(content, str):
                raise TypeError("headline must be a string")
            if len(content) >= self.width:
                raise ValueError("headline must fit in width of box")
        self._headline = content


    @property
    def style(self):
        """Style regarding the outlines of the ascii box."""
        return self._style

    @style.setter
    def style(self, content: str):
        """Checks if style is an string and is present in borders.json."""
        if not isinstance(content, str):
            raise TypeError("style must be a string")
        with open("./pyascbox/borders.json", "r", encoding="utf-8") as borders:
            if content not in json.load(borders).keys():
                raise ValueError("style is not defined")
        self._style = content


    def __centralize__(self, content: str, length: int) -> str:
        """
        Centralises a line of text with equal whitespace infront and behind the
        initial string with specified final width.
        If the target width is odd, the whitespace behind the string is larger
        than the whitespace infront of the string.
        
        Parameters
        ----------
        content : str
            Initial string to be centralized.
        length : int
            Length of the desired centralized string (width).

        Returns
        -------
        str
            Centralized string.
        
        """
        space = (length - len(content)) / 2
        if space % 1 == 0:
            return f"{' ' * int(space)}{content}{' ' * int(space)}"
        return f"{' ' * int(space)}{content}{' ' * (int(space) + 1)}"

    
    def __split_body__(self) -> list:
        """
        Splits the body with as equal a length as possible lines so they fit
        into the borders of the ascii box.
        If there is no whitespace, the lines are split exactly according to
        the specified width. Otherwise, the lines are split at positions where
        whitespace is available.

        Returns
        -------
        list
            List of strings representing the lines of text in the ascii box.
        
        """
        if not any(x in self.body for x in whitespace):
            content = wrap(self.body, self.width)
            for i, k in enumerate(content):
                content[i] = self.__centralize__(k, self.width)

            return content


        content = self.body.split(" ")
        storage = []
        j = 0

        for i in range(len(content)+1):
            if (sum([len(x) for x in content][j:i])
                + len(content[j:i])-1 >= self.width):
                storage.append(" ".join(content[j:i-1]))
                j = i-1
        storage.append(" ".join(content[j:]))

        return [self.__centralize__(x, self.width) for x in storage]


    def __str__(self):
        """
        Creates the string representing the ascii box.
        If the headline is None, this part of the box is not included in the
        string. The body will always be included in the string.

        Returns
        -------
        str
            Ascii box with content.
        """
        splited_body = self.__split_body__()

        with open("./pyascbox/borders.json", "r", encoding="utf-8") as borders:
            chars = json.load(borders)[self.style][0]

        content = (f"{chars.get('leftUpperCorner')}"
                   f"{chars.get('horizontalConnector')*(self.width+2)}"
                   f"{chars.get('rightUpperCorner')}\n")

        if self.headline is not None:
            content += (f"{chars.get('verticalConnector')} "
                        f"{self.__centralize__(self.headline, self.width)}"
                        f" {chars.get('verticalConnector')}\n")

            content += (f"{chars.get('headBodyConnectorLeft')}"
                        f"{chars.get('horizontalConnector')*(self.width+2)}"
                        f"{chars.get('headBodyConnectorRight')}\n")

        for x in splited_body:
            content += (f"{chars.get('verticalConnector')} "
                        f"{x}"
                        f" {chars.get('verticalConnector')}\n")

        content += (f"{chars.get('leftLowerCorner')}"
                    f"{chars.get('horizontalConnector')*(self.width+2)}"
                    f"{chars.get('rightLowerCorner')}")

        return content

