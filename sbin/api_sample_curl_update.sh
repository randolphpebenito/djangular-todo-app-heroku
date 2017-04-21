#!/bin/bash

: '
    This script assumes you are using localhost with PORT = 8000. 
    Otherwise, you may tweak this script and have it your own way.
    Ensure every request is verbose. Since we are using cURL for
    this example, every request should have a -v option.
'

#Update Todo App Sample Curl PUT - This assumes id = 1 exists'
curl -v -XPATCH -H "Content-Type: application/json" -d '{"completed": true}' http://localhost:8000/todo/1

