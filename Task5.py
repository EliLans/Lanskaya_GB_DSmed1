#5. Реализовать класс Stationery (канцелярская принадлежность).

class Stationery:
    title: str

    def draw(self):
        return 'action'

class Pen(Stationery):
    title = 'it is pen'

    def draw(self):
        return self.title

class Pencil(Stationery):
    title = 'it is pencil'

    def draw(self):
        return self.title

class Handle(Stationery):
    title = 'it is handle'

    def draw(self):
        return self.title

p = Pen()
pc = Pencil()
h = Handle()
s = Stationery()

print(s.draw())
print(h.draw())
print(p.draw())
print(pc.draw())