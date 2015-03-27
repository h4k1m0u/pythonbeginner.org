## Install Apache Httpd 2.4:

-- Install `Apache` using `freebsd`''s package manager:

    pkg install apache24
    
-- Start `Apache` service with:

    service apache24 start

<!--more-->
    
-- Open `/etc/rc.conf` and add the following to start `Apache` service on boot:

    apache24_enable="YES"

-- Open /usr/local/etc/apache24/httpd.conf:

-- Go to the `<IfModule dir_module>...</IfModule>` tag, and add inside it:

    DirectoryIndex index.php index.html

to set the file that `Apache` will serve if a directory is requested.

-- Go to the `<IfModule mime_module>...</IfModule>` tag, and add inside it:

    AddType application/x-httpd-php .php

to detect `PHP` files from their extension.

Now that `Apache` is configured, we''ll install `PHP` and its `Apache` module.
    
## Install PHP 5:

-- First, we install `PHP`:

    pkg install php5

-- Then `Apache`''s `PHP` module`:

    pkg install mod_php5

-- We need to create a `php.ini` file by copying php.ini-developement content:

    cp /usr/local/etc/php.ini-development /usr/local/etc/php.ini
    
## Install MySQL server:

Same installation as `Apache` and `PHP`:

    pkg install mysql56-server
    
-- Start `MySQL` service with:

    service mysql-server start

-- Open `/etc/rc.conf` and add the following to start `MySQL` service on boot:

    mysql_enable="YES"

## Install PhpMyAdmin:

    pkg install phpmyadmin

-- Add `PhpMyAdmin` alias to `/usr/local/etc/apache24/httpd.conf` between `<IfModule alias_module>...</IfModule>` tags:

    Alias /phpmyadmin "/usr/local/www/phpMyAdmin/"

    <Directory "/usr/local/www/phpMyAdmin/">
        AllowOverride All
        Require local
    </Directory>

You should now be able to access `PhpMyAdmin` in your browser at `localhost/phpmyadmin`, with your `MySQL` credentials.
