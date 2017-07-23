if !has('python3')
  finish
endif

function! CodeSpell()
  py3file codespell.py
endfunction

command! Codespell call CodeSpell()
