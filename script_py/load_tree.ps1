function Show-Tree($path, $indent = "") {
    Get-ChildItem $path | ForEach-Object {
        Write-Host "$indent├── $($_.Name)"
        if ($_.PSIsContainer) {
            Show-Tree $_.FullName "$indent│   "
        }
    }
}

Show-Tree
