#!/bin/bash

: '
    This script assumes you are using localhost with PORT = 8000. 
    Otherwise, you may tweak this script and have it your own way.
    Ensure every request is verbose. Since we are using cURL for
    this example, every request should have a -v option.
'

#Create Todo App Sample Curl POST - Header MUST include 'application/json'
curl -v -XPOST -H "Content-Type: application/json" -d '{"title": "This is my task.", "note": "This is a note"}' http://localhost:8000/todo/

