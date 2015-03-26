`Webcamd` is a daemon service that enables use of hundreds of different USB-based webcams under `FreeBSD`. See <a href="https://www.freshports.org/multimedia/webcamd/" target="_blank">Webcamd Port</a>. In this tutorial, we'll see how to configure the webcam under `Freebsd`.

We'll first install `webcamd` using `Freebsd` package manager:

    pkg install webcamd  
    

The `webcamd` daemon depends on the `Cuse4BSD` kernel module which allows userland programs (like `webcamd`) to create character devices under `/dev`. See <a href="http://www.freshports.org/multimedia/cuse4bsd-kmod/" target="_blank">Cuse4BSD Port</a>. If `Cuse4BSD` is not already installed, install it:

    pkg install cuse4bsd-kmod
    

After that, open `/etc/rc.conf`:  
And add the `Cuse4BSD` kernel module to the list of modules to load on startup, and `webcamd` to the list of services to start on boot:

    kld_list="... cuse4bsd"
    webcamd_enable="YES"
    

If you reboot your system, you could verify that each of `Cuse4BSD4` kernel module and `webcamd` service are running using:

    kldstat
    service webcamd status
    

To test your webcam, you'll need to install a webcam viewer like `pwcview`:

    pkg install pwcview
    

Now, run `pwcview` to be able to see your webcam's video stream on stdout:

    sudo pwcview
    

In order to run `pwcview` as a regular user (without root access), you will need to add your user to `webcamd` group:

    pw groupmod webcamd -m <your user>
