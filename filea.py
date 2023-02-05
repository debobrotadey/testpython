class filea():
    a = 4
    def __init__(self, name=""):
        print(name)

    def abc(self):
        print(f"this is just abc class {self.a}")


b = filea("Deb")
b.abc()