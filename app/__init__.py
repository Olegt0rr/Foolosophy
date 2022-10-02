__all__ = [
    "start_dinner",
    "Table",
    "TableWithSmartPhilosophers",
    "TableWithWaiter",
    "TableWithNumberedForks",
]

import signal
from typing import Type

from .tables import (
    Table,
    TableWithNumberedForks,
    TableWithSmartPhilosophers,
    TableWithWaiter,
)


def start_dinner(table_class: Type[Table]):
    """Start the dinner"""
    table = Table(seats=5)
    table.seat_philosophers()

    for philosopher in table.philosophers:
        philosopher.start()

    _shutdown(table)


def _shutdown(table: Table):
    """Wait for graceful shutdown (Ctrl+C)."""
    try:
        signal.pause()

    except (KeyboardInterrupt, SystemExit):
        for philosopher in table.philosophers:
            philosopher.is_hungry = False

        for philosopher in table.philosophers:
            philosopher.join()
