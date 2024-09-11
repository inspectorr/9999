#!/bin/bash
sudo apt-get update
sudo apt-get install -y nginx
sudo cp .deploy/nginx.conf /etc/nginx/sites-enabled/site.conf
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
