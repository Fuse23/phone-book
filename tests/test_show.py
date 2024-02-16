import pytest

import show
from show import show_records, contact_dict_to_str
from utils import Fields, KeyType


@pytest.mark.parametrize("records, expected", [
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
    ], contact_dict_to_str({
        Fields.INDEX: '4',
        Fields.SURNAME: "petrov",
        Fields.NAME: "pavel",
        Fields.PATRONYMIC: "dmitrievich",
        Fields.COMPANY: "tech-solutions",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89665554433",
    }) + '\n' + contact_dict_to_str({
        Fields.INDEX: '5',
        Fields.SURNAME: "sokolov",
        Fields.NAME: "dmitry",
        Fields.PATRONYMIC: "ivanovich",
        Fields.COMPANY: "netguru",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89887776655",
    }) + '\n' + contact_dict_to_str({
        Fields.INDEX: '6',
        Fields.SURNAME: "volkov",
        Fields.NAME: "oleg",
        Fields.PATRONYMIC: "aleksandrovich",
        Fields.COMPANY: "web-masters",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89998887766",
    }) + '\n' + contact_dict_to_str({
        Fields.INDEX: '7',
        Fields.SURNAME: "kozlov",
        Fields.NAME: "denis",
        Fields.PATRONYMIC: "sergeevich",
        Fields.COMPANY: "codecrafters",
        Fields.WORK_NUMBER: "89990001122",
        Fields.MOBILE_NUMBER: "",
    }) + '\n' + contact_dict_to_str({
        Fields.INDEX: '8',
        Fields.SURNAME: "sidorov",
        Fields.NAME: "anton",
        Fields.PATRONYMIC: "anatolevich",
        Fields.COMPANY: "app-devs",
        Fields.WORK_NUMBER: "",
        Fields.MOBILE_NUMBER: "89001112233",
    }) + '\n')
])
def test_show_records(
    records: list[dict[KeyType, str]],
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(show, "get_records", lambda _: records)

    show_records()
    captured = capsys.readouterr()
    assert expected == captured.out
