class InvalidUuidException(Exception):
    def __init__(self, error='ID must be a valid UUID') -> None:  # pylint: disable=useless-super-delegation
        super().__init__(error)