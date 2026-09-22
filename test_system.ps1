$cfg = Get-Content -Raw "config.json" | ConvertFrom-Json
if ($cfg.passing_threshold_percentage -lt 0) {
    Write-Host "TEST FAILED: passing_threshold_percentage is negative: $($cfg.passing_threshold_percentage)"
    exit 1
} else {
    Write-Host "TEST PASSED: passing_threshold_percentage is $($cfg.passing_threshold_percentage)"
    exit 0
}
