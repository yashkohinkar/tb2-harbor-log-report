# Harbor Task: Parse Access Log to JSON Report (Fixed)

This is a **corrected Terminal-Bench 2 (Harbor) task** that was originally broken in 7 critical ways. All defects have been identified, fixed, and verified.

## Task Summary

**Objective:** Parse an Apache-style HTTP access log and generate a JSON summary report with request counts, unique client IPs, and the most popular path.

**Artifact:** `/app/report.json` (JSON file with `total_requests`, `unique_ips`, `top_path`)

**Difficulty:** Easy (0.3 hours expert time)

**Category:** Data Processing & ETL

## Defects Fixed

| # | Defect | Severity | Fix |
|---|--------|----------|-----|
| 1 | Leaked solution in environment image | CRITICAL | Removed `solution_hint.py` COPY from Dockerfile |
| 2 | Artifact path mismatch (task.toml vs reality) | CRITICAL | Updated to `/app/report.json` |
| 3 | Base image not pinned by digest | HIGH | Pinned to `python:3.12.8@sha256:e74938514dc67ad3eade8798aa929f5dd569e463758c83243636d4e1b54aa559` |
| 4 | Weak verifier (only file existence checks) | CRITICAL | Expanded to 5 tests validating JSON structure and types |
| 5 | Verifier output not in Harbor format | CRITICAL | Corrected paths to `/logs/verifier/reward.txt` and `ctrf.json` |
| 6 | Vague instructions, no success criteria | HIGH | Rewrote with numbered criteria and JSON schema |
| 7 | Dockerfile COPY references broken paths | MEDIUM | Removed invalid references |

## Repository Structure

```
log-report/
├── task.toml                    # Harbor task metadata (FIXED)
├── instruction.md               # Task instructions (REWRITTEN)
├── environment/
│   ├── Dockerfile              # Agent environment image (FIXED - pinned digest, no leak)
│   ├── access.log              # Sample access log for agent
│   └── solution_hint.py         # ⚠️ REMOVED (was leaked)
├── solution/
│   ├── solve.py                # Reference implementation
│   ├── solve.sh                # Solution entrypoint
│   └── solve_buggy.py          # Demo of buggy solution (for assessment)
├── tests/
│   ├── test.sh                 # Verifier script (FIXED - writes Harbor format)
│   └── test_outputs.py         # Test suite (EXPANDED to 5 tests)
├── README.md                   # This file
├── FIXES.md                    # Detailed repair documentation
└── .gitignore                  # Git ignore rules
```

## Verification

### ✓ Oracle Run (Reference Solution)
```
reward.txt: 1
ctrf.json: 5 passed, 0 failed
Output: {"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}
```

### ✓ No-Op Run (No Solution)
```
reward.txt: 0
ctrf.json: 0 passed, 5 failed
All tests fail on file not found
```

### ✓ Buggy Solution (Empty JSON)
```
reward.txt: 0
ctrf.json: 2 passed, 3 failed
Catches missing required fields
```

## Key Features

- **Reproducible:** Base image pinned by digest
- **Honest Grading:** Verifier validates content, not just file existence
- **Clean Environment:** No solution leaked to agent
- **Harbor Compliant:** All outputs in correct format and paths
- **Strong Tests:** 5 tests covering existence, structure, types, and values

## Running the Task

### Build Environment
```bash
docker build -t log-report-env environment/
```

### Run Oracle (should pass)
```bash
docker run --rm \
  -v $(pwd)/solution:/solution \
  -v $(pwd)/tests:/tests \
  -v $(pwd)/environment/access.log:/app/access.log \
  -v $(pwd)/output:/logs \
  log-report-env \
  bash -c "python3 /solution/solve.py && bash /tests/test.sh"
```

### Verify Output
```bash
cat output/verifier/reward.txt  # Should be: 1
cat output/verifier/ctrf.json   # Should show 5 passed
```

## Files Modified from Original

- ✏️ `task.toml` — artifact path corrected
- ✏️ `instruction.md` — rewritten with clear success criteria
- ✏️ `environment/Dockerfile` — pinned digest, removed leaked file
- ✏️ `tests/test_outputs.py` — expanded from 2 to 5 tests
- ✏️ `tests/test.sh` — fixed verifier output paths and error handling
- ✏️ `environment/solution_hint.py` — **DELETED** (was leaked)

## Assessment Results

All defects identified, fixed, and verified. Task now passes both oracle and no-op runs correctly.

See `FIXES.md` for detailed repair documentation and full test output.
