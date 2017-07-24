if !has('python3')
  finish
endif

function! CodeSpell()
  call clearmatches()
  py3file codespell.py
endfunction

command! Codespell call CodeSpell()
