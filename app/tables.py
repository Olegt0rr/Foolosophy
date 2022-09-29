__all__ = [
    "Table",
    "Philosopher",
    "PhilosopherWithNumberedForks",
    "PhilosopherWithWaiter",
    "SmartPhilosopher",
]

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

    def seat_philosophers(self) -> None:
        """Seat philosophers to their seats."""
        self.philosophers = [
            PhilosopherWithNumberedForks(
                name=str(i),
                seat_id=i,
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
                seat_id=i,
                left_fork=self.forks[i],
                right_fork=self.forks[(i + 1) % self.seats],
                waiter=waiter,
            )
            for i in range(self.seats)
        ]
