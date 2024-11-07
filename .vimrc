" ____ _______   ______  __  __    _    _   _ ____  
"/ ___|_   _\ \ / /  _ \|  \/  |  / \  | \ | / ___| 
"\___ \ | |  \ V /| |_) | |\/| | / _ \ |  \| \___ \ 
" ___) || |   | | |  _ <| |  | |/ ___ \| |\  |___) |
"|____/ |_|   |_| |_| \_\_|  |_/_/   \_\_| \_|____/ 
"                                                   
"__     _____ __  __ ____   ____ 
"\ \   / /_ _|  \/  |  _ \ / ___|
" \ \ / / | || |\/| | |_) | |    
"  \ V /  | || |  | |  _ <| |___ 
"   \_/  |___|_|  |_|_| \_\\____|
"                                
" https://github.com/styrman-g
" My vim config file. Take a copy of it, if you want.
"
call plug#begin()

" List your plugins here
Plug 'jceb/vim-orgmode'
Plug 'junegunn/goyo.vim'
Plug 'mhinz/vim-startify'
Plug 'itchyny/lightline.vim'
Plug 'preservim/nerdtree'
Plug 'preservim/vim-markdown'
Plug 'ptzz/lf.vim'
Plug 'voldikss/vim-floaterm'
Plug 'lervag/vimtex'
Plug 'vimwiki/vimwiki'
Plug 'arcticicestudio/nord-vim'
Plug 'morhetz/gruvbox'

call plug#end()

let mapleader = ","
" Line number.
set number
set relativenumber

"Tabs.
set tabstop=4
set softtabstop=4
set expandtab

" Move vertically by visual line.
nnoremap j gj
nnoremap k gk

" Themes.
"let g:molokai_original = 1
"colorscheme nord
colorscheme gruvbox
set background=dark    " Setting dark mode

" Goyo Plugin for fokus writing
map <leader>g :Goyo<CR>

" Keybindings for NerdtTree
nnoremap <leader>t :NERDTreeToggle<CR>

" Keybindings for Latex
" Compiling dokument
nnoremap <leader>c :VimtexCompile<CR>

" vimwiki place for folder
let g:vimwiki_list = [{'path': '~/Dokument/vimwiki/', 'syntax': 'markdown', 'ext': '.md'}]

" cursorline.
set cursorline

" Sets
" Vimrc in folder.
set exrc

"Save in buffer.
set hidden

set noswapfile
set nobackup
set undodir=/.vim/undodir
set undofile
set incsearch
set scrolloff=8
set hlsearch
set nocompatible
filetype plugin on

syntax on

" Status bar
set laststatus=2
