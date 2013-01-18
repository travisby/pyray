pyray
=====

Python implementation of PHP's array


I had a coworker mention that he misses PHP's arrays when he is working in python.  He wants a data structure that would take whatever he threw at it.  

For the exception of arr[] syntax (which would append), this is completely possible with dictionaries.

arr[] will not work.  Instead we emulate it through arr['']
