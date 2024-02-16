import pytest
import os
import csv
from typing import Generator, Any
from tempfile import NamedTemporaryFile

from exceptions import BadInput
from utils import (
    Fields,
    KeyType,
    contact_dict_to_str,
    write_records,
    get_records,
    validate_input,
    _check_company_name,
    _check_mobile_number,
    _check_name,
    _check_patronymic,
    _check_surname,
    _check_work_number,
)


@pytest.mark.parametrize("data, expected", [
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "777",
        Fields.MOBILE_NUMBER: "666",
    }, "0, surname, name, patronymic, company, 777, 666"),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "666",
    }, "0, surname, name, patronymic, company, , 666"),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "666",
    }, "0, surname, name, , 666"),
])
def test_contact_dict_to_str(data: dict[KeyType, str], expected: str) -> None:
    assert contact_dict_to_str(data) == expected


@pytest.fixture
def temp_csv_file() -> Generator[str, Any, None]:
    with NamedTemporaryFile(
        mode='w', delete=False, newline='', encoding='utf-8'
    ) as temp_file:
        temp_file.flush()
        yield temp_file.name
    os.unlink(temp_file.name)


@pytest.mark.parametrize("data", [
    ([{
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "777",
        Fields.MOBILE_NUMBER: "666",
    }]),
    ([{
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "777",
        Fields.MOBILE_NUMBER: "666",
    }, {
        Fields.INDEX: '1',
        Fields.SURNAME: "afsegr",
        Fields.NAME: "rfgert",
        Fields.PATRONYMIC: "fgr4terd",
        Fields.COMPANY: "rfegtr",
        Fields.WORK_NUMBER: "sfgbr",
        Fields.MOBILE_NUMBER: "fsgebr",
    }]),
])
def test_write_records(
    data: list[dict[KeyType, str]],
    temp_csv_file: str
) -> None:
    write_records(data, temp_csv_file, 'w')

    with open(temp_csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(
            csvfile,
            fieldnames=[field for field in Fields]
        )
        for record, data_record in zip(reader, data):
            for field in Fields:
                assert record[field] == data_record[field]


@pytest.mark.parametrize("expected", [
    ({
        Fields.INDEX: '4',
        Fields.SURNAME: "petrov",
        Fields.NAME: "pavel",
        Fields.PATRONYMIC: "dmitrievich",
        Fields.COMPANY: "tech-solutions",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89665554433",
    }),
    ({
        Fields.INDEX: '5',
        Fields.SURNAME: "sokolov",
        Fields.NAME: "dmitry",
        Fields.PATRONYMIC: "ivanovich",
        Fields.COMPANY: "netguru",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89887776655",
    }),
    ({
        Fields.INDEX: '6',
        Fields.SURNAME: "volkov",
        Fields.NAME: "oleg",
        Fields.PATRONYMIC: "aleksandrovich",
        Fields.COMPANY: "web-masters",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89998887766",
    }),
    ({
        Fields.INDEX: '7',
        Fields.SURNAME: "kozlov",
        Fields.NAME: "denis",
        Fields.PATRONYMIC: "sergeevich",
        Fields.COMPANY: "codecrafters",
        Fields.WORK_NUMBER: "89990001122",
        Fields.MOBILE_NUMBER: "",
    }),
    ({
        Fields.INDEX: '8',
        Fields.SURNAME: "sidorov",
        Fields.NAME: "anton",
        Fields.PATRONYMIC: "anatolevich",
        Fields.COMPANY: "app-devs",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89001112233",
    }),
])
def test_get_records(expected: dict[KeyType, str]) -> None:
    records = get_records("tests/test_data.csv")
    assert expected in records


@pytest.mark.parametrize("data, expected", [
    ({
        Fields.INDEX: '8',
        Fields.SURNAME: "234ref",
        Fields.NAME: "anton",
        Fields.PATRONYMIC: "anatolevich",
        Fields.COMPANY: "app-devs",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89001112233",
    }, "surname"),
    ({
        Fields.INDEX: '8',
        Fields.SURNAME: "surname",
        Fields.NAME: "34950ghnve",
        Fields.PATRONYMIC: "anatolevich",
        Fields.COMPANY: "app-devs",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89001112233",
    }, "name"),
    ({
        Fields.INDEX: '8',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "fh49e8oijf",
        Fields.COMPANY: "app-devs",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89001112233",
    }, "patronymic"),
    ({
        Fields.INDEX: '8',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "!vjne&@",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89001112233",
    }, "company"),
    ({
        Fields.INDEX: '8',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "89001112233",
    }, "work number"),
    ({
        Fields.INDEX: '8',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "mobile number",
    }, "mobile number"),
    ({
        Fields.INDEX: '8',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patr0nymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "mobile number",
    }, "patronymic"),
])
def test_validate_input(data: dict[KeyType, str], expected: str) -> None:
    with pytest.raises(BadInput) as e:
        validate_input(data)
    assert expected in str(e.value)


@pytest.mark.parametrize("surname, expected", [
    ("sjdnjvbieu", True),
    ("dsfnjvfi", True),
    ("", True),
    ("a", False),
    ("fnsjkv9sndfi", False),
    ("f28wfsjdc", False),
    ("fwfsjdc!", False),
])
def test_check_surname(surname: str, expected: bool) -> None:
    assert _check_surname(surname) == expected


@pytest.mark.parametrize("name, expected", [
    ("sjdnjvbieu", True),
    ("dsfnjvfi", True),
    ("", True),
    ("a", False),
    ("fnsjkv9sndfi", False),
    ("f28wfsjdc", False),
    ("fwfsjdc!", False),
])
def test_check_name(name: str, expected: bool) -> None:
    assert _check_name(name) == expected


@pytest.mark.parametrize("patronymic, expected", [
    ("sjdnjvbieu", True),
    ("dsfnjvfi", True),
    ("", True),
    ("a", False),
    ("fnsjkv9sndfi", False),
    ("f28wfsjdc", False),
    ("fwfsjdc!", False),
])
def test_check_patronymic(patronymic: str, expected: bool) -> None:
    assert _check_patronymic(patronymic) == expected


@pytest.mark.parametrize("company, expected", [
    ("sjdnjvbieu", True),
    ("dsfnjvfi", True),
    ("", True),
    ("a", False),
    ("fnsjkv9sndfi", True),
    ("f28wfsjdc", True),
    ("fwfsjdc!", False),
])
def test_check_company_name(company: str, expected: bool) -> None:
    assert _check_company_name(company) == expected


@pytest.mark.parametrize("number, expected", [
    ("89998887766", True),
    ("89990001122", True),
    ("", True),
    ("a", False),
    ("899900O1122", False),
    ("899900011", False),
    ("fwfsjdc!", False),
])
def test_check_work_number(number: str, expected: bool) -> None:
    assert _check_work_number(number) == expected


@pytest.mark.parametrize("number, expected", [
    ("89998887766", True),
    ("89990001122", True),
    ("", True),
    ("a", False),
    ("899900O1122", False),
    ("899900011", False),
    ("fwfsjdc!", False),
])
def test_check_mobile_number(number: str, expected: bool) -> None:
    assert _check_mobile_number(number) == expected
