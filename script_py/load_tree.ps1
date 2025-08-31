function Show-Tree($path, $indent = "") {
     Get-ChildItem $path | Where-Object { $_.Name -ne "node_modules" } | ForEach-Object {
         Write-Host "$indent├── $($_.Name)"
         if ($_.PSIsContainer) {
             Show-Tree $_.FullName "$indent│   "
         }
     }
 }
 
Show-Tree