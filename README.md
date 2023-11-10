# Zeus Package Manager

![Zeus Logo](zeus-logo1.png)

Zeus is a Package Manager for the [Athena Environment](https://github.com/DanielSant0s/AthenaEnv)  
Athena is an Environment to develop games and apps using JavaScript for PlayStation 2, and this is its official package manager.

This package manager search for packages in this [Official AthenaEnv Packages Repository](https://github.com/terremoth/athenaenv-pkgs)  
It will create a `athena_pkgs` directory in the current path to put the pkgs in it.

## Documentation

## Zeus Installation
- You should have [Python installed](https://www.python.org/downloads/), version at least 3.8 or higher should be fine
- `$ pip install -r requirements.txt` or `$ python -m pip install -r requirements.txt`

#### Install a package in the current dir:

```sh
$ python zeus.py -i pkg-name
```

#### Update a package in the current dir:

\- At the time, it does the same as install: get from repo and overwrite the current version

```sh
$ python zeus.py -u pkg-name
```

#### Remove a package in the current dir:

```sh
$ python zeus.py -r pkg-name
```

#### Update all installed packages in the current dir:

```sh
$ python zeus.py -a
```

#### Search for a package:

```sh
$ python zeus.py -s pkg-name (or --search pkg-name)
```

#### List all available packages to install:

```sh
$ python zeus.py -l (or --list)
```

### TO-DO
- make an executable/installable version of Zeus, using [Nuitka](https://github.com/Nuitka/Nuitka)
  - `python -m nuitka --onefile --windows-icon-from-ico=main.ico zeus.py`
  - the `--onefile` option is debatable if it is a good idea
  - we must see an icon file for the executable
  - if installable (Windows), maybe we can use iexpress.exe to create a package?
  - Define a good path to install. Maybe at %appdata% like PHP Composer and VSCode do?
  - Automatic GitHub actions to compile with Nuitka, and release a tag + release object?
- `zeus --init` or `zeus -in` command to create a lib from the current directory
- unit tests
