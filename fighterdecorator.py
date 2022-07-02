from fighter import Fighter


class FighterDecorator(Fighter):


    _fighter: Fighter = None

    def __init__(self, fighter: Fighter) -> None:
        self._fighter = fighter



    def take_damage(self) -> int:
        return self._fighter.take_damage()

    def get_hp(self) -> float:
        return self._fighter.get_hp()

    def get_def(self) -> float:
        return self._fighter.get_def()

    def get_velocity(self) -> float:
        return self._fighter.get_velocity()
