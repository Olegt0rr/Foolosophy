__all__ = [
    "AbstractPhilosopher",
    "Philosopher",
    "PhilosopherWithNumberedForks",
    "SmartPhilosopher",
    "PhilosopherWithWaiter",
    "Philosopher",
]

from .abstract import AbstractPhilosopher
from .basic import Philosopher
from .numbered import PhilosopherWithNumberedForks
from .smart import SmartPhilosopher
from .waiter import PhilosopherWithWaiter
