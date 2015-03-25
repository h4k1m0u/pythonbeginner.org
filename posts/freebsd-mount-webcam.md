`pkg install webcamd`  
vim `/etc/rc.conf`:  
    - add to kernel modules: `kld_list="cuse4bsd"`  
    - load service on startup: `webcamd_enable="YES"`  
if no reboot:  
    - sudo webcamd (list available devices)  
    - sudo webcamd -d ugen7.2  
Open a new shell  
install webcam viewer client program: `pkg install pwcview`  
test webcam: `sudo pwcview`  
troubleshooting:  
dmesg (check if webcam is recognized)  
