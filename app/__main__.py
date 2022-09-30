import logging

from .tables import Table

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

table = Table(seats=5)
table.start()
