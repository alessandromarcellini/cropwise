from core.orm import SessionLocal
class PersistanceBase:
    """
    Base class for persistence layer.
    Creates a session for database operations.
    Inheriting classes should use this session for database interactions.
    """
    # session

    def __init__(self):
        self.session = SessionLocal()