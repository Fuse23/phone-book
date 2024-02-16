import sys

from exceptions import BadInput
from utils import (
    DATA_FILE,
    Fields,
    KeyType,
    validate_input,
    write_records,
    get_records,
)


def add_record() -> None:
    """Add a new record to the data file"""
    record = _get_input()
    record[Fields.INDEX] = str(len(get_records(DATA_FILE)) + 1)
    write_records([record], DATA_FILE, '+a')
    print("Success add record")


def _get_input() -> dict[KeyType, str]:
    """Get input data for a new record from user.

    Returns:
        dict: Dictionary representing the new record.
    """
    print("Input contact data")

    contact_dict: dict[KeyType, str] = {}
    for field in Fields:
        if field is Fields.INDEX:
            contact_dict[field] = '0'
            continue

        contact_dict[field] = input(field.value + ": ").strip().lower()

    _validate_data(contact_dict)

    return contact_dict


def _validate_data(data: dict[KeyType, str]) -> None:
    """Validate input data for a new record.

    Parameters:
        data (dict): Dictionary representing the new record.

    Raises:
        BadInput: If input data violates validation rules.
    """
    _check_any_names(data)
    _check_any_number(data)
    validate_input(data)


def _check_any_names(data: dict[KeyType, str]) -> None:
    """Check if any name fields are empty in the input data.

    Parameters:
        data (dict): Dictionary representing the new record.

    Raises:
        BadInput: If any name fields are empty.
    """
    names = (
        data[Fields.SURNAME] + data[Fields.NAME]
        + data[Fields.PATRONYMIC] + data[Fields.COMPANY]
    )

    if not len(names) > 0:
        raise BadInput([
            Fields.SURNAME.value,
            Fields.NAME.value,
            Fields.PATRONYMIC.value,
            Fields.COMPANY.value,
        ])


def _check_any_number(data: dict[KeyType, str]) -> None:
    """Check if any number fields are empty in the input data.

    Parameters:
        data (dict): Dictionary representing the new record.

    Raises:
        BadInput: If any number fields are empty.
    """
    numbers = data[Fields.WORK_NUMBER] + data[Fields.MOBILE_NUMBER]

    if not len(numbers) > 0:
        raise BadInput([Fields.WORK_NUMBER, Fields.MOBILE_NUMBER])


if __name__ == "__main__":
    while True:
        try:
            add_record()
        except BadInput as e:
            print(e, file=sys.stderr)
