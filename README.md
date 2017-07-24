# Commands
* `:Codespell`

# Testing
* `sudo pip3 install pytest pytest-benchmark` (Or use `virtualenv`)
* `py.test`

# Tips
* Check if `python3` is supported in your vim build: `vim --version`, look for the string "+python3".
* Load the `*.vim` script from commandline:
 `vim -S codespell.vim`
* `:match Error /\%2l\%>1c\%<4c./`: highlight line 2 (`\%2l`) and column 2 (`\%>1c`) to column 3 (`\%<4c`), the `.` is required because the match is 0 width.

# References
* Python's `vim` interface [doc](http://vimdoc.sourceforge.net/htmldoc/if_pyth.html)
* [Learn vimscript the hard way](http://learnvimscriptthehardway.stevelosh.com)
