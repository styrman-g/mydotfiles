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
let g:molokai_original = 1


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

syntax on

" Status bar
set laststatus=2
