import pytest
from train_model import phones

def test_no_missing_name_or_generation():
    for phone in phones:
        assert "name" in phone and phone["name"], "Phone name missing!"
        assert "generation" in phone and phone["generation"], "Generation missing!"

def test_unique_phone_names():
    names= [phone["name"] for phone in phones]
    assert len(names) == len(set(names)), "Duplicate phone names found!"
    