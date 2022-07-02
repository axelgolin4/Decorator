from fighterDecorator import FighterDecorator


class PortalWeapon(FighterDecorator):

    def take_damage(self) -> float:
        return self._fighter.take_damage() + 100

    def get_velocity(self) -> float:
        return self._fighter.get_velocity() - 10

