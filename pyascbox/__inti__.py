from boxcreation import Box


def main():
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
    style = "double" # simple, double, dashed


    asciibox = Box(body, head, width=width, style=style)
    print(asciibox)


if __name__ == "__main__":
    main()
    
