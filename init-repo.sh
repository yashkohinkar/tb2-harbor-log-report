#!/bin/bash
# Initialize git repository for TB2 Harbor Fixed Task

cd "$(dirname "$0")"

# Initialize git
git init

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

Verification:
- Oracle run: 5/5 tests PASS → reward 1
- No-op run: 0/5 tests PASS → reward 0
- Buggy run: 2/5 tests PASS → reward 0 (catches errors)

Status: Production ready
"

echo ""
echo "✅ Git repository initialized"
echo ""
echo "To push to GitHub:"
echo "  git remote add origin https://github.com/YOUR_USERNAME/tb2-harbor-log-report.git"
echo "  git branch -M main"
echo "  git push -u origin main"
echo ""
echo "After passing assessment, make private with:"
echo "  gh repo edit tb2-harbor-log-report --visibility private"
echo ""
