# [html2text](http://www.aaronsw.com/2002/html2text/)

html2text is a Python script that converts a page of HTML into clean, easy-to-read plain ASCII text. Better yet, that ASCII also happens to be valid Markdown (a text-to-HTML format).

# Why does this fork exist?
 * better build process
 * (less) disgusting code
 * maintaineable

# If you use this software
Please take a moment to pay your respects to Aaron.

# Usage 

## From within Python:

```python
import html2text
print html2text.html2text("<p>Hello, world.</p>")
```

Or with some configuration options:

```python
import html2text
h = html2text.HTML2Text()
h.ignore_links = True
print h.handle("<p>Hello, <a href='http://earth.google.com/'>world</a>!")
```

_Originally written by Aaron Swartz. This code is distributed under the GPLv3._


## Getting started (developers)

This project uses the [pybuilder](https://pybuilder.github.io/).

```bash
sudo pip install pyb_init
pyb-init github mriehl : html2text
```

Further building (includes coverage, pep8 linting, building a release) can be done with

```bash
source venv/bin/activate
pyb
```
