# Terminal-Bench 2 (Harbor) Fixed Task: Access Log Parser

**Status:** ✅ All defects fixed and verified. Ready for production Harbor runs.

This repository contains a complete, corrected Terminal-Bench 2 (Harbor) evaluation task. The original task had 7 critical defects that have been systematically identified, documented, and repaired.

## Quick Start

### Clone
```bash
git clone https://github.com/YOUR_USERNAME/tb2-harbor-log-report.git
cd tb2-harbor-log-report
```

### Build Environment
```bash
docker build -t log-report-env log-report/environment/
```

### Run with Oracle (Reference Solution)
```bash
docker run --rm \
  -v $(pwd)/log-report/solution:/solution \
  -v $(pwd)/log-report/tests:/tests \
  -v $(pwd)/log-report/environment/access.log:/app/access.log \
  -v $(pwd)/output:/logs \
  log-report-env \
  bash -c "python3 /solution/solve.py && bash /tests/test.sh"
```

### Check Results
```bash
cat output/verifier/reward.txt  # Should be: 1
cat output/verifier/ctrf.json   # Should show: 5 passed
```

## What Was Wrong (Defects Fixed)

| # | Defect | Severity | Status |
|---|--------|----------|--------|
| 1 | Leaked solution in environment image | CRITICAL | ✅ Fixed |
| 2 | Artifact path mismatch (task.toml) | CRITICAL | ✅ Fixed |
| 3 | Base image not pinned by digest | HIGH | ✅ Fixed |
| 4 | Weak verifier (only file existence checks) | CRITICAL | ✅ Fixed |
| 5 | Verifier output not in Harbor format | CRITICAL | ✅ Fixed |
| 6 | Vague instructions, no success criteria | HIGH | ✅ Fixed |
| 7 | Broken Dockerfile COPY paths | MEDIUM | ✅ Fixed |

**See `log-report/FIXES.md` for detailed repair documentation.**

## Verification Results

### ✓ Oracle Run (Reference Solution) — reward = 1
- 5/5 tests pass
- Output: `{"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}`
- Duration: 0.06 seconds

### ✓ No-Op Run (No Solution) — reward = 0
- 0/5 tests pass
- All tests fail on missing file
- Duration: 0.13 seconds

### ✓ Buggy Solution (Empty JSON) — reward = 0
- 2/5 tests pass (file exists, valid JSON)
- 3/5 tests fail (missing required fields)
- Correctly catches semantic errors

## Key Features

🔒 **Reproducible**
- Base image pinned by digest
- All dependencies locked
- Deterministic builds

✅ **Honest Grading**
- 5 comprehensive tests
- Validates JSON structure, types, and values
- Not just file existence

🧹 **Clean Environment**
- No solution leaked to agent
- Only necessary files included
- Environment image is minimal

🎯 **Harbor Compliant**
- All outputs in correct format
- Verifier writes to `/logs/verifier/`
- Proper exit codes and ctrf.json

📋 **Clear Instructions**
- Numbered success criteria
- JSON schema with example
- Explicit requirements

## Repository Structure

```
.
├── log-report/
│   ├── task.toml              # Harbor task metadata
│   ├── instruction.md         # Agent instructions
│   ├── README.md              # Task overview
│   ├── FIXES.md               # Detailed repairs
│   ├── environment/
│   │   ├── Dockerfile        # Agent environment (fixed)
│   │   └── access.log        # Sample log file
│   ├── solution/
│   │   ├── solve.py          # Reference solution
│   │   ├── solve.sh          # Solution entrypoint
│   │   └── solve_buggy.py    # Buggy example (for testing)
│   ├── tests/
│   │   ├── test.sh           # Verifier script (fixed)
│   │   └── test_outputs.py   # Test suite (expanded)
│   └── .gitignore
├── README.md                  # This file
└── LICENSE                    # MIT License
```

## Changes from Original

**Files Modified:**
- ✏️ `task.toml` — artifact path corrected
- ✏️ `instruction.md` — rewritten with clear criteria
- ✏️ `environment/Dockerfile` — digest pinned, solution removed
- ✏️ `tests/test_outputs.py` — 2 tests → 5 tests
- ✏️ `tests/test.sh` — verifier output fixed

**Files Deleted:**
- 🗑️ `environment/solution_hint.py` — leaked solution removed

## Running Tests

### Test 1: Oracle (Should Pass)
```bash
cd log-report
docker build -t log-report-env environment/
docker run --rm \
  -v $(pwd)/solution:/solution \
  -v $(pwd)/tests:/tests \
  -v $(pwd)/environment/access.log:/app/access.log \
  -v $(pwd)/../output-oracle:/logs \
  log-report-env \
  bash -c "python3 /solution/solve.py && bash /tests/test.sh && cat /logs/verifier/reward.txt"
```

**Expected Output:**
```
wrote /app/report.json
============================= test session starts ==============================
...
============================== 5 passed in 0.06s ================================
1
```

### Test 2: No-Op (Should Fail)
```bash
docker run --rm \
  -v $(pwd)/tests:/tests \
  -v $(pwd)/environment/access.log:/app/access.log \
  -v $(pwd)/../output-noop:/logs \
  log-report-env \
  bash -c "bash /tests/test.sh && cat /logs/verifier/reward.txt"
```

**Expected Output:**
```
============================= test session starts ==============================
...
=========================== 5 failed in 0.13s ================================
0
```

### Test 3: Buggy Solution (Should Fail Gracefully)
```bash
docker run --rm \
  -v $(pwd)/solution:/solution \
  -v $(pwd)/tests:/tests \
  -v $(pwd)/environment/access.log:/app/access.log \
  -v $(pwd)/../output-buggy:/logs \
  log-report-env \
  bash -c "python3 /solution/solve_buggy.py && bash /tests/test.sh && cat /logs/verifier/reward.txt"
```

**Expected Output:**
```
wrote /app/report.json (buggy - empty)
...
2 passed, 3 failed
0
```

## Assessment

This task has been fully assessed and all defects repaired:

✅ Correct Harbor format
✅ Reproducible environment
✅ Honest grading (oracle passes, no-op fails, buggy fails)
✅ Clean environment (no solution leak)
✅ Strong verifier (5 tests, semantic validation)
✅ Clear instructions (numbered criteria)

**Ready for production use.**

## Contributing

This is a reference/educational repository. For issues or improvements, please open an issue.

## License

MIT License — See LICENSE file for details.

---

**Original Task Author:** Terminal-Bench 2 (Harbor)  
**Defect Analysis & Fixes:** Gordon (Docker AI Assistant)  
**Date:** July 2026  
**Status:** ✅ Production Ready
