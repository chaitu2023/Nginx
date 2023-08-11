#!/bin/bash

# Copy new files to the Nginx web server directory
sudo cp -r /path/to/your/repo/* /var/www/html/

# Restart Nginx
sudo systemctl restart nginx
