## Passing Verifier Output (Oracle Run - reward 1)

**reward.txt:**
```
1
```

**ctrf.json:**
```json
{
    "results": {
        "tool": {
            "name": "pytest",
            "version": "8.4.1"
        },
        "summary": {
            "tests": 5,
            "passed": 5,
            "failed": 0,
            "skipped": 0,
            "start": 1784212044.45244,
            "stop": 1784212044.494237
        },
        "tests": [
            {
                "name": "test_outputs.py::test_report_exists",
                "status": "passed",
                "duration": 0.00124
            },
            {
                "name": "test_outputs.py::test_report_valid_json",
                "status": "passed",
                "duration": 0.00134
            },
            {
                "name": "test_outputs.py::test_report_required_fields",
                "status": "passed",
                "duration": 0.00076
            },
            {
                "name": "test_outputs.py::test_report_field_types",
                "status": "passed",
                "duration": 0.00071
            },
            {
                "name": "test_outputs.py::test_report_reasonable_values",
                "status": "passed",
                "duration": 0.00079
            }
        ]
    }
}
```

---

## Passing Verifier Output (No-Op Run - reward 0)

**reward.txt:**
```
0
```

**ctrf.json:**
```json
{
    "results": {
        "tool": {
            "name": "pytest",
            "version": "8.4.1"
        },
        "summary": {
            "tests": 5,
            "passed": 0,
            "failed": 5,
            "skipped": 0,
            "start": 1784212054.9646137,
            "stop": 1784212055.069249
        },
        "tests": [
            {
                "name": "test_outputs.py::test_report_exists",
                "status": "failed",
                "raw_status": "call_failed",
                "message": "AssertionError: no report.json found"
            },
            {
                "name": "test_outputs.py::test_report_valid_json",
                "status": "failed",
                "raw_status": "call_failed",
                "message": "FileNotFoundError: [Errno 2] No such file or directory: '/app/report.json'"
            },
            {
                "name": "test_outputs.py::test_report_required_fields",
                "status": "failed",
                "raw_status": "call_failed",
                "message": "FileNotFoundError: [Errno 2] No such file or directory: '/app/report.json'"
            },
            {
                "name": "test_outputs.py::test_report_field_types",
                "status": "failed",
                "raw_status": "call_failed",
                "message": "FileNotFoundError: [Errno 2] No such file or directory: '/app/report.json'"
            },
            {
                "name": "test_outputs.py::test_report_reasonable_values",
                "status": "failed",
                "raw_status": "call_failed",
                "message": "FileNotFoundError: [Errno 2] No such file or directory: '/app/report.json'"
            }
        ]
    }
}
```

---

## Buggy Solution (Caught by Verifier)

**Buggy Code (solution/solve_buggy.py):**
```python
import json
import re
from collections import Counter

paths, ips, total = Counter(), set(), 0
with open("/app/access.log") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1

# BUG: Write empty JSON instead of required report structure
with open("/app/report.json", "w") as out:
    json.dump({}, out)
print("wrote /app/report.json (buggy - empty)")
```

**Verifier Output (catches bug - reward 0):**

**reward.txt:**
```
0
```

**ctrf.json:**
```json
{
    "results": {
        "tool": {
            "name": "pytest",
            "version": "8.4.1"
        },
        "summary": {
            "tests": 5,
            "passed": 2,
            "failed": 3,
            "skipped": 0,
            "start": 1784212280.5814235,
            "stop": 1784212280.6622384
        },
        "tests": [
            {
                "name": "test_outputs.py::test_report_exists",
                "status": "passed",
                "duration": 0.00068
            },
            {
                "name": "test_outputs.py::test_report_valid_json",
                "status": "passed",
                "duration": 0.00073
            },
            {
                "name": "test_outputs.py::test_report_required_fields",
                "status": "failed",
                "raw_status": "call_failed",
                "duration": 0.00124,
                "trace": "/tests/test_outputs.py:21: in test_report_required_fields\n    assert \"total_requests\" in data, \"missing total_requests\"\nE   AssertionError: missing total_requests\nE   assert 'total_requests' in {}",
                "message": "The test failed in the call phase due to an assertion error"
            },
            {
                "name": "test_outputs.py::test_report_field_types",
                "status": "failed",
                "raw_status": "call_failed",
                "duration": 0.00113,
                "trace": "/tests/test_outputs.py:30: in test_report_field_types\n    assert isinstance(data[\"total_requests\"], int), \"total_requests is not an int\"\n                      ^^^^^^^^^^^^^^^^^^^^^^\nE   KeyError: 'total_requests'",
                "message": "The test failed in the call phase"
            },
            {
                "name": "test_outputs.py::test_report_reasonable_values",
                "status": "failed",
                "raw_status": "call_failed",
                "duration": 0.00080,
                "trace": "/tests/test_outputs.py:39: in test_report_reasonable_values\n    assert data[\"total_requests\"] > 0, \"total_requests must be > 0\"\n           ^^^^^^^^^^^^^^^^^^^^^^\nE   KeyError: 'total_requests'",
                "message": "The test failed in the call phase"
            }
        ]
    }
}
```

**Verification:** Buggy solution (empty JSON) fails 3 tests and returns reward = **0**. Verifier correctly catches semantic errors (missing required fields) not just file existence.
