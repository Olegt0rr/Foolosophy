import logging

from .basic import Philosopher

logger = logging.getLogger(__name__)


class PhilosopherWithNumberedForks(Philosopher):
    """Represents philosopher taking lowest fork id first."""

    def process(self) -> None:
        """Start dine."""

        logger.info("%r join the table", self)

        sides_ordered = [
            side
            for side, fork in sorted(self.forks.items(), key=lambda item: item[1].id)
        ]

        while True:
            for side in sides_ordered:
                self._get_fork(side)

            self._eat()

            for side in sides_ordered:
                self._return_fork(side)
