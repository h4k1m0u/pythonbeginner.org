In all these examples, you could unmount mounted device afterwards using:

    umount /mnt/<mount-point>
    

## Mounting a Windows NTFS partition:

We are going to use the `ntfs-3g` read/write `NTFS` driver, which provides easy handling of `Windows` partitions.

-- First install `ntfs-3g`:

    pkg install fusefs-ntfs
    

-- Since `ntfs-3g` depends upon the `fuse` kernel module, we have to load the latter on boot. Open `/etc/rc.conf` and add `fuse` to the list of kernels to load on startup:

    kld_list="... fuse ..."
    

-- Mount your `NTFS` partition (In my case it's the first partition right after the bootloader):

    ntfs-3g /dev/ada0s1 /mnt/win
    

## Mounting a CD-ROM/DVD:

-- Create a mount point in `/mnt/`:

    mkdir /mnt/cd
    

-- Mount the disk `/dev/cd0` with the type of filesystem `cd9660`:

    mount -t cd9660 /dev/cd0 /mnt/cd
    

## Mounting USB Drives:

-- At first, confirm that your usb drive has been recognized. If so it will show up on the list when you type:

    usbconfig
    

-- Create a mount point in `/mnt/`:

    mkdir /mnt/usb
    

-- Mount the device `/dev/da0` with the type of filesystem `msdosfs`:

    mount -t msdosfs /dev/da0 /mnt/usb
    

## Mounting ISO images:

-- Start by creating a `memory disk` for the `ISO` file. This `memory disk` will be mounted instead of the `ISO` file. Note that we provide our `memory disk` with a unit number `-u 0` to identify it later:

    mdconfig -f file.iso -u 0
    

-- Create a mount point in `/mnt`:

    mkdir /mnt/iso
    

-- Mount your `memory disk` `/dev/md0` with the type of filesystem `cd9660`:

    mount -t cd9660 /dev/md0 /mnt/iso
    

-- Once you have finished with the `memory disk` `/dev/md0`, you have to delete it by providing its unit number `-u 0`:

    mdconfig -d -u 0
    

## Mounting an Android device:

We are going to use a gui mtp client `gmtp`.

-- Install `gmtp`:

    pkg install gmtp
    

-- Then run it as a superuser:

    sudo gmtp
    

-- Finally connect to your device and start downloading/uploading from/to it.

<img class="post-image" src="/wp-content/uploads/2015/03/gmtp.png" title="gmtp" />
