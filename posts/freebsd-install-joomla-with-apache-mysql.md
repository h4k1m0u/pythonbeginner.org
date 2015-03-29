## Install Apache, MySQL and PhpMyAdmin:

See <a href="/freebsd-install-apache-mysql-php-phpmyadmin" target="_blank">Installation of Apache, MySQL and PhpMyAdmin</a>.

## Get Joomla:

-- Go to <a href="http://www.joomla.org/download.html" target="_blank">Download Joomla</a> to get `Joomla`.

-- Extract the `Joomla` zip archive into `/usr/local/www`:

    unzip -d /usr/local/www/joomla.loc/ ~/Downloads/Joomla_3.4.1-Stable-Full_Package.zip
    

<!--more-->

-- Change permissions of the folder to `Apache` user and group:

    chown -R www:www joomla.loc/
    

## Create an Apache vhost for Joomla:

-- Add this line to `/etc/hosts`, to have the local domain name recognized:

    127.0.0.1       joomla.loc
    

-- You have to be sure that `vhosts` support is enabled in `Apache`. Open `/usr/local/etc/apache24/httpd.conf` and verify that this line is uncommented:

    Include etc/apache24/extra/httpd-vhosts.conf
    

-- Start adding your `vhost` by adding to `/usr/local/etc/apache24/extra/httpd-vhosts.conf` the following:

    <VirtualHost *:80>
        DocumentRoot "/usr/local/www/joomla.loc"
        ServerName joomla.loc
        ErrorLog "/var/log/httpd-joomla.loc-error_log"
        CustomLog "/var/log/httpd-joomla.loc-access_log" common
        <Directory "/usr/local/www/joomla.loc">
            AllowOverride All
            Require local
        </Directory>
    <VirtualHost *:80>
    

-- Open `joomla.loc` on your browser. If you encounter an error related to `sessions` or `xml` (and you will):

    Fatal error: Call to undefined function session_id()
    Fatal error: Call to undefined function simplexml_load_file()
    

It means that you have to install basic `PHP` modules (session, xml...), those modules are also needed by `Joomla`:

    pkg install php56-extensions
    

-- If you go to `joomla.loc` on your browser, you could start the `Joomla` installation process. You won't have to create a `MySQL` database in `PhpMyAdmin`, you just need to provide `Joomla` with your `MySQL` credentials and it will create a database for you.

<img class="post-image" src="/wp-content/uploads/2015/03/freebsd-install-joomla-with-apache-mysql-result.png" title="Freebsd - Finished Joomla Installation" />
