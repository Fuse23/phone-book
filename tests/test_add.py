import pytest
import builtins

import add
from add import (
    _check_any_names,
    _check_any_number,
    _get_input,
    _validate_data,
    add_record,
    Fields,
    KeyType,
)
from exceptions import BadInput


@pytest.mark.parametrize("data, expected", [
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "",
        Fields.NAME: "",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, "surname name patronymic company"),
    ({
        Fields.INDEX: '',
        Fields.SURNAME: "",
        Fields.NAME: "",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, "surname name patronymic company"),
    ({
        Fields.INDEX: '11',
        Fields.SURNAME: "",
        Fields.NAME: "",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "456789",
        Fields.MOBILE_NUMBER: "fghjkl",
    }, "surname name patronymic company"),
])
def test_check_any_names(data: dict[KeyType, str], expected: str) -> None:
    with pytest.raises(BadInput) as e:
        _check_any_names(data)
    assert expected in str(e.value)


@pytest.mark.parametrize("_input, expected", [
    ("text", {
        Fields.INDEX: '0',
        Fields.SURNAME: "text",
        Fields.NAME: "text",
        Fields.PATRONYMIC: "text",
        Fields.COMPANY: "text",
        Fields.WORK_NUMBER: "text",
        Fields.MOBILE_NUMBER: "text",
    }),
])
def test_get_input(
    _input: str,
    expected: dict[KeyType, str],
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(builtins, 'input', lambda _: _input)
    monkeypatch.setattr(add, '_validate_data', lambda _: True)

    assert _get_input() == expected


@pytest.mark.parametrize("data, expected", [
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "",
        Fields.NAME: "",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, " ".join([
        Fields.SURNAME.value,
        Fields.NAME.value,
        Fields.PATRONYMIC.value,
        Fields.COMPANY.value,
    ])),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, " ".join([Fields.WORK_NUMBER.value, Fields.MOBILE_NUMBER.value])),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "1234",
    }, Fields.MOBILE_NUMBER.value),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "",
        Fields.NAME: "",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "77776665",
        Fields.MOBILE_NUMBER: "",
    }, Fields.WORK_NUMBER.value),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patr0nymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89997777666",
    }, Fields.PATRONYMIC.value),
])
def test_validate_data(
    data: dict[KeyType, str],
    expected: str
) -> None:
    with pytest.raises(BadInput) as e:
        _validate_data(data)
    assert expected in str(e.value)


@pytest.mark.parametrize("data, expected", [
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, "work number mobile number"),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, "work number mobile number"),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, "work number mobile number"),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, "work number mobile number"),
    ({
        Fields.INDEX: '0',
        Fields.SURNAME: "",
        Fields.NAME: "",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, "work number mobile number"),
    ({
        Fields.INDEX: '',
        Fields.SURNAME: "",
        Fields.NAME: "",
        Fields.PATRONYMIC: "",
        Fields.COMPANY: "",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "",
    }, "work number mobile number"),
])
def test_check_any_numbers(data: dict[KeyType, str], expected: str) -> None:
    with pytest.raises(BadInput) as e:
        _check_any_number(data)
    assert expected in str(e.value)


@pytest.mark.parametrize("expected", [
    ("Success add record\n"),
])
def test_add_contact(
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(add, "_get_input", lambda: {"index": 0})
    monkeypatch.setattr(add, "get_records", lambda _: [1])
    monkeypatch.setattr(add, "write_records", lambda x, y, z: None)

    add_record()
    captured = capsys.readouterr()

    assert captured.out == expected
