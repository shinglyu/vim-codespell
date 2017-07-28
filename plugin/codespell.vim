if !has('python3')
  finish
endif

" s:dir will be used in python
let s:dir= fnamemodify(resolve(expand('<sfile>:p')), ':h')
let s:path = s:dir . '/codespell.py'

function! CodeSpell()
  call clearmatches()
  execute 'py3file ' . s:path
endfunction

command! Codespell call CodeSpell()
