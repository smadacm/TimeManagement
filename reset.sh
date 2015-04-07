#!/usr/bin/env bash

# Clear DB
rm timemgt.db3

# Create DB
python manage.py makemigrations
python manage.py migrate

# Add initial Data
python init_data.py
find init_data.d -iname '*.py' -exec python {} \;

# Change ownership of db to Apache (Ubuntu 14.04)
chown :www-data timemgt.db3
chmod g+w timemgt.db3
