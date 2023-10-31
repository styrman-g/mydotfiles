" MY VIMRC.
let mapleader =","
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


" cursorline.
set cursorline
" Syntax
syntax on
"My Plugins
call plug#begin()
        " Color Scheme
        Plug 'ribru17/bamboo.nvim'
        " Filemanager
        Plug 'preservim/nerdtree'
        " For reading text 
        Plug 'junegunn/goyo.vim'
        " Airline
        Plug 'vim-airline/vim-airline'
call plug#end()

" Themes.
colorscheme bamboo 

" Nerd Tree
nnoremap <leader>n :NERDTreeFocus<CR>j

" Goyo plugin makes text more readable when writing prose:
map <leader>f :Goyo<CR>



