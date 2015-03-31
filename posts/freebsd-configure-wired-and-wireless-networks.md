-- Before you start, you need to get your network interfaces names with:

    ifconfig
    

<!--more-->

My network interfaces are:

*   **Wired:** `bge0` (See <a href="https://www.freebsd.org/cgi/man.cgi?query=bge&apropos=0&sektion=0&manpath=FreeBSD+10.1-RELEASE&arch=default&format=html" target="_blank">Broadcom Gigabit/Fast Ethernet (bge) driver</a>).

*   **Wireless:** `iwn0` (See <a href="https://www.freebsd.org/cgi/man.cgi?query=iwn&apropos=0&sektion=0&manpath=FreeBSD+10.1-RELEASE&arch=default&format=html" target="_blank">Intel wireless network (iwn) driver</a>).

Note that I will be using static local ip addresses and `WPA` encryption for Wireless.

## Configure networking:

Set the default `route` in `/etc/rc.conf`:

    defaultrouter="<gateway ip address>"
    

### Wired networks:

Configure the Ethernet interface in `/etc/rc.conf` with:

    ifconfig_bge0="inet <local ip address> netmask <network mask>"
    

### Wireless networks:

Configure the Wireless interface in `/etc/rc.conf` with:

    wlans_iwn0=wlan0
    ifconfig_wlan0="WPA inet <local ip address> netmask <network mask>"
    

-- The modules that implement cryptographic support for the security protocols (`WPA` in my case) used in wireless networks must be manually loaded. Add these modules to the list of kernel modules to load on boot in `/etc/rc.conf`:

    kld_list="... wlan_wep wlan_tkip wlan_ccmp ..."
    

-- Wireless connection and key negotiation or authentication is done using `wpa_supplicant`. To configure it, open `/etc/wpa_supplicant.conf` and add your `Wi-Fi` network credentials:

    network={
        ssid="<Wi-Fi name>"
        psk="<Wi-Fi password>"
    }
    

## Configure DNS:

Open `/etc/resolv.conf` and add Google `DNS` servers' addresses:

    nameserver 8.8.8.8
    nameserver 8.8.4.4
