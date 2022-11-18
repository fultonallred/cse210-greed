import random
from game.shared.color import Color
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
        self._value = 1

    def get_value(self):
        """Returns point value of the mineral.
        Args:
            self (Mineral): an instance of Mineral
        """
        return self._value

    def rand_properties(self):
        """Sets the mineral's type as either a gem or rock.
        
        Args:
            self (Mineral): an instance of Mineral
        """
        types = ["gem", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock", "rock"]
        self._mineral_type = random.choice(types)

        if self._mineral_type == "gem":
            self._text = "#"
            self._value = 1
        elif self._mineral_type == "rock":
            self._text = "O"
            self._value = -2
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self._color = Color(r, g, b)

    def get_collectability(self):
        return self._collected
        
    def downgrade(self):
        self._value = -1
        self._text = "O"