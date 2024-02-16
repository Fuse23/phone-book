from exceptions import BadInput
from utils import (
    DATA_FILE,
    Fields,
    KeyType,
    contact_dict_to_str,
    validate_input,
    write_records,
    get_records,
)


def edit_record() -> None:
    """Edit a record stored in the data file"""
    records = get_records(DATA_FILE)
    record_index = _get_record_index()
    edited = _edit_record_by_index(records, record_index)

    if not edited:
        print(f"Record with this index: {record_index} dose not exist!")
        return

    write_records(records, DATA_FILE, 'w')
    print("Success edit record")


def _edit_record_by_index(
    records: list[dict[KeyType, str]],
    index: str
) -> bool:
    """Edit a record in the list of records based on the index.

    Parameters:
        records (list): List of dictionaries representing records.
        index (str): Index of the record to edit.

    Returns:
        bool: True if the record is successfully edited, False otherwise.
    """
    for i in range(len(records)):
        if records[i][Fields.INDEX] == index:
            print(contact_dict_to_str(records[i]))
            records[i] = _get_new_values(records[i])
            return True

    return False


def _get_record_index() -> str:
    """Get the index of the record to edit from user input.

    Returns:
        str: Index of the record to edit.
    """
    index = input("Enter the number of records for edeting: ").strip()

    if not index.isdigit():
        raise BadInput(["index for edit"])

    return index


def _get_new_values(data: dict[KeyType, str]) -> dict[KeyType, str]:
    """Get new values for the record fields from user input.

    Parameters:
        data (dict): Dictionary representing the original record.

    Returns:
        dict: Dictionary with updated values for the record fields.
    """
    print("Enter new value or press 'enter' for skip")

    new_record: dict[KeyType, str] = {}
    for field in Fields:
        if field is Fields.INDEX:
            new_record[field] = data[field]
            continue

        _input = input(field.value + ": ").strip().lower()

        new_record[field] = (
            _input if len(_input) > 0 else data[field]
        )

    validate_input(new_record)

    return new_record


if __name__ == "__main__":
    from show import show_records

    try:
        while True:
            show_records()
            edit_record()
    except KeyboardInterrupt:
        print("End")
