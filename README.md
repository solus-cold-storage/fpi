fpi
----

FPI is the `Foreign Package Installer`, an `alien`-like utility for Solus that
converts between package formats. The initial idea is to convert `.deb` files
into native `.eopkg` files for installation on Solus. This is used in more
extreme situations where certain packages are not readily usable on Solus due to
being restricted in format and distribution. The main goal is in providing the
user with at least _some method_ to install the packages locally.

Long story short, users will be able to download those previously inaccessible
`.deb` files through their browser and install it with FPI with no fuss or
interference.

![evil](https://raw.githubusercontent.com/solus-project/fpi/master/.github/9KCIeJi.gif)


Planned Dependencies
--------------------

 * `ypkg` (to convert to `.eopkg`)
 * `ar` from `binutils` (extract `.deb`)
 * `tar` (extract `.deb` innards.)
 * Python. I know, I'm sorry. But `eopkg` is still Pythonic at this moment in time.

License
-------

fpi is available under the terms of the `GPL-2.0` license.

Copyright © 2017 Ikey Doherty

