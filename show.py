from utils import DATA_FILE, contact_dict_to_str, get_records


def show_records() -> None:
    """Show records stored in the data file"""
    records = get_records(DATA_FILE)

    for record in records:
        print(contact_dict_to_str(record))
