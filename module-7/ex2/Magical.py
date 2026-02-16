from abc import ABC, abstractmethod


class Magical(ABC):

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list):
        pass

    @abstractmethod
    def channel_mana(self, amount: int):
        pass

    @abstractmethod
    def get_magic_stats(self):
        pass
