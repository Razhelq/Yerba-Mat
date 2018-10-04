# Yerba-Mat

The concept of a Yerba Mate Store.

This project contains 2 applications. The website with Online shop and REST API which allows to send and modify Products data in the database.

The shop contains:
- a view of all products
- a view with product details
- multiple views to manage order process
- user and basket views to manage account and a content of basket
- admin models to manage data from the admin level
- views to manage store content from the website level - allowed only for users with required permissions


To do:
- leaving and displaying reviews possibility
- django-getpaid Przelewy24 implementation

---

REST API contains:
- methods to handle HTTP requests to get products details or manage products content from database.
- methods created to manage requests send to wrong endpoints
- every request and response saves in the logs.


As a front-end side I chose bootstrap 4 with my modifications.
