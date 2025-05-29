## Installation instructions
Open a Windows PowerShell.

Download Microphone repository.

```
git clone git@github.com:Nush395/Microphone.git
```

Step into the repo and create a virtual environment and install 
necessary dependencies.
```
pip install -e .
```

### Install FFMPEG on Windows using Scoop (https://scoop.sh/)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install ffmpeg
```

## Running transcribe tool
```
python microphone transcribe.py -h
```