import logging
import random
import time

from .base import BasePhilosopher
from ..enums import Side

logger = logging.getLogger(__name__)


class Philosopher(BasePhilosopher):
    """Represents thinker man."""

    def process(self) -> None:
        """Start dine."""
        logger.info("%r join the table", self)

        while True:
            self._get_fork(Side.LEFT)
            self._get_fork(Side.RIGHT)
            self._eat()
            self._return_fork(Side.RIGHT)
            self._return_fork(Side.LEFT)

    def _get_fork(self, side: Side) -> None:
        """Get fork from side."""
        fork = self.forks[side]
        fork.acquire()
        logger.info("%r get %r from the %s", self, fork, side)
        time.sleep(random.random())

    def _return_fork(self, side: Side) -> None:
        """Return fork back."""
        fork = self.forks[side]
        fork.release()
        logger.info("%r return fork %r to the %s", self, fork, side)
        time.sleep(random.random())
