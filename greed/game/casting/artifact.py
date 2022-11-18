from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """An artifact is a small object that the kitten can be hidden behind.
    It inherits from Actor.
    
    Args:
        Actor (Actor): the parent class of Artifact"""

    def __init__(self):
        super().__init__()
        """Constructs a new instance of Artifact."""
        self._message = ""

    def set_message(self, message):
        """Set a message to display when Artifact is hovered over.
        
        Args:
            self (Artifact): an instance of Artifact
            message (str): message to be displayed
        """
        self._message = message

    def get_message(self):
        """Returns the message assigned to Artifact.
        
        Args:
            self (Artifact): an instance of Artifact
        """
        return self._message