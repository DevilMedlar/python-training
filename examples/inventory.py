"""Local SQLite invariant lab for Python 3.12+.

Every operation owns and closes a separate connection to a file database.
This does not implement idempotency, authorization, or a distributed service.
"""

from contextlib import closing
from pathlib import Path
import sqlite3


def _integer(value: int, *, positive: bool = False) -> None:
    if type(value) is not int:
        raise TypeError("quantity must be an integer, excluding booleans")
    if value < (1 if positive else 0) or value > 2**63 - 1:
        raise ValueError("quantity is outside the allowed SQLite integer range")


def _connect(path: Path) -> sqlite3.Connection:
    # Avoid a version-dependent default for transaction policy.
    return sqlite3.connect(Path(path), autocommit=False, timeout=5)


def initialize(path: Path, quantity: int) -> None:
    """Create a new stock table. Existing tables are not reset or overwritten."""
    _integer(quantity)
    with closing(_connect(path)) as connection:
        with connection:
            connection.execute(
                "CREATE TABLE stock (code TEXT PRIMARY KEY, "
                "quantity INTEGER NOT NULL CHECK (quantity >= 0))"
            )
            connection.execute("INSERT INTO stock VALUES (?, ?)", ("A", quantity))


def reserve(path: Path, amount: int) -> None:
    """Reserve from item A or raise ValueError, owning the complete transaction."""
    _integer(amount, positive=True)
    with closing(_connect(path)) as connection:
        with connection:
            changed = connection.execute(
                "UPDATE stock SET quantity = quantity - ? "
                "WHERE code = ? AND quantity >= ?",
                (amount, "A", amount),
            ).rowcount
            if changed != 1:
                raise ValueError("insufficient stock")


def remaining(path: Path) -> int:
    with closing(_connect(path)) as connection:
        row = connection.execute("SELECT quantity FROM stock WHERE code = ?", ("A",)).fetchone()
        if row is None:
            raise ValueError("stock item A is missing")
        return row[0]
