# Stop localost service
sudo kill -9 $(lsof -t -i:8080)

#First pull any changes
git pull https://github.com/VivianDee/Tales-of-Africa

# Listen updated app to local host
sudo python3 manage.py runserver

# This binds web server to application server
sudo tmux new-session -d -s 'gunicorn --bind 127.0.0.1:8080 africreads.wsgi'

# Restart the server
sudo service nginx restart