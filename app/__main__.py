import logging

from . import start_dinner
from .tables import (
    Table,
    TableWithNumberedForks,
    TableWithSmartPhilosophers,
    TableWithWaiter,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

start_dinner(Table)
