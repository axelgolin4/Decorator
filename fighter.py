import abc



class Fighter(metaclass=abc.ABCMeta):
    def get_hp(self):
        raise NotImplementedError

    def get_attack(self):
        raise NotImplementedError

    def get_def(self):
        raise NotImplementedError

    def get_velocity(self):
        raise NotImplementedError

    def reduce_hp(self, damage: float):
        raise NotImplementedError

    def compute_damage(self, enemy):
        raise NotImplementedError
