$evidence = Join-Path $PSScriptRoot "simulated_server_image.bin"
$manifest = Join-Path $PSScriptRoot "SHA256SUMS.txt"
if (!(Test-Path $evidence) -or !(Test-Path $manifest)) {
    Write-Host "FAIL: Evidence or manifest missing" -ForegroundColor Red
    exit 1
}
$line = Get-Content $manifest |
    Where-Object { $_ -match 'simulated_server_image\.bin$' } |
    Select-Object -First 1
if (!$line) {
    Write-Host "FAIL: Manifest entry missing" -ForegroundColor Red
    exit 1
}
$expected = ($line -split '\s+')[0]
$actual = (Get-FileHash $evidence -Algorithm SHA256).Hash
if ($expected -eq $actual) {
    Write-Host "PASS: SHA-256 hashes match!" -ForegroundColor Green
    exit 0
} else {
    Write-Host "FAIL: SHA-256 hashes differ!" -ForegroundColor Red
    exit 1
}
