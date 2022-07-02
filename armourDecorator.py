from fighterDecorator import FighterDecorator


class ArmourDecorator(FighterDecorator):

    def take_damage(self) -> float:
        return self._fighter.take_damage() / 1.5

    def get_velocity(self) -> float:
        return self._fighter.get_velocity() - 50

    def get_def(self) -> float:
        return self._fighter.get_def() + 100

