class Color:
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 255

    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)

        elif attr == "hexcolor":
            return f"#{self.red:02x}{self.green:02x}{self.blue:02x}"

        else:
            raise AttributeError

    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor", "hexcolor")


color = Color()
print(color.rgbcolor)
print(color.hexcolor)

color.rgbcolor = (0, 0, 0)
print(color.rgbcolor)
print(color.hexcolor)

print(dir(color))
