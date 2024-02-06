import pytest

from flight_data_module import (
    load_json_data,
    load_csv_data,
    parse_log_data,
    combine_data,
    calculate_revenue_per_passenger
)

JSON_FILE_PATH = "./data.json"
CSV_FILE_PATH = "./data.csv"
LOG_FILE_PATH = "./data.log"

@pytest.fixture
def json_data():
    return load_json_data(JSON_FILE_PATH)

@pytest.fixture
def empty_json_data(tmp_path):
    file_path = tmp_path / "empty_json_data.json"
    file_path.write_text("{}")
    return str(file_path)

@pytest.fixture
def invalid_json_data(tmp_path):
    file_path = tmp_path / "invalid_json_data.json"
    file_path.write_text("JSON Data invalido")
    return str(file_path)

@pytest.fixture
def csv_data():
    return load_csv_data(CSV_FILE_PATH)

@pytest.fixture
def empty_csv_data(tmp_path):
    file_path = tmp_path / "empty_csv_data.csv"
    file_path.write_text("Flight_ID, Passengers, Revenue\n")
    return str(file_path)

@pytest.fixture
def invalid_csv_data(tmp_path):
    file_path = tmp_path / "invalid_csv_data.csv"
    file_path.write_text("CSV Data invalido")
    return str(file_path)

@pytest.fixture
def log_data():
    return parse_log_data(LOG_FILE_PATH)

@pytest.fixture
def empty_log_data(tmp_path):
    file_path = tmp_path / "empty_log_data.log"
    file_path.write_text("")
    return str(file_path)

@pytest.fixture
def invalid_log_data(tmp_path):
    file_path = tmp_path / "invalid_log_data.log"
    file_path.write_text("Log Data invalido")
    return str(file_path)


def test_load_json_data():
    data = load_json_data(JSON_FILE_PATH)
    assert isinstance(data, list)

def test_load_json_data_empty(empty_json_data):
    data = load_json_data(empty_json_data)
    assert data == []

def test_load_json_data_invalid(invalid_json_data):
    data = load_json_data(invalid_json_data)
    assert data == []

def test_load_csv_data():
    data = load_csv_data(CSV_FILE_PATH)
    assert isinstance(data, list)

def test_load_csv_data_empty(empty_csv_data):
    data = load_csv_data(empty_csv_data)
    assert data == []

def test_load_csv_data_invalid(invalid_csv_data):
    data = load_csv_data(invalid_csv_data)
    assert data == []

def test_parse_log_data():
    data = parse_log_data(LOG_FILE_PATH)
    assert isinstance(data, list)

def test_parse_log_data_empty(empty_log_data):
    data = parse_log_data(empty_log_data)
    assert data == []

def test_parse_log_data_invalid(invalid_log_data):
    data = parse_log_data(invalid_log_data)
    assert data == []

def test_combine_data(json_data, csv_data, log_data):
    combined_data = combine_data(json_data, csv_data, log_data)
    assert isinstance(combined_data, list)

def test_calculate_revenue_per_passenger(json_data, csv_data, log_data):
    combined_data = combine_data(json_data, csv_data, log_data)
    calculate_revenue_per_passenger(combined_data)
    for flight in combined_data:
        assert "Revenue_Per_Passenger" in flight