class Planet(object)
    color = ["blue", "yellow", "red", "grey"]
    size = ["S", "M", "L", "XL"]

    def _init_(self, size, color)
    self.sizeIndex = size
    self.colorIndex = color

    def _str_(self):
        face = Planet.size[self.sizeIndex]
        suit = Planet.color[self.colorIndex]
        return size + color

