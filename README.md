# Assignment 6: MLOps CI/CD with Gatekeeper Logic

## Overview

This project implements a resource-efficient CI/CD pipeline with strict conditional execution to prevent wasted GPU compute on broken code or unauthorized branches.

## Workflow Architecture

### Pipeline: `.github/workflows/pipeline.yaml`

The workflow implements a **three-layer Gatekeeper system**:

#### Layer 1: Linter Job (Lightweight Guard)
- Runs on all pushes to `main` and `develop` branches
- Performs code quality checks before expensive training
- `train` job depends on this via `needs: [linter]`
- Prevents broken code from reaching GPU training

#### Layer 2: Branch Protection
- `train` job only executes on the `main` branch
- Condition: `github.ref == 'refs/heads/main'`
- Prevents unauthorized development branches from consuming GPU resources

#### Layer 3: Manual Intent Verification
- Commit message must explicitly contain `[run-train]` keyword
- Condition: `contains(github.event.head_commit.message, '[run-train]')`
- Provides explicit developer control over when expensive runs execute

### Key Conditions on `train` Job
```yaml
if: github.ref == 'refs/heads/main' && contains(github.event.head_commit.message, '[run-train]')
```

All three conditions must be met:
1. ✅ `linter` job must pass (dependency)
2. ✅ Code must be on `main` branch
3. ✅ Commit message must contain `[run-train]`

## Error Handling & Artifacts

### Failure Step
```yaml
- name: Log failure details
  if: failure()
  run: |
    # Creates error_logs.txt with detailed diagnostic information
```

### Artifact Upload
```yaml
- name: Upload error logs as artifact
  if: failure()
  uses: actions/upload-artifact@v3
  with:
    name: training-error-logs
    path: error_logs.txt
    retention-days: 30
```

Developers can download `error_logs.txt` from the GitHub Actions UI without re-running the expensive GPU job.

## Cleanup Step

```yaml
- name: Cleanup temporary cloud volumes
  if: always()
  run: |
    echo "Cleaning up temporary cloud volumes..."
```

This runs **regardless of success or failure**, ensuring temporary resources are always cleaned up.

## How to Test

### Test 1: Skip Training (No [run-train] Tag)
```bash
# Commit to main without [run-train] in message
git add .
git commit -m "Update model configuration"
git push origin main
```

**Expected Behavior:**
- ✅ `linter` job runs and passes
- ⏭️ `train` job is **SKIPPED** (appears grey/skipped in GitHub Actions UI)
- Reason: Commit message doesn't contain `[run-train]`

### Test 2: Run Training (With [run-train] Tag)
```bash
# Commit to main WITH [run-train] in message
git add .
git commit -m "Improve model accuracy [run-train]"
git push origin main
```

**Expected Behavior:**
- ✅ `linter` job runs and passes
- ▶️ `train` job runs (will simulate random failure 70% of the time for demo)
- If fails: `error_logs.txt` artifact is uploaded automatically

### Test 3: Branch Protection (develop branch)
```bash
# Commit to develop with [run-train] tag
git add .
git commit -m "WIP: new feature [run-train]"
git push origin develop
```

**Expected Behavior:**
- ✅ `linter` job runs (develop branch is allowed)
- ⏭️ `train` job is **SKIPPED** (branch is not `main`)

## Resource Cost Savings

By implementing this gatekeeper logic:

- ❌ **Before:** GPU training runs on every push, even with lint errors or on feature branches
  - Cost: $X per failed run × 50 commits/day = Wasted $50X/day

- ✅ **After:** GPU training only runs on explicit intent to `main` branch
  - Cost: Only intentional runs with explicit `[run-train]` tag
  - Savings: ~80-90% reduction in compute costs

## Files Created

```
Assignment 6 MLOps/
├── .github/
│   └── workflows/
│       └── pipeline.yaml          # Main CI/CD workflow
└── README.md                       # This file
```

## GitHub Actions UI Screenshots

### Screenshot 1: Job Skipped (No [run-train])
When you push to `main` WITHOUT `[run-train]` in commit message:
- The `train` job will appear with a **yellow/grey "Skipped" badge**
- Hover over it to see the skipped reason
- The `linter` job will have a green checkmark

### Screenshot 2: Job Running (With [run-train])
When you push to `main` WITH `[run-train]` in commit message:
- The `train` job will execute (blue "In progress" or complete)
- If it fails, an artifact will be available for download

## Instructions for Screenshot Submission

1. Commit and push to your repository's `main` branch **without** `[run-train]` tag
2. Go to GitHub repository → Actions tab
3. Find the most recent workflow run
4. Take a screenshot showing the skipped `train` job
5. The screenshot should clearly show:
   - ✅ `linter` job with green checkmark
   - ⏭️ `train` job with "Skipped" badge
   - The reason for skip in the job details (condition not met)

## Troubleshooting

**Q: Why is my train job still running on non-main branches?**
- A: Ensure you pushed to the `main` branch. Check `github.ref` in job logs.

**Q: The [run-train] tag isn't being detected**
- A: Verify the commit message contains exactly `[run-train]` (case-sensitive)
- Note: For squash/rebase commits, the tag must be in the final commit message

**Q: How do I download the error logs?**
- A: After a failed `train` job, go to the workflow run → Artifacts section → Download `training-error-logs.zip`

## Testing Gatekeeper Logic

This shows resource governance in action.
