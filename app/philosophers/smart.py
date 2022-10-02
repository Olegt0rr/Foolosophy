import logging
import random
import time

from .abstract import AbstractPhilosopher
from ..enums import Side

logger = logging.getLogger(__name__)


class SmartPhilosopher(AbstractPhilosopher):
    """Represents smart thinker man."""

    def process(self) -> None:
        """Start dine."""
        logger.info("%r join the table", self)

        while self.is_hungry:
            self._get_both_forks()
            self._eat()
            self._return_both_forks()

        logger.info("%r left the table", self)

    def _get_both_forks(self):
        """Took both forks from the table."""
        time.sleep(random.random())
        got_left = got_right = False

        while not (got_left and got_right):
            got_left: bool = self.forks[Side.LEFT].acquire(blocking=False)
            got_right: bool = self.forks[Side.RIGHT].acquire(blocking=False)

            if not (got_left and got_right):
                if got_left:
                    self.forks[Side.LEFT].release()
                if got_right:
                    self.forks[Side.RIGHT].release()

            time.sleep(random.random())

        logger.info("%r get both forks from the table", self)

    def _return_both_forks(self):
        """Return both forks to the table."""
        self.forks[Side.LEFT].release()
        self.forks[Side.RIGHT].release()
        logger.info("%r return both forks to the table", self)
        time.sleep(random.random())
