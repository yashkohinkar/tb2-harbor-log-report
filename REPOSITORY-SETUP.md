# GitHub Repository Setup Guide

This document explains how to create and configure the GitHub repository for this fixed Harbor task.

## Prerequisites

- GitHub account
- Git installed locally
- Docker installed
- GitHub CLI (optional, for privacy settings)

## Step 1: Create GitHub Repository

### Via GitHub Web UI
1. Go to https://github.com/new
2. Repository name: `tb2-harbor-log-report`
3. Description: "Terminal-Bench 2 (Harbor) Fixed Task: Access Log Parser"
4. Choose **Public** (for now; will make private after assessment passes)
5. Initialize with: **No** (we have local files)
6. Click **Create repository**

### Via GitHub CLI
```bash
gh repo create tb2-harbor-log-report \
  --public \
  --source=. \
  --description "Terminal-Bench 2 (Harbor) Fixed Task: Access Log Parser" \
  --push
```

## Step 2: Initialize Local Git Repository

```bash
cd /path/to/fix-task-broken

# Initialize git
git init

# Configure git (if not already done)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add -A

# Create initial commit
git commit -m "fix: Complete repair of Harbor task - all 7 defects fixed

Defects resolved:
1. REMOVED leaked solution from environment image
2. FIXED artifact path mismatch (task.toml)
3. PINNED base image by digest (reproducibility)
4. EXPANDED verifier from 2 to 5 semantic tests
5. CORRECTED verifier output to Harbor format
6. REWROTE instructions with numbered criteria
7. REMOVED broken Dockerfile COPY paths

Status: Production ready for Harbor runs"
```

## Step 3: Add Remote and Push

```bash
# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/tb2-harbor-log-report.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 4: Verify Repository

Visit `https://github.com/YOUR_USERNAME/tb2-harbor-log-report`

You should see:
- ✅ All files present
- ✅ README.md displayed
- ✅ Correct commit message
- ✅ Public visibility

## Step 5: Run Final Verification Tests

Before making private, verify task works with Harbor:

### Test 1: Oracle Run
```bash
cd log-report
docker build -t log-report-env environment/
docker run --rm \
  -v $(pwd)/solution:/solution \
  -v $(pwd)/tests:/tests \
  -v $(pwd)/environment/access.log:/app/access.log \
  -v $(pwd)/../output:/logs \
  log-report-env \
  bash -c "python3 /solution/solve.py && bash /tests/test.sh"

# Check result
cat ../output/verifier/reward.txt  # Should output: 1
```

### Test 2: No-Op Run
```bash
docker run --rm \
  -v $(pwd)/tests:/tests \
  -v $(pwd)/environment/access.log:/app/access.log \
  -v $(pwd)/../output:/logs \
  log-report-env \
  bash -c "bash /tests/test.sh"

# Check result
cat ../output/verifier/reward.txt  # Should output: 0
```

## Step 6: Submit for Assessment

Provide this link to the assessment:
```
https://github.com/YOUR_USERNAME/tb2-harbor-log-report
```

## Step 7: After Assessment Passes - Make Private

Once assessment confirms task is correct:

### Via GitHub CLI
```bash
gh repo edit tb2-harbor-log-report --visibility private
```

### Via GitHub Web UI
1. Go to https://github.com/YOUR_USERNAME/tb2-harbor-log-report
2. Settings → General
3. Scroll to "Danger Zone"
4. Click "Change visibility"
5. Select "Private"
6. Confirm

## Repository Structure (What Reviewers See)

```
tb2-harbor-log-report/
├── README.md                    # Overview and quick start
├── LICENSE                      # MIT License
├── init-repo.sh                 # Repository initialization script
├── REPOSITORY-SETUP.md          # This file
├── log-report/
│   ├── task.toml               # Harbor task metadata
│   ├── instruction.md          # Agent instructions (FIXED)
│   ├── README.md               # Task-specific overview
│   ├── FIXES.md                # Detailed repair documentation
│   ├── .gitignore
│   ├── environment/
│   │   ├── Dockerfile         # Agent environment (FIXED)
│   │   └── access.log         # Sample data
│   ├── solution/
│   │   ├── solve.py           # Reference solution
│   │   ├── solve.sh           # Solution entrypoint
│   │   └── solve_buggy.py     # Buggy example for testing
│   └── tests/
│       ├── test.sh            # Verifier script (FIXED)
│       └── test_outputs.py    # Test suite (EXPANDED)
├── oracle-final/               # (After running tests)
│   └── verifier/
│       ├── reward.txt
│       └── ctrf.json
├── noop-final/                 # (After running tests)
│   └── verifier/
│       ├── reward.txt
│       └── ctrf.json
└── REPOSITORY-SETUP.md         # This setup guide
```

## Verification Checklist

- [ ] GitHub repository created
- [ ] Local git initialized
- [ ] All files committed and pushed
- [ ] Repository is public
- [ ] README.md displays correctly
- [ ] Oracle run passes (reward = 1)
- [ ] No-op run fails (reward = 0)
- [ ] Assessment confirms all defects fixed
- [ ] Repository made private (post-assessment)

## Files Included

### Documentation
- `README.md` — Repository overview and quick start
- `LICENSE` — MIT License
- `log-report/README.md` — Task-specific overview
- `log-report/FIXES.md` — Detailed repair documentation

### Task Files
- `log-report/task.toml` — Harbor task metadata (FIXED)
- `log-report/instruction.md` — Agent instructions (REWRITTEN)
- `log-report/environment/Dockerfile` — Agent environment (PINNED, CLEANED)
- `log-report/environment/access.log` — Sample access log
- `log-report/solution/solve.py` — Reference solution
- `log-report/solution/solve.sh` — Solution entrypoint
- `log-report/solution/solve_buggy.py` — Buggy example for testing
- `log-report/tests/test.sh` — Verifier script (FIXED)
- `log-report/tests/test_outputs.py` — Test suite (EXPANDED)

### Configuration
- `.gitignore` — Git ignore patterns
- `init-repo.sh` — Repository initialization script

## Defects Fixed (Summary for Reviewers)

| # | Defect | Severity | Fix |
|---|--------|----------|-----|
| 1 | Leaked solution in environment | CRITICAL | Removed COPY line; verified with `docker run ... ls /app` |
| 2 | Artifact path mismatch | CRITICAL | Updated task.toml: `/app/out.json` → `/app/report.json` |
| 3 | Base image not pinned | HIGH | Pinned to exact digest: `python:3.12.8@sha256:...` |
| 4 | Weak verifier (2 tests) | CRITICAL | Expanded to 5 tests with semantic validation |
| 5 | Verifier output wrong path | CRITICAL | Fixed to `/logs/verifier/reward.txt` + `ctrf.json` |
| 6 | Vague instructions | HIGH | Rewritten with numbered criteria and JSON schema |
| 7 | Broken Dockerfile paths | MEDIUM | Removed invalid COPY references |

## Assessment Verification

Before making private, confirm:

✅ Oracle run: 5/5 tests pass → reward = 1  
✅ No-op run: 0/5 tests pass → reward = 0  
✅ Environment: No solution leaked  
✅ Reproducible: Base image pinned by digest  
✅ Honest grading: Verifier validates content, not just files  

## Support

For issues or questions:
1. Check `log-report/FIXES.md` for detailed explanations
2. Review `log-report/README.md` for task overview
3. Check test output files in `oracle-final/`, `noop-final/` directories

---

**Ready to submit!** ✅

When you've completed all steps, provide the GitHub URL to your assessor.
After assessment passes, make the repository private.
