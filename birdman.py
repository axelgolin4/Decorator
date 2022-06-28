import velocity as velocity

from fighter import Fighter


class Rick:
    def __init__(self):
        self.hp: float = 600
        self.defence: float = 200
        self.attack: float = 150
        self.velocity: float = 150

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack

    def get_def(self):
        return self.defence

    def get_velocity(self):
        return self.velocity

    def reduce_hp(self):
        damage = self.attack
        return damage

    def compute_damage(enemy: Fighter):
        pass


