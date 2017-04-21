#!/bin/bash

: '
    This script assumes you are using localhost with PORT = 8000. 
    Otherwise, you may tweak this script and have it your own way.
    Ensure every request is verbose. Since we are using cURL for
    this example, every request should have a -v option.
'

#List Todo App Sample Curl GET - returns JSON Array
curl -v -XGET  http://localhost:8000/todo/

