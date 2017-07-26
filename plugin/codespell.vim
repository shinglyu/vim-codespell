if !has('python3')
  finish
endif

let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h') . '/codespell.py'

function! CodeSpell()
  call clearmatches()
  execute 'py3file ' . s:path
endfunction

command! Codespell call CodeSpell()
