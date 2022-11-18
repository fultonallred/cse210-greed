import random
from game.casting.actor import Actor

class Mineral(Actor):
    """An mineral is either a gem or rock that falls from the top of the
    screen. It inherits from Actor.
    
    Args:
        Actor (Actor): the parent class of Mineral"""

    def __init__(self):
        super().__init__()
        """Constructs a new instance of Mineral from the Actor class.
            
            Args:
                self (Mineral): an instance of Mineral
            """
        self._mineral_type = ""
        self._value = 0

        types = ["gem", "rock"]
        self._mineral_type = random.choice(types)

        if type == "gem":
            self._value = 1
            self._text = "*"
        elif type == "rock":
            self._value = -1
            self._text = "O"

    def get_mineral_type(self):
        """Returns the mineral type.
        
        Args:
            self (Mineral): an instance of Mineral
        """
        return self._mineral_type

    def get_value(self):
        """Returns point value of the mineral.
        Args:
            self (Mineral): an instance of Mineral
        """
        return self._value