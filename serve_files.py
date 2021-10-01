#!/usr/bin/env python3

import http.server
import socketserver
from pathlib import Path
import jinja2
import functools

script_path = Path(__file__).parent.absolute()
template = Path(script_path / "template.jinja")
rendered_file = Path(script_path / "index.html")
directory = Path('.').cwd()

files = [file for file in directory.iterdir()]

content = {
    "title_text": "PYTHON FILE SERVER",
    "files": files
}

template_file = Path(script_path / template)
html_file = Path(script_path / rendered_file)


environment = jinja2.Environment(loader=jinja2.FileSystemLoader(script_path))
output = environment.get_template(template_file.name).render(content)

with open(html_file, 'w') as html:
    html.write(output)

handler = functools.partial(http.server.SimpleHTTPRequestHandler,
                            directory=script_path)

with socketserver.TCPServer(('127.0.0.1', 8000), handler) as httpd:
    httpd.serve_forever()
