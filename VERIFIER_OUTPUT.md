# Terminal-Bench 2 (Harbor) - Fixed Task Verifier Output

## Run 1: Oracle (Reference Solution) — harbor run -p log-report -a oracle

### reward.txt
```
1
```

### ctrf.json (Common Test Report Format)
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
            "pending": 0,
            "other": 0,
            "start": 1784212044.45244,
            "stop": 1784212044.494237
        },
        "tests": [
            {
                "name": "test_outputs.py::test_report_exists",
                "status": "passed",
                "duration": 0.0012480770001275232,
                "start": 1784212044.4805508,
                "stop": 1784212044.4825277,
                "retries": 0,
                "file_path": "test_outputs.py"
            },
            {
                "name": "test_outputs.py::test_report_valid_json",
                "status": "passed",
                "duration": 0.0013483750001341832,
                "start": 1784212044.4839253,
                "stop": 1784212044.486139,
                "retries": 0,
                "file_path": "test_outputs.py"
            },
            {
                "name": "test_outputs.py::test_report_required_fields",
                "status": "passed",
                "duration": 0.0007680720000280417,
                "start": 1784212044.4875598,
                "stop": 1784212044.4888487,
                "retries": 0,
                "file_path": "test_outputs.py"
            },
            {
                "name": "test_outputs.py::test_report_field_types",
                "status": "passed",
                "duration": 0.0007164930000271852,
                "start": 1784212044.490121,
                "stop": 1784212044.4912956,
                "retries": 0,
                "file_path": "test_outputs.py"
            },
            {
                "name": "test_outputs.py::test_report_reasonable_values",
                "status": "passed",
                "duration": 0.0007943519999571436,
                "start": 1784212044.4927833,
                "stop": 1784212044.4940548,
                "retries": 0,
                "file_path": "test_outputs.py"
            }
        ]
    }
}
```

**Summary:** All 5 tests **PASSED** in 0.049 seconds. Reward = **1** (competent solution).

---

## Run 2: No-Op Agent — harbor run -p log-report --agent nop

### reward.txt
```
0
```

### ctrf.json (Common Test Report Format)
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
            "pending": 0,
            "other": 0,
            "start": 1784212054.9646137,
            "stop": 1784212055.069249
        },
        "tests": [
            {
                "name": "test_outputs.py::test_report_exists",
                "status": "failed",
                "raw_status": "call_failed",
                "duration": 0.0011044209995816345,
                "start": 1784212054.9960837,
                "stop": 1784212055.0284157,
                "retries": 0,
                "file_path": "test_outputs.py",
                "trace": "/tests/test_outputs.py:7: in test_report_exists\n    assert Path(\"/app/report.json\").exists(), \"no report.json found\"\nE   AssertionError: no report.json found\nE   assert False\nE    +  where False = exists()\nE    +    where exists = PosixPath('/app/report.json').exists\nE    +    where PosixPath('/app/report.json') = Path('/app/report.json')",
                "message": "The test failed in the call phase due to an assertion error"
            },
            {
                "name": "test_outputs.py::test_report_valid_json",
                "status": "failed",
                "raw_status": "call_failed",
                "duration": 0.000885164999999688,
                "start": 1784212055.0296564,
                "stop": 1784212055.0387478,
                "retries": 0,
                "file_path": "test_outputs.py",
                "trace": "/tests/test_outputs.py:12: in test_report_valid_json\n    with open(\"/app/report.json\") as f:\n         ^^^^^^^^^^^^^^^^^^^^^^^^\nE   FileNotFoundError: [Errno 2] No such file or directory: '/app/report.json'",
                "message": "The test failed in the call phase"
            },
            {
                "name": "test_outputs.py::test_report_required_fields",
                "status": "failed",
                "raw_status": "call_failed",
                "duration": 0.000809611000249788,
                "start": 1784212055.0400631,
                "stop": 1784212055.0485852,
                "retries": 0,
                "file_path": "test_outputs.py",
                "trace": "/tests/test_outputs.py:19: in test_report_required_fields\n    with open(\"/app/report.json\") as f:\n         ^^^^^^^^^^^^^^^^^^^^^^^^\nE   FileNotFoundError: [Errno 2] No such file or directory: '/app/report.json'",
                "message": "The test failed in the call phase"
            },
            {
                "name": "test_outputs.py::test_report_field_types",
                "status": "failed",
                "raw_status": "call_failed",
                "duration": 0.0006901840001773962,
                "start": 1784212055.0497932,
                "stop": 1784212055.0594258,
                "retries": 0,
                "file_path": "test_outputs.py",
                "trace": "/tests/test_outputs.py:28: in test_report_field_types\n    with open(\"/app/report.json\") as f:\n         ^^^^^^^^^^^^^^^^^^^^^^^^\nE   FileNotFoundError: [Errno 2] No such file or directory: '/app/report.json'",
                "message": "The test failed in the call phase"
            },
            {
                "name": "test_outputs.py::test_report_reasonable_values",
                "status": "failed",
                "raw_status": "call_failed",
                "duration": 0.0008484950001275138,
                "start": 1784212055.0606585,
                "stop": 1784212055.069056,
                "retries": 0,
                "file_path": "test_outputs.py",
                "trace": "/tests/test_outputs.py:37: in test_report_reasonable_values\n    with open(\"/app/report.json\") as f:\n         ^^^^^^^^^^^^^^^^^^^^^^^^\nE   FileNotFoundError: [Errno 2] No such file or directory: '/app/report.json'",
                "message": "The test failed in the call phase"
            }
        ]
    }
}
```

**Summary:** All 5 tests **FAILED** in 0.104 seconds. Reward = **0** (no solution, no output).

---

## Verification

✓ **Honest grading**: Oracle returns reward 1, no-op returns reward 0  
✓ **Strong verifier**: 5 specific tests validate JSON structure, fields, and types  
✓ **Harbor format**: Both reward.txt and ctrf.json written to `/logs/verifier/` with correct exit codes  
✓ **Reproducible**: Environment uses pinned base image digest  
✓ **No solution leak**: No reference implementation in environment image  

Task is now correct and ready for production Harbor runs.
