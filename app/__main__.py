import logging
import signal

from .tables import Table

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# start dinner!
table = Table(seats=5)
table.seat_philosophers()
for philosopher in table.philosophers:
    philosopher.start()

# graceful shutdown (Ctrl+C)
try:
    signal.pause()

except (KeyboardInterrupt, SystemExit):
    for philosopher in table.philosophers:
        philosopher.is_hungry = False

    for philosopher in table.philosophers:
        philosopher.join()
