vim-codespell
---------------------
A vim plugin for checking the spelling for source code. The main difference from the built-in spell checker is that it handles CamelCase, snake_case better, and you can add custom words to it.

# Installation
* Enable vim python3 support
* Install [aspell][http://aspell.net/]
  * Mac: `brew install aspell`
  * Ubuntu: `sudo apt-get install aspell`
* Add it to vim with the vim plugin manager of your choice.
  * Vundle: Add `Plugin 'shinglyu/vim-codespell'` to your `~/.vimrc` and run `:PluginInstall`
* To use the custom dictionary, you need to build it.
  * Go to the installed location of the plugin. (For Vundle on Mac it's `cd ~/.vim/bundle/vim-codespell`)
  * `cd dict`
  * `./build.sh`

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
You can add custom words to the dictionary.

* Create a text file in `dict/` (e.g. `dict/cs.list`) of words, one word per line
* Generate the dictionary
```
aspell --lang=en create master ./cs.dict < cs.list
```

A dictionary file `cs.dict` will be generated in the current dir. The plugin will pick it up using the default filename.

* Test the dictionary locally:
```
cat file_to_be_checked.txt | aspell -l en -d cs.dict --dict-dir=./ --list
```

The `--dict-dir` must be specified otherwise `aspell` will check the default location.

# Tips
* Check if `python3` is supported in your vim build: `vim --version`, look for the string "+python3".
* To load it temporarily for test, `cd` to `plugin/`, run `vim -S codespell.vim`.
* `:match Error /\%2l\%>1c\%<4c./`: highlight line 2 (`\%2l`) and column 2 (`\%>1c`) to column 3 (`\%<4c`), the `.` is required because the match is 0 width.

# References
* Python's `vim` interface [doc](http://vimdoc.sourceforge.net/htmldoc/if_pyth.html)
* [Learn vimscript the hard way](http://learnvimscriptthehardway.stevelosh.com)
