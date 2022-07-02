import abc


class Fighter(metaclass=abc.ABCMeta):
    def take_damage(self) -> int:
        raise NotImplementedError

    def get_hp(self) -> float:
        raise NotImplementedError

    def get_def(self) -> float:
        raise NotImplementedError

    def get_velocity(self) -> float:
        raise NotImplementedError



