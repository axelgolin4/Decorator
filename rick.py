from fighter import Fighter


class Rick(Fighter):
    def __init__(self):
        self.hp: float = 500
        self.defence: float = 500
        self.attack: float = 50
        self.velocity: float = 250
        self.damage: float = 0



    def get_hp(self) -> float:
        return self.hp

    def get_def(self) -> float:
        return self.defence

    def get_velocity(self) -> float:
        # velocity_capacity = f"Velocidad: {self.velocity}"
        return self.velocity

    def take_damage(self) -> float:
        return self.attack