Python
=====

.. _installation:

Installation
------------

To use HikerAPI, first install it using pip:

.. code-block:: console

   $ pip install hikerapi

Usage
------------

You need to pass the key to the Client and call the function you want to get the result

For example:

>>> from hikerapi import Client
>>> cl = Client(api_key="")
>>> cl.user_by_username_v1("user")

or

>>> from hikerapi import AsyncClient
>>> cl = AsyncClient(api_key="")
>>> await cl.user_by_username_v1("user")


API Reference
------------

.. autoclass:: hikerapi.Client
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: hikerapi.AsyncClient
   :members:
   :undoc-members:
   :show-inheritance:
