# Foolosophy

Solving [Dining philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem)

## How to launch

There are no requirements.\
Just run ```python3 -m app```

## Solutions

### 1. Smart philosopher

Philosopher try to take both forks and if it's not successful - release acquired forks.

### 2. Waiter

Let's add waiter. Philosopher can't get fork without waiter. Waiter is a Semaphore with n-1 limit.

### 3. Numbered forks

Let Philosopher take fork with smaller ID first.

### 4. Contribute your solution!

Feel free to contribute your solution.
