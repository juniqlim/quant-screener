import math

import pytest

from fetch_kr import (
    _calc_growth_rate,
    _income_current_and_yoy_base,
    _to_int_amount,
)


class TestToIntAmount:
    def test_parses_numeric_string(self):
        assert _to_int_amount("1,234,567") == 1234567

    def test_invalid_returns_zero(self):
        assert _to_int_amount(None) == 0
        assert _to_int_amount("") == 0
        assert _to_int_amount("N/A") == 0


class TestGrowthRate:
    def test_basic_growth(self):
        result = _calc_growth_rate(120, 100)
        assert pytest.approx(result, rel=1e-6) == 0.2

    def test_zero_base_returns_none(self):
        assert _calc_growth_rate(120, 0) is None
        assert _calc_growth_rate(120, None) is None


class TestIncomeCurrentAndYoyBase:
    def test_annual_uses_thstrm_and_frmtrm(self):
        row = {
            "thstrm_amount": "200",
            "frmtrm_amount": "160",
        }
        current, yoy_base = _income_current_and_yoy_base(row)
        assert current == 200
        assert yoy_base == 160

    def test_quarterly_prefers_frmtrm_q_amount(self):
        row = {
            "thstrm_amount": "300",
            "frmtrm_q_amount": "240",
            "frmtrm_amount": "999",  # should be ignored when frmtrm_q exists
        }
        current, yoy_base = _income_current_and_yoy_base(row)
        assert current == 300
        assert yoy_base == 240
