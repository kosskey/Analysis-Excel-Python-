rem pip install virtualenv
::pip install virtualenv

python -m venv .\env
.\env\Scripts\activate
python -m pip install --upgrade pip
pip install -r .\requirements.txt