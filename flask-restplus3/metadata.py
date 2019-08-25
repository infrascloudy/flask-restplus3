# -*- coding: utf-8 -*-
"""Project metadata

Information describing the project.
"""

# The package name, which is also the "UNIX name" for the project.
package = "flask-restplus3"
project = (
    "Fully featured framework for fast, easy and documented API development with Flask"
)
project_no_spaces = project.replace(" ", "")
version = "0.1"
description = """Flask-RESTPlus is an extension for Flask that adds support for quickly building REST APIs. 
Flask-RESTPlus encourages best practices with minimal setup. 
If you are familiar with Flask, Flask-RESTPlus should be easy to pick up. 
It provides a coherent collection of decorators and tools to describe your API and expose its documentation properly using Swagger3."
"""
authors = ["Foo Bar", "John Doe"]
authors_string = ", ".join(authors)
emails = ["foobar@example.com", "johndoe@thisisfake.org"]
license = "MIT"
copyright = "2019 " + authors_string
url = "http://example.com/"
