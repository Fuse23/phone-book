from enum import Enum
import re
from typing import Literal
import csv

from exceptions import BadInput


# Constants
DATA_FILE = "data.csv"  # Default data file name


class Fields(str, Enum):
    """Enum class representing fields in the contact records
    """
    INDEX = "index"
    SURNAME = "surname"
    NAME = "name"
    PATRONYMIC = "patronymic"
    COMPANY = "company"
    WORK_NUMBER = "work number"
    MOBILE_NUMBER = "mobile number"


# Literal type for specifying key type
KeyType = Literal[
    Fields.INDEX,
    Fields.SURNAME,
    Fields.NAME,
    Fields.PATRONYMIC,
    Fields.COMPANY,
    Fields.WORK_NUMBER,
    Fields.MOBILE_NUMBER,
]


def contact_dict_to_str(contact_dict: dict[KeyType, str]) -> str:
    """Convert a dictionary representing a contact into a string.

    Parameters:
        contact_dict (dict): Dictionary representing a contact with keys as
            Field enums and values as strings.

    Returns:
        str: String representation of the contact.
    """
    return ", ".join(contact_dict.values())


def write_records(
    records: list[dict[KeyType, str]],
    file: str,
    mode: str
) -> None:
    """Write records to a CSV file.

    Parameters:
        records (list): List of dictionaries representing records with keys as
            Field enums and values as strings.
        file (str): Path to the CSV file.
        mode (str): Mode in which to open the file ('w' for write, 'a' for append).
    """
    with open(file, mode, newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[field for field in Fields]
        )

        for record in records:
            writer.writerow(record)


def get_records(file: str) -> list[dict[KeyType, str]]:
    """Get records from a CSV file.

    Parameters:
        file (str): Path to the CSV file.

    Returns:
        list: List of dictionaries representing records with keys as
            Field enums and values as strings.
    """
    records = []

    with open(file, 'r', newline='', encoding="utf-8") as csvread:
        reader = csv.DictReader(
            csvread,
            fieldnames=[field for field in Fields],
        )

        for record in reader:
            records.append(record)

    return records


def validate_input(data: dict[KeyType, str]) -> None:
    """Validate input data against predefined rules.

    Parameters:
        data (dict): Dictionary representing a contact with keys as
                     Field enums and values as strings.

    Raises:
        BadInput: If input data violates the validation rules.
    """
    check_func_dict = {
        Fields.SURNAME: _check_surname,
        Fields.NAME: _check_name,
        Fields.PATRONYMIC: _check_patronymic,
        Fields.COMPANY: _check_company_name,
        Fields.WORK_NUMBER: _check_work_number,
        Fields.MOBILE_NUMBER: _check_mobile_number,
    }

    for key in data.keys():
        if (
            key in check_func_dict
            and not check_func_dict[key](data[key])
        ):
            raise BadInput([key.value])


def _check_name(name: str) -> bool:
    """Check if the name string is valid.

    Parameters:
        name (str): Name string to validate.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    if not re.match(r"^[a-zа-яёA-ZА-ЯЁ]{2,15}$", name) and len(name) > 0:
        return False
    return True


def _check_surname(surname: str) -> bool:
    """Check if the surname string is valid.

    Parameters:
        surname (str): Surname string to validate.

    Returns:
        bool: True if the surname is valid, False otherwise.
    """
    if not re.match(r"^[a-zа-яёA-ZА-ЯЁ]{2,15}$", surname) and len(surname) > 0:
        return False
    return True


def _check_patronymic(patronymic: str) -> bool:
    """Check if the patronymic string is valid.

    Parameters:
        patronymic (str): Patronymic string to validate.

    Returns:
        bool: True if the patronymic is valid, False otherwise.
    """
    if not re.match(
        r"^[a-zа-яёA-ZА-ЯЁ]{2,15}$",
        patronymic
    ) and len(patronymic) > 0:
        return False
    return True


def _check_company_name(company_name: str) -> bool:
    """Check if the company name string is valid.

    Parameters:
        company_name (str): Company name string to validate.

    Returns:
        bool: True if the company name is valid, False otherwise.
    """
    if not re.match(
        r"^[a-zа-яёA-ZА-ЯЁ0-9\s-]{2,20}$",
        company_name
    ) and len(company_name) > 0:
        return False
    return True


def _check_work_number(work_number: str) -> bool:
    """Check if the work number string is valid.

    Parameters:
        work_number (str): Work number string to validate.

    Returns:
        bool: True if the work number is valid, False otherwise.
    """
    if not re.match(
        r"^[\+]?[(]?[0-9]{3}[)]?[-\s]?[0-9]{3}[-\s]?[0-9]{4,6}$",
        work_number
    ) and len(work_number) > 0:
        return False
    return True


def _check_mobile_number(mobile_number: str) -> bool:
    """Check if the mobile number string is valid.

    Parameters:
        mobile_number (str): Mobile number string to validate.

    Returns:
        bool: True if the mobile number is valid, False otherwise.
    """
    if not re.match(
        r"^[\+]?[(]?[0-9]{3}[)]?[-\s]?[0-9]{3}[-\s]?[0-9]{4,6}$",
        mobile_number
    ) and len(mobile_number) > 0:
        return False
    return True
