# python_file_server

# Serve files on a local network using Python and Jinja2.

## Jinja2 is used to create an index.html file. Python serves the index.html file. In the index.html file CSS is added to make the interface look nicer. Download files one by one or all at once with wget.

### Requirements:

* Python3
* jinja2
* pathlib

![screenshot](/screenshot.png)


Change directories into directory containing the files you wish to share. 

```
$ cd my_images/
```

Run program.

```
$ python3 /path/to/serve_files.py
```

Click on the links to download files one by one.

Download all files at once using wget.

```
$ wget -r http://<server_ip>:8000/
```
