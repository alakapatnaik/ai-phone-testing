# AI Phone Testing (Python + Pytest)

This is a simple learning project to understand AI/model testing concepts using a basic iPhone generation prediction model.
Learning focus: data validation, model validation, and automated testing workflow.
The model predicts:

- old
- modern
- latest
- unknown

## Files

- train_model.py → Phone prediction logic
- test_data.py → Data validation tests
- test_model.py → Model output tests

## Run Project

Create virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install pytest joblib

Run tests:

pytest -v

---

This project demonstrates:
- Data validation
- Model output validation
- Edge case testing
- Basic AI testing workflow
