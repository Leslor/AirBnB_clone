#!/usr/bin/env bash
sudo apt update
sudo apt -y install dpkg
#Install Nginx if it not already installed
if ! dpkg -l nginx | grep nginx > /dev/null 2>&1; then
	sudo apt install -y nginx
fi
#Create the folder /data/ if it doesn’t already exist
#Create the folder /data/web_static/ if it doesn’t already exist
#Create the folder /data/web_static/releases/ if it doesn’t already exist
#Create the folder /data/web_static/shared/ if it doesn’t already exist
#Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
#Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)

echo "
<html>
	<head>
		<title>LesLor Page</title>
		<style>
			body{
				background-color: rgb(255, 105, 180);
				}
		</style>
	</head>
	<body>
		<h1>Hello World</h1>
		<p> 
			Trying to learn how to deploy a webr<br>
	        Just a test<br>
		</p>
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
ln -fs /data/web_static/releases/test/ /data/web_static/current
#Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
#	Use alias inside your Nginx configuration

echo "
server {
		listen 80 default_server;
		listen [::]:80 default_server;
		server_name _;
		add_header X-Served-By $HOSTNAME;

		root   /var/www/html;
		index  index.html index.htm;

		location /hbnb_static {
			alias /data/web_static/current;
			index index.html index.htm;
		}
}
" | sudo tee /etc/nginx/sites-available/default
# Restart Nginx
sudo service nginx restart
