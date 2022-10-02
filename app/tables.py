__all__ = [
    "Table",
    "TableWithNumberedForks",
    "TableWithSmartPhilosophers",
    "TableWithWaiter",
    "Philosopher",
    "PhilosopherWithNumberedForks",
    "SmartPhilosopher",
    "PhilosopherWithWaiter",
]

from threading import Semaphore
from typing import List, Type

from .forks import Fork
from .philosophers import (
    AbstractPhilosopher,
    Philosopher,
    PhilosopherWithNumberedForks,
    PhilosopherWithWaiter,
    SmartPhilosopher,
)

DEFAULT_SEATS = 5


class Table:
    """Represents Table with Philosophers.

    This is example of blocking state.
    Every philosopher took the left fork and then will forever await
    for the right fork.
    """

    philosopher_class: Type[AbstractPhilosopher] = Philosopher

    def __init__(
        self,
        seats: int = DEFAULT_SEATS,
    ):
        self.seats = seats
        self.forks = [Fork(i) for i in range(seats)]
        self.philosophers: List[AbstractPhilosopher] = []

    def seat_philosophers(self) -> None:
        """Seat philosophers to their seats."""
        self.philosophers = [
            self.philosopher_class(
                name=str(i),
                left_fork=self.forks[i],
                right_fork=self.forks[(i + 1) % self.seats],
            )
            for i in range(self.seats)
        ]


class TableWithSmartPhilosophers(Table):
    """Represents table with smart philosophers.

    Philosopher try to take both forks and if it's not successful -
    release acquired forks.
    """

    philosopher_class: Type[AbstractPhilosopher] = SmartPhilosopher


class TableWithWaiter(Table):
    """Represents table with a waiter.

    Let's add waiter. Philosopher can't get fork without waiter.
    Waiter is a Semaphore with `len(forks)-1` limit.
    """

    philosopher_class: Type[AbstractPhilosopher] = PhilosopherWithWaiter

    def seat_philosophers(self) -> None:
        """Seat philosophers to their seats and add waiter."""
        waiter = Semaphore(len(self.forks) - 1)
        self.philosophers = [
            self.philosopher_class(
                name=str(i),
                left_fork=self.forks[i],
                right_fork=self.forks[(i + 1) % self.seats],
                waiter=waiter,
            )
            for i in range(self.seats)
        ]


class TableWithNumberedForks(Table):
    """Represents table with numbered forks.

    Let Philosopher take fork with smallest ID first.
    """

    philosopher_class: Type[AbstractPhilosopher] = PhilosopherWithNumberedForks
