# Foolosophy

Solving [Dining philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem)

## How to launch

There are no requirements.\
Just run ```python3 -m app```

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
