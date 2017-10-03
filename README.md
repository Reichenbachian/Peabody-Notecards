# Peabody Notecards Instruction Document

Currently our main code is stored in one app. By the Django documentation, one should keep things in a single app as long as they follow the same purpose, and currently all do.

The main app is dashboard. In future, as other supplementary apps are added, this document will be updated.

Make sure to create a virtual environment and install pip packages using "pip install -r requirements.txt". If you add new requirements, add it using "pip freeze > requirements.txt"

```
BASH SCRIPTS
	•	Ffempg convert .pdf to .pdf.png: for i in *; do for i2 in $i/*; do convert -density 300 -quality 100 $i2 $i2.png; done; done https://askubuntu.com/questions/50170/how-to-convert-pdf-to-image/50180
	•	Rename: for i in *; do mv "$i" "$(echo $i | cut -f3 -d' ')"; done;
	•	Delete PDF: find . -name "*.pdf" -delete
	•	Python manage.py shell, then csv script
 
SERVER
	•	service nginx restart
	•	Make sure screen is running with ini
	•	Crl+ad to exit screen (detach)
	•	Screen -r, do the git pull, then detach, make sure venv is running
```
