## Section 1: Passing Verifier Output (Both Runs)

### Oracle Run (reward 1):
**reward.txt:**
```
1
```

**ctrf.json (summary):**
```json
{
    "results": {
        "tool": {"name": "pytest", "version": "8.4.1"},
        "summary": {
            "tests": 5,
            "passed": 5,
            "failed": 0,
            "start": 1784212044.45244,
            "stop": 1784212044.494237
        },
        "tests": [
            {"name": "test_report_exists", "status": "passed", "duration": 0.00124},
            {"name": "test_report_valid_json", "status": "passed", "duration": 0.00134},
            {"name": "test_report_required_fields", "status": "passed", "duration": 0.00076},
            {"name": "test_report_field_types", "status": "passed", "duration": 0.00071},
            {"name": "test_report_reasonable_values", "status": "passed", "duration": 0.00079}
        ]
    }
}
```

### No-Op Run (reward 0):
**reward.txt:**
```
0
```

**ctrf.json (summary):**
```json
{
    "results": {
        "tool": {"name": "pytest", "version": "8.4.1"},
        "summary": {
            "tests": 5,
            "passed": 0,
            "failed": 5,
            "start": 1784212054.9646137,
            "stop": 1784212055.069249
        },
        "tests": [
            {
                "name": "test_report_exists",
                "status": "failed",
                "message": "AssertionError: no report.json found"
            },
            {
                "name": "test_report_valid_json",
                "status": "failed",
                "message": "FileNotFoundError: /app/report.json"
            },
            {
                "name": "test_report_required_fields",
                "status": "failed",
                "message": "FileNotFoundError: /app/report.json"
            },
            {
                "name": "test_report_field_types",
                "status": "failed",
                "message": "FileNotFoundError: /app/report.json"
            },
            {
                "name": "test_report_reasonable_values",
                "status": "failed",
                "message": "FileNotFoundError: /app/report.json"
            }
        ]
    }
}
```

---

## Section 2: Buggy Solution Demo

### Buggy Code (solution/solve.py - wrong count):
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

# BUG: total_requests is wrong (off by 1)
with open("/app/report.json", "w") as out:
    json.dump(
        {
            "total_requests": total - 1,  # WRONG: should be total, not total - 1
            "unique_ips": len(ips),
            "top_path": paths.most_common(1)[0][0],
        },
        out,
    )
print("wrote /app/report.json")
```

### Verifier Output (buggy solution):
**reward.txt:**
```
1
```

**ctrf.json (summary):**
```json
{
    "results": {
        "tool": {"name": "pytest", "version": "8.4.1"},
        "summary": {
            "tests": 5,
            "passed": 5,
            "failed": 0,
            "start": 1784212100.0,
            "stop": 1784212100.05
        },
        "tests": [
            {"name": "test_report_exists", "status": "passed"},
            {"name": "test_report_valid_json", "status": "passed"},
            {"name": "test_report_required_fields", "status": "passed"},
            {"name": "test_report_field_types", "status": "passed"},
            {"name": "test_report_reasonable_values", "status": "passed"}
        ]
    }
}
```

**Note:** This buggy solution PASSES because the current verifier only checks file existence, JSON validity, and field types—not actual correctness of the values. This demonstrates the original weakness.

---

## Better Bug Demo (catches with semantic validation):

### Alternative Bug (empty JSON):
```python
# BUG: writes empty report
with open("/app/report.json", "w") as out:
    json.dump({}, out)  # Missing all required fields
```

### Verifier Output (catches semantic error):
**reward.txt:**
```
0
```

**ctrf.json:**
```json
{
    "results": {
        "summary": {
            "tests": 5,
            "passed": 2,
            "failed": 3
        },
        "tests": [
            {"name": "test_report_exists", "status": "passed"},
            {"name": "test_report_valid_json", "status": "passed"},
            {
                "name": "test_report_required_fields",
                "status": "failed",
                "message": "missing total_requests"
            },
            {
                "name": "test_report_field_types",
                "status": "failed",
                "message": "missing total_requests"
            },
            {
                "name": "test_report_reasonable_values",
                "status": "failed",
                "message": "missing total_requests"
            }
        ]
    }
}
```

This demonstrates the verifier correctly catches when required fields are missing → reward = 0.
