import pytest
import builtins

import search
from utils import Fields, KeyType
from search import (
    search_record,
    _get_search_fields,
    _get_fields_values,
    contact_dict_to_str,
)


@pytest.mark.parametrize("_input, expected", [
    ("1", [
        Fields.SURNAME
    ]),
    ("1 2", [
        Fields.SURNAME,
        Fields.NAME,
    ]),
    ("1 2 3", [
        Fields.SURNAME,
        Fields.NAME,
        Fields.PATRONYMIC,
    ]),
    ("1 2 3 4", [
        Fields.SURNAME,
        Fields.NAME,
        Fields.PATRONYMIC,
        Fields.COMPANY,
    ]),
    ("1 2 3 4 5", [
        Fields.SURNAME,
        Fields.NAME,
        Fields.PATRONYMIC,
        Fields.COMPANY,
        Fields.WORK_NUMBER,
    ]),
    ("1 2 3 4 5 6", [
        Fields.SURNAME,
        Fields.NAME,
        Fields.PATRONYMIC,
        Fields.COMPANY,
        Fields.WORK_NUMBER,
        Fields.MOBILE_NUMBER,
    ]),
    ("1 2 3 4 5  6 ", [
        Fields.SURNAME,
        Fields.NAME,
        Fields.PATRONYMIC,
        Fields.COMPANY,
        Fields.WORK_NUMBER,
        Fields.MOBILE_NUMBER,
    ]),
])
def test_get_search_fields(
    _input: str,
    expected: list[Fields],
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(builtins, "input", lambda _: _input)

    assert _get_search_fields() == expected


@pytest.mark.parametrize("fields, _input, expected", [
    ([
        Fields.SURNAME,
        Fields.NAME,
        Fields.PATRONYMIC,
        Fields.COMPANY,
        Fields.WORK_NUMBER,
    ], "lol", {
        Fields.SURNAME: "lol",
        Fields.NAME: "lol",
        Fields.PATRONYMIC: "lol",
        Fields.COMPANY: "lol",
        Fields.WORK_NUMBER: "lol",
    }),
    ([
        Fields.SURNAME,
        Fields.NAME,
        Fields.PATRONYMIC,
    ], "lol", {
        Fields.SURNAME: "lol",
        Fields.NAME: "lol",
        Fields.PATRONYMIC: "lol",
    }),
    ([
        Fields.SURNAME,
        Fields.WORK_NUMBER,
    ], "lol", {
        Fields.SURNAME: "lol",
        Fields.WORK_NUMBER: "lol",
    }),
])
def test_get_fields_values(
    fields: list[Fields],
    _input: str,
    expected: dict[KeyType, str],
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(builtins, "input", lambda _: _input)

    assert _get_fields_values(fields) == expected


@pytest.mark.parametrize("records, search_fields, expected", [
    ([
        {
            Fields.INDEX: '4',
            Fields.SURNAME: "petrov",
            Fields.NAME: "pavel",
            Fields.PATRONYMIC: "dmitrievich",
            Fields.COMPANY: "tech-solutions",
            Fields.WORK_NUMBER: "",
            Fields.MOBILE_NUMBER: "89665554433",
        }, {
            Fields.INDEX: '5',
            Fields.SURNAME: "sokolov",
            Fields.NAME: "dmitry",
            Fields.PATRONYMIC: "ivanovich",
            Fields.COMPANY: "netguru",
            Fields.WORK_NUMBER: "",
            Fields.MOBILE_NUMBER: "89887776655",
        }, {
            Fields.INDEX: '6',
            Fields.SURNAME: "volkov",
            Fields.NAME: "oleg",
            Fields.PATRONYMIC: "aleksandrovich",
            Fields.COMPANY: "web-masters",
            Fields.WORK_NUMBER: "",
            Fields.MOBILE_NUMBER: "89998887766",
        }, {
            Fields.INDEX: '7',
            Fields.SURNAME: "kozlov",
            Fields.NAME: "denis",
            Fields.PATRONYMIC: "sergeevich",
            Fields.COMPANY: "codecrafters",
            Fields.WORK_NUMBER: "89990001122",
            Fields.MOBILE_NUMBER: "",
        }, {
            Fields.INDEX: '8',
            Fields.SURNAME: "sidorov",
            Fields.NAME: "anton",
            Fields.PATRONYMIC: "anatolevich",
            Fields.COMPANY: "app-devs",
            Fields.WORK_NUMBER: "",
            Fields.MOBILE_NUMBER: "89001112233",
        }
    ], {
        Fields.NAME: "denis",
        Fields.COMPANY: "app-devs",
    }, contact_dict_to_str({
        Fields.INDEX: '7',
        Fields.SURNAME: "kozlov",
        Fields.NAME: "denis",
        Fields.PATRONYMIC: "sergeevich",
        Fields.COMPANY: "codecrafters",
        Fields.WORK_NUMBER: "89990001122",
        Fields.MOBILE_NUMBER: "",
    }) + "\n" + contact_dict_to_str({
        Fields.INDEX: '8',
        Fields.SURNAME: "sidorov",
        Fields.NAME: "anton",
        Fields.PATRONYMIC: "anatolevich",
        Fields.COMPANY: "app-devs",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89001112233",
    }) + '\n'),
])
def test_search_record(
    records: list[dict[KeyType, str]],
    search_fields: dict[KeyType, str],
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(search, "get_records", lambda _: records)
    monkeypatch.setattr(search, "_get_search_fields", lambda: None)
    monkeypatch.setattr(search, "_get_fields_values", lambda _: search_fields)

    search_record()
    captured = capsys.readouterr()
    assert expected == captured.out
