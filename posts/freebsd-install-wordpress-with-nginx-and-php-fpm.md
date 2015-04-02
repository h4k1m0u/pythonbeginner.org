## Install PHP-FPM, MySQL, Nginx services:

-- Note that the installation of `php56` will automatically install `php-fpm`.

    pkg install nginx php56 mysql56-server
    

-- To set `nginx`, `mysql` and `php-fpm` services to start on boot, open `/etc/rc.conf` and add:

    mysql_enable="YES"
    nginx_enable="YES"
    php_fpm_enable="YES"
    

<!--more-->

## Get Wordpress:

-- Go to <a href="https://wordpress.org/latest.zip" target="_blank">Download Wordpress</a> to get `Wordpress`.

-- Extract the `Wordpress` zip archive into `/usr/local/www`:

    unzip -d /usr/local/www/ ~/Downloads/wordpress-4.1.1.zip
    mv wordpress/ wordpress.loc/
    

-- Change permissions of the folder to `Apache` user and group:

    chown -R www:www wordpress.loc/
    

## Configure Nginx:

-- Add this line to `/etc/hosts`, to have the local domain name recognized:

    127.0.0.1       wordpress.loc
    

-- Add your host configuration to `nginx` by inserting in `/usr/local/etc/nginx/nginx.conf` between the `http {...}` block, the following:

    server {
        listen 80;
        server_name wordpress.loc;
    
        access_log /var/log/nginx-wordpress.loc-access_log;
        error_log /var/log/nginx-wordpress.loc-error_log;
    
        root /usr/local/www/wordpress.loc;
        index index.php index.html index.htm;
    
        location / {
            try_files $uri $uri/ /index.php?$args;
        }
    
        error_page 404 /404.html;
    
        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
            root /usr/local/www/nginx;
        }
    
        # pass the PHP scripts to FastCGI server listening on /var/run/php5-fpm.sock
        location ~ \.php$ {
            try_files $uri =404;
            fastcgi_pass unix:/var/run/php5-fpm.sock;
            fastcgi_index index.php;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_read_timeout 600s;
            client_max_body_size 20M;
            include fastcgi_params;
        }
    }
    

## Configure PHP-FPM:
`Nginx` will proxy `PHP` queries to `PHP-FPM` in a `Unix socket` file. This file needs to have the same permissions as `Nginx`. 
To make this configuration, open `/usr/local/etc/php-fpm.conf`:

-- For better performance, set `php-fpm` to listen on a `Unix socket` instead of a `TCP socket`, since `Nginx` and `PHP-FPM` are installed on the same machine:

    ; listen = 127.0.0.1:9000
    listen = /var/run/php5-fpm.sock   

-- Set the permissions for the `Unix socket` (`/var/run/php5-fpm.sock`), with the user and group of the Http server (`Nginx`):

    listen.owner = www
    listen.group = www
    listen.mode = 0660

-- If you go to `wordpress.loc` on your browser, you could start the `Wordpress` installation process. You will need to create a database for `Wordpress`.

In case, a `wordpress` plugin you installed require php's xml, json... functions, these could be available in `php56-extensions` which is installed with:

    pkg install php56-extensions
    

<img class="post-image" src="/wp-content/uploads/2015/04/freebsd-install-wordpress-with-nginx-and-php-fpm-result.png" title="Freebsd - Finished Wordpress Installation" />
