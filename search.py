from utils import DATA_FILE, Fields, KeyType, contact_dict_to_str, get_records


def search_record() -> None:
    """Search for records based on user-defined criteria"""
    records = get_records(DATA_FILE)
    search_fields = _get_fields_values(_get_search_fields())

    found = False
    for record in records:
        if any(
            value in [record[key] for key in search_fields.keys()]
            for value in search_fields.values()
        ):
            print(contact_dict_to_str(record))
            found = True

    if not found:
        print("\nNot found any records!\n")


def _get_search_fields() -> list[Fields]:
    """Get the fields to search for from user input.

    Returns:
        list: A list of Fields enum representing the fields to search for.
    """
    print("Enter the number of the fields to search for")
    for index, field in enumerate(Fields):
        if field is Fields.INDEX:
            continue

        print(str(index) + ". " + field.value)

    fields_dict = {index: field for index, field in zip(
        [str(index) for index in range(len(Fields) + 1)],
        [field for field in Fields]
    )}
    fields = [
        fields_dict[_] for _ in input(
            "Enter number split wise space: "
        ).split()
    ]

    return fields


def _get_fields_values(fields: list[Fields]) -> dict[KeyType, str]:
    """Get values for the specified fields from user input.

    Parameters:
        fields (list): A list of Fields enum representing the fields.

    Returns:
        dict: A dictionary with Field keys and corresponding user-entered values.
    """
    print("Enter the values of fields")

    values = {}
    for field in fields:
        values[field] = input(f"{field}: ").strip().lower()

    return values


if __name__ == "__main__":
    try:
        while True:
            search_record()
    except KeyboardInterrupt:
        print("End!")
