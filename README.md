Installation instructions

pip install -e .

### on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

### on Windows using Scoop (https://scoop.sh/)
Open Windows PowerShell
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install ffmpeg
```