`Lumina` is a new lightweight desktop environment based on `Qt`, which is available in `Freebsd` repository.

-- Install `Lumina` with the package manager:

    pkg install lumina
    

<!--more-->

-- Open `~/.xinitrc` and add this line at the end of the file:

    /usr/local/bin/Lumina-DE
    

-- After you log-in, you can start `Lumina` with this command:

    startx
