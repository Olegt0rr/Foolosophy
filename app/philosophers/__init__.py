__all__ = [
    "BasePhilosopher",
    "Philosopher",
    "PhilosopherWithNumberedForks",
    "SmartPhilosopher",
    "PhilosopherWithWaiter",
    "Philosopher",
]

from .base import BasePhilosopher
from .basic import Philosopher
from .numbered import PhilosopherWithNumberedForks
from .smart import SmartPhilosopher
from .waiter import PhilosopherWithWaiter
