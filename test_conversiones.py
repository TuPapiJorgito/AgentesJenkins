
import pytest
import Conversion as con


def test_cm_a_pulgadas():
    assert con.cm_a_pulgadas(2.54) == pytest.approx(1)


def test_pies_a_metros():
    assert con.pies_a_metros(1) == pytest.approx(0.3048)


def test_millas_a_km():
    assert con.millas_a_km(1) == pytest.approx(1.60934)


def test_galones_a_litros():
    assert con.galones_a_litros(1) == pytest.approx(3.78541)


def test_libras_a_kg():
    assert con.libras_a_kg(1) == pytest.approx(0.453592)
