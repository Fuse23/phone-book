import pytest
import builtins

import edit
from utils import Fields, KeyType, contact_dict_to_str
from exceptions import BadInput
from edit import (
    _edit_record_by_index,
    _get_record_index,
    _get_new_values,
    edit_record,
)


@pytest.mark.parametrize("data, index, expected", [
    ([{
        Fields.INDEX: '2',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "mobile number",
    }], '2', True),
    ([{
        Fields.INDEX: '2',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "mobile number",
    }], '1', False),
    ([{
        Fields.INDEX: '2',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "mobile number",
    }, {
        Fields.INDEX: '4',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "mobile number",
    }], '2', True),
    ([{
        Fields.INDEX: '2',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "mobile number",
    }, {
        Fields.INDEX: '4',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "mobile number",
    }], '3', False),
])
def test_edit_record_by_index(
    data: list[dict[KeyType, str]],
    index: str,
    expected: bool,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(edit, "_get_new_values", lambda _: data[0])

    result = _edit_record_by_index(data, index)
    captured = capsys.readouterr()

    assert result == expected
    if expected:
        assert captured.out == contact_dict_to_str(data[0]) + '\n'


@pytest.mark.parametrize("expected", [('1'), ('2'), ('a'), ('zero')])
def test_get_record_index(
    expected: str,
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(builtins, "input", lambda _: expected)

    if not expected.isdigit():
        with pytest.raises(BadInput) as e:
            _get_record_index()
        assert "index for edit" in str(e.value)
    else:
        assert _get_record_index() == expected


@pytest.mark.parametrize("data, _input, expected", [
    ({
        Fields.INDEX: '4',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "mobile number",
    }, "lol", {
        Fields.INDEX: '4',
        Fields.SURNAME: "lol",
        Fields.NAME: "lol",
        Fields.PATRONYMIC: "lol",
        Fields.COMPANY: "lol",
        Fields.WORK_NUMBER: "lol",
        Fields.MOBILE_NUMBER: "lol",
    }),
    ({
        Fields.INDEX: '4',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "mobile number",
    }, "", {
        Fields.INDEX: '4',
        Fields.SURNAME: "surname",
        Fields.NAME: "name",
        Fields.PATRONYMIC: "patronymic",
        Fields.COMPANY: "company",
        Fields.WORK_NUMBER: "work number",
        Fields.MOBILE_NUMBER: "mobile number",
    }),
])
def test_get_new_values(
    data: dict[KeyType, str],
    _input: str,
    expected: dict[KeyType, str],
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(edit, "validate_input", lambda _: _)
    monkeypatch.setattr(builtins, "input", lambda _: _input)

    assert _get_new_values(data) == expected


@pytest.mark.parametrize("index, edited, expected", [
    ('2', True, "Success edit record\n"),
    ('2', False, ""),
])
def test_edit_record(
    index: str,
    edited: bool,
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(edit, "get_records", lambda _: [])
    monkeypatch.setattr(edit, "_get_record_index", lambda: index)
    monkeypatch.setattr(edit, "_edit_record_by_index", lambda x, y: edited)
    monkeypatch.setattr(edit, "write_records", lambda x, y, z: None)

    edit_record()
    captured = capsys.readouterr()

    if not edited:
        assert index in captured.out
    else:
        assert expected == captured.out
