# Foolosophy

Solving [Dining philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem)

## How to launch

Use `python3.9`. There are no other requirements.

```python
import logging

# import required solution class and `start_dinner` executor
from app import start_dinner
from app.tables import Table

# setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# pass chosen solution class to the executor
start_dinner(Table)
```

## Solutions

### 0. Basic problem.

Every philosopher took the left fork and then will forever await for the right fork.

Class `Table`

### 1. Smart philosopher

Philosopher try to take both forks and if it's not successful - release acquired forks.

Class: `TableWithSmartPhilosophers`

### 2. Waiter

Let's add waiter. Philosopher can't get fork without waiter. Waiter is a Semaphore with n-1 limit.

Class: `TableWithWaiter`

### 3. Numbered forks

Let Philosopher take fork with smaller ID first.

Class: `TableWithNumberedForks`

### 4. Contribute your solution!

Feel free to contribute your solution.
