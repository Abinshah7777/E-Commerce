class CatalogueNotFoundError(Exception):
    """Raised when a catalogue entry is not found."""
    pass

class InvalidCatalogueInputError(Exception):
    """Raised when input data is invalid."""
    pass

class DatabaseConnectionError(Exception):
    """Raised when the database connection fails."""
    pass
