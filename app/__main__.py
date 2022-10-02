import logging

from . import Table, start_dinner

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

start_dinner(Table)
