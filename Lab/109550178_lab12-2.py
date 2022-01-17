class Attraction:

    attraction_name = "default"

    def __init__(self):
        pass

    def set_attraction_name(self):
        pass

    def print(self):
        print("The attraction is ", end="")


class Place(Attraction):

    def __init__(self, name):
        self.name = name
        print(self.name, "is created")

    def set_attraction_name(self, attraction_name):
        self.attraction_name = attraction_name

    def print_attraction_name(self):
        if self.attraction_name == "Love River":
            self.print()
            print("Love River")
        else:
            self.print()
            print("A LIE")


p1 = Place("p1")
p1.set_attraction_name("Love River")
p1.print_attraction_name()
p2 = Place("p2")
p2.set_attraction_name("Love Ferris Wheel")
p2.print_attraction_name()
p3 = Place("p3")
p3.set_attraction_name("Disneyland")
p3.print_attraction_name()
