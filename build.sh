set -o exit

pip install -r requirements.txt
python manage.py collectstatic
