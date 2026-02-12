import pytest 
from train_model import predict_phone_generation

def test_known_phones():
    assert predict_phone_generation("iPhone 6") == "old"
    assert predict_phone_generation("iPhone 13") == "morden"

def test_unknown_phone():
    assert predict_phone_generation("iPhone 20") == "unknown"

def test_all_phones_have_valid_generation():
    generations = {"old","morden","latest"}
    phone_list = ["iPhone 6", "iPhone XR", "iPhone 14"]
    for phone in phone_list:
        assert predict_phone_generation(phone) in generations