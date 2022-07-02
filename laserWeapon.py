from fighterDecorator import FighterDecorator


class LaserWeapon(FighterDecorator):

    def take_damage(self) -> float:
        return self._fighter.take_damage() + 150

    def get_velocity(self) -> float:
        return self._fighter.get_velocity() - 15

