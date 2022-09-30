__all__ = [
    "Table",
    "Philosopher",
    "PhilosopherWithNumberedForks",
    "PhilosopherWithWaiter",
    "SmartPhilosopher",
]

import signal
from threading import Semaphore
from typing import List

from .forks import Fork
from .philosophers import (
    Philosopher,
    PhilosopherWithNumberedForks,
    PhilosopherWithWaiter,
    SmartPhilosopher,
)

DEFAULT_SEATS = 5


class Table:
    """Represents Table with Philosophers."""

    def __init__(
        self,
        seats: int = DEFAULT_SEATS,
    ):
        self.seats = seats
        self.forks = [Fork(i) for i in range(seats)]
        self.philosophers: List[Philosopher] = []

    def start(self) -> None:
        """Start dinner."""
        self.seat_philosophers()
        for philosopher in self.philosophers:
            philosopher.start()

        try:
            signal.pause()

        except (KeyboardInterrupt, SystemExit):
            for philosopher in self.philosophers:
                philosopher.is_hungry = False

            for philosopher in self.philosophers:
                philosopher.join()

    def seat_philosophers(self) -> None:
        """Seat philosophers to their seats."""
        self.philosophers = [
            PhilosopherWithNumberedForks(
                name=str(i),
                left_fork=self.forks[i],
                right_fork=self.forks[(i + 1) % self.seats],
            )
            for i in range(self.seats)
        ]


class TableWithWaiter(Table):
    """Represents table with a waiter."""

    def seat_philosophers(self) -> None:
        """Seat philosophers to their seats."""
        waiter = Semaphore(len(self.forks) - 1)
        self.philosophers = [
            PhilosopherWithWaiter(
                name=str(i),
                left_fork=self.forks[i],
                right_fork=self.forks[(i + 1) % self.seats],
                waiter=waiter,
            )
            for i in range(self.seats)
        ]
