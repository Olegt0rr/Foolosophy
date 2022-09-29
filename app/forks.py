from threading import Lock


class Fork:
    """Represents a table fork."""

    def __init__(self, fork_id: int):
        self.id = fork_id
        self._lock = Lock()

    def acquire(self, blocking: bool = True, timeout: float = -1.0) -> bool:
        """Took fork from the table."""
        return self._lock.acquire(blocking=blocking, timeout=timeout)

    def release(self) -> None:
        """Turn fork back to the table."""
        return self._lock.release()

    def __repr__(self):
        return f"<Fork {self.id}>"
