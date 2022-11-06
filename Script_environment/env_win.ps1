#pip install virtualenv

#$a = Get-Location
#cd $a

python -m venv .\env
.\env\Scripts\activate
python -m pip install --upgrade pip
pip install -r .\requirements.txt
