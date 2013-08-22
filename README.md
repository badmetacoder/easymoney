easymoney
=========

A financial math library in the cloud

Design
------

Each cell is a JSON object with two **required** elements:

 * value -- could be a string, a number, or a formula. Expect this to change as I work on the code.
 * type -- a string.

Additionally, cell objects may contain the following optional elements:

 * label -- a string.
 * TBD -- I'd rather not create too many extra bits and pieces, but things like create/modify/access timestamps, or even change logs might be of some use to someone.  But in such cases, leveraging fetures of databases like CouchDB may be a better idea.

Cloud
-----

Easymoney comes with a RESTful API, hence the cloud connection.  But you can
use it as any other Python module.

Requirements
------------

Python 2.7.2

