set scrolloff=8
set number
set relativenumber

set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent

let mapleader = " "
nnoremap <leader>pv :Vex<CR>
 
call plug#begin('~/vimfiles/plugged')
 
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Emmet Zen coding
Plug 'mattn/emmet-vim'
" closetag.vim
Plug 'alvan/vim-closetag'

" Ruby/Rails
Plug 'tpope/vim-rails'
Plug 'tpope/vim-bundler'

" testing
Plug 'janko-m/vim-test'
Plug 'tpope/vim-cucumber'

" code linter
Plug 'scrooloose/syntastic'

Plug 'ayu-theme/ayu-vim'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim', { 'tag': '0.1.0' }
call plug#end()

set termguicolors     " enable true colors support
let ayucolor="light"  " for light version of theme
let ayucolor="mirage" " for mirage version of theme
