===================
Practical task # 03
===================
-------
Content
-------

- ``convertations`` package
- runner script (``convert.py``)
- ``requirements.txt``

----------------------------------------
Description of ``convertations`` package
----------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Content of package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package consists of following packages:

- convertations
- tools

~~~~~~~~~~~~~~~~~~~~~~~~
``convertations`` module
~~~~~~~~~~~~~~~~~~~~~~~~

This module is aimed for making different transformations on given data. For that purposes there is ``Transform`` class.
This class has following methods:

- ``Transform(value: int = None, message: str = None, library_type: LibraryType = LibraryType.NUM2WORDS)`` - create class' object with given value, we will work with, also you can put custom greeting message, also you can select convertation library either ``num2words`` or ``inflect``;
- ``get_number_into_words()`` - returns string with number typed in words;
- ``print_number_into_words()`` - prints string with number typed in words;
- ``read_value()`` - read value from console input with putting invitation message, we given its when created object, otherwise it uses predefined message;
- ``get_value()`` - return stored value;
- ``set_value(value: int)`` - set value;

~~~~~~~~~~~~~~~~~~~~~~~~
``tools`` module
~~~~~~~~~~~~~~~~~~~~~~~~

This module is aimed for giving different support methods for other modules. It consists of following functions:

- ``isinteger(value: any)`` - this static method checks if given ``value`` can be converted into ``int``;
- ``value_validation(value: str)`` - this static method validate whether given ``str`` value can be converted into positive ``int``. In case If it's possible it returns this ``int`` value, otherwise it returns ``None``;