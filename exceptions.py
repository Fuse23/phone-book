class BadInput(Exception):
    """Exception raised for bad input.

    Attributes:
        field_names (list): A list of field names that are not correct.
    """
    def __init__(self, field_names: list[str]) -> None:
        """Initialize the BadInput exception.

        Parameters:
            field_names (list): A list of field names that are not correct.
        """
        self._field_name = field_names

        line = (
            "Bad input: "
            + ' '.join(field for field in self._field_name)
        )
        if len(self._field_name) < 0:
            line += "is not correct!"
        else:
            line += "are not correct!"

        super().__init__(line)
