from fighter import Fighter


class Morty(Fighter):
    def __init__(self):
        self.hp: float = 400
        self.defence: float = 350
        self.attack: float = 35
        self.velocity: float = 300

    def get_hp(self) -> str:
        life = f"Vida: {self.hp}"
        return life

    def get_def(self) -> str:
        defence_life = f"Escudo: {self.defence}"
        return defence_life

    def get_velocity(self) -> str:
        velocity_capacity = f"Velocidad: {self.velocity}"
        return velocity_capacity

    def take_damage(self) -> float:
        return self.attack


