import logging
from threading import Semaphore

from .basic import Philosopher
from ..enums import Side
from ..forks import Fork

logger = logging.getLogger(__name__)


class PhilosopherWithWaiter(Philosopher):
    def __init__(
        self,
        name: str,
        seat_id: int,
        left_fork: Fork,
        right_fork: Fork,
        waiter: Semaphore,
    ):
        super().__init__(
            name=name,
            seat_id=seat_id,
            left_fork=left_fork,
            right_fork=right_fork,
        )
        self._waiter = waiter

    def _get_fork(self, side: Side) -> None:
        """Get fork from side with waiter's help."""
        with self._waiter:
            super()._get_fork(side)
