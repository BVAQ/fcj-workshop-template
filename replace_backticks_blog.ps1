$files = Get-ChildItem -Path "d:\HK252\AWS\fcj-workshop-template\content\3-BlogsPosted" -Recurse -Filter "*.md"
foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $newContent = [regex]::Replace($content, '(?<!`)`([^`\r\n]+)`(?!`)', '**$1**')
    if ($content -cne $newContent) {
        [System.IO.File]::WriteAllText($file.FullName, $newContent, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($file.FullName)"
    }
}
