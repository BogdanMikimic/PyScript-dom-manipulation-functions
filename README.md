# PyScript functions for dom manipulation

A series of functions using pyodide translated to a more Pythonian
look.

## Using PyScript instructions
* Pyscript version: 2024.4.2 (as available on 28 Apr 2024) 
* Put in head of HTML file: &lt;link rel="stylesheet" href="https://pyscript.net/releases/2024.4.2/core.css" &gt;
* Put in head of HTML file: &lt;script type="module" src="https://pyscript.net/releases/2024.4.2/core.js" &gt; &lt;/script &gt;
* In the body tag put your script (linking to your function) &lt; script type="py" src="index_for_test" terminal &gt;&lt; /script &gt; 
The "terminal" argument is optional - it opens a little screen on your html page where you can see things that you normally see
in a terminal, such as the result of print() or tracebacks (?)
* The html files don't load PyScript directly if you simply double-click on your
html file, so you need to serve the files through a server. To run a server run the
command in the command line while in the same folder with your html file: python -m http.server 8000  


## Functions:
* 