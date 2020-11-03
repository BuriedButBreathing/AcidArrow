Invoke-WebRequest -Uri https://i.imgur.com/7oMTBQM.jpg  -OutFile $env:TEMP\7oMTBQM.jpg
$rick = $env:TEMP + '\70MTBQM.jpg'
Set-ItemProperty -path 'HKCU:\Control Panel\Desktop\' -name wallpaper -value $rick
rundll32.exe user32.dll, UpdatePerUserSystemParameters
