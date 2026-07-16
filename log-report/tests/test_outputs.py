import json
from pathlib import Path


def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_valid_json():
    """The report file contains valid JSON."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json is not a JSON object"


def test_report_required_fields():
    """The report contains all required fields."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert "total_requests" in data, "missing total_requests"
    assert "unique_ips" in data, "missing unique_ips"
    assert "top_path" in data, "missing top_path"


def test_report_field_types():
    """The report fields have correct types."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert isinstance(data["total_requests"], int), "total_requests is not an int"
    assert isinstance(data["unique_ips"], int), "unique_ips is not an int"
    assert isinstance(data["top_path"], str), "top_path is not a string"


def test_report_reasonable_values():
    """The report values are reasonable (non-negative, non-empty)."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data["total_requests"] > 0, "total_requests must be > 0"
    assert data["unique_ips"] > 0, "unique_ips must be > 0"
    assert len(data["top_path"]) > 0, "top_path must not be empty"
