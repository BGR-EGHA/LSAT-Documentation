.. _install:

Installation
------------

LSAT is distributed in two ways: Installer for Windows and as source code.

Installation with the installer (Windows)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Download `the newest LSAT installer <https://github.com/BGR-EGHA/LSAT/releases>`_
#. Run the installer and follow the instructions.

Installation with source code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Download and Install `Python 3.7 <https://www.python.org/downloads/>`_
#. Download the `LSAT source code <https://github.com/BGR-EGHA/LSAT>`_
#. Open a command-line interface (Windows: Powershell) in the LSAT folder
#. Create a `virtual environment <https://docs.python.org/3.7/tutorial/venv.html>`_

    .. code-block:: none
    
        py -m venv venv

#. | Activate the virtual envirnment (venv should appear in the command line, indicating you were 
   | successfull)

    .. code-block:: none
    
        .\venv\Scripts\activate
    
#. Install the required packages

    .. code-block:: none
    
        py -m pip install -r requirements.txt
    
    Additionally to the packages listed in the requirements.txt you will need GDAL (3.3.0 tested).
    Unfortunately, GDAL can usually not simply be installed with pip. You can either downloada .whl
    file from Christoph Gohlkes fantastic `website <https://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
    or build it yourself.
    To install the downloaded .whl:

    .. code-block:: none
    
        py -m pip install *path to .whl file*

For Linux users, the installation process follows the same steps. Only the sources for external 
software and the syntax on the command line are different.