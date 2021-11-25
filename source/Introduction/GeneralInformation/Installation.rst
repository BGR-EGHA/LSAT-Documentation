.. _install:

Installation
------------

LSAT is distributed in two ways: Installer for Windows and as source code.

Installation with the installer (Windows)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Download `the newest LSAT installer <https://github.com/BGR-EGHA/LSAT/releases>`_
#. Run the installer and follow the instructions.

Installation with source code on Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Make sure you have Python 3 installed (3.7 tested), if not you can get it from `python.org/downloads <https://www.python.org/downloads/>`_
2. Download LSAT
3. Navigate to the LSAT directory and open a PowerShell window (if you downloaded a zipped version you will need to unzip LSAT first).
4. Create a virtual environment

.. code-block:: none

    python -m venv venv

5. Activate the virtual environment (venv should appear in the command line, indicating you were successful)

.. code-block:: none

    .\venv\Scripts\activate

6. Install the required packages

.. code-block:: none

    python -m pip install -r requirements.txt

Additionally to the packages listed in the requirements.txt you will need GDAL (3.3.1 tested).
Unfortunately, GDAL can usually not simply be installed with a pip command.
You can either download a .whl file from `Christoph Gohlkes fantastic website <https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal>`_ or
build it yourself.
Installing a .whl file:

.. code-block:: none

    python -m pip install *path to .whl file*

7. Start LSAT PM

.. code-block:: none

    python startMenu_main.py

Installation with source code on Linux (Ubuntu 20.04.3 tested)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Download LSAT
2. | Navigate to the LSAT directory and open a Terminal (if you downloaded a zipped version you will
   | need to extract LSAT first).
3. Install Python packages (venv, pip, python development tools), gdal and libraries for Qt

.. code-block:: none

    sudo apt install python3-venv python3-pip gdal-bin libgdal-dev python3-dev '^libxcb.*-dev'

4. Create a virtual environment

.. code-block:: none

    python3 -m venv venv

5. | Activate the virtual environment (venv should appear in the command line, indicating you were
   | successful)

.. code-block:: none

    source venv/bin/activate

6. Install the required packages

.. code-block:: none

    python3 -m pip install -r requirements.txt

Additionally to the packages listed in the requirements.txt you will need GDAL (3.0.4 tested).
Unfortunately, GDAL can usually not simply be installed with the standard pip command.
You need to specify the version based on the gdal version installed.
To get the installed version run

.. code-block:: none

    ogrinfo --version

It will output something like: "GDAL $VERSION, released $RELEASEDATE". Now install that version

.. code-block:: none

    python3 -m pip install gdal==$VERSION

7. Start LSAT PM

.. code-block:: none

    python3 startMenu_main.py
