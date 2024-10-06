from app.players.dwarves.dwarf import Dwarf

class DwarfBlacksmith(Dwarf):
    def __init__(self, name: str, favourite_dish: str, skill_level: int) -> None:
        super().__init__(name, favourite_dish)
        self._skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"

    def get_rating(self):
        return self._skill_level
