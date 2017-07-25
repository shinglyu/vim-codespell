# Loading
* To load it temporarily for test, `cd` to `plugin/`, run `vim -S codespell.vim`.

# Commands
* `:Codespell`: Run the spell checker once

* To run it everytime you save a `*.py` file, add the following to your vimrc:
```
:autocmd BufWritePre *.py :Codespell
```

# Testing
* `sudo pip3 install pytest pytest-benchmark` (Or use `virtualenv`)
* `py.test`

# Generating Dictionaries
* Create a text file (`cs.list`) of words, one word per line

* Generate the dictionary
```
aspell --lang=en create master ./cs.dict < cs.list
```

A dictionary file `cs.dict` will be generated in the current dir.

* Use the dictionary:
```
cat file_to_be_checked.txt | aspell -l en -d cs.dict --dict-dir=./ --list
```

The `--dict-dir` must be specified otherwise `aspell` will check the default location.

# Tips
* Check if `python3` is supported in your vim build: `vim --version`, look for the string "+python3".
* Load the `*.vim` script from commandline:
 `vim -S codespell.vim`
* `:match Error /\%2l\%>1c\%<4c./`: highlight line 2 (`\%2l`) and column 2 (`\%>1c`) to column 3 (`\%<4c`), the `.` is required because the match is 0 width.

# References
* Python's `vim` interface [doc](http://vimdoc.sourceforge.net/htmldoc/if_pyth.html)
* [Learn vimscript the hard way](http://learnvimscriptthehardway.stevelosh.com)
