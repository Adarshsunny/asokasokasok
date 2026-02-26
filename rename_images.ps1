$i = 5
Get-ChildItem -Path d:\porfolio\portfolio\WhatsApp*.jpeg | Sort-Object Name | ForEach-Object {
    Rename-Item $_.FullName -NewName ('gallery-' + $i + '.jpg')
    $i++
}
