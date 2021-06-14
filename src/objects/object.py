from pygame import Vector2


class Object:
    def __init__(self, x, y, width, height):
        self.pos = Vector2(x, y)
        self.size = Vector2(width, height)

    def collides_with(self, other):
        si = self.pos
        sf = self.pos + self.size
        oi = other.pos
        of = other.pos + other.size

        if si[1] > of[1] or sf[1] < oi[1] or si[0] > of[0] or sf[0] < oi[0]:
            return False
        return True

    def move_by(self, delta: Vector2):
        self.pos += delta

    def move_to(self, pos):
        self.pos = Vector2(pos.x, pos.y)
