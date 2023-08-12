#!/bin/bash

# Copy new files to the Nginx web server directory
sudo cp -r $(Build.ArtifactStagingDirectory) /var/www/html/

# Restart Nginx
sudo systemctl restart nginx
