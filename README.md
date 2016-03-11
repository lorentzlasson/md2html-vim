# md2html-vim

[Remote plugin](https://neovim.io/doc/user/remote_plugin.html) for [neovim](https://github.com/neovim/neovim) that generates .html from .md file on save in same directory.

## Dependencies
* node.js
* [evilstreak/markdown-js](https://github.com/evilstreak/markdown-js/blob/master/README.md) (global installation)

## Installation
Follow instructions plugin manager of your choice and then type `:UpdateRemotePlugins`

### vim-plug
Plug 'lorentzlasson/md2html-vim'

## Todo
* Handle life cycle of .html file
* Allow toggling of .html generation
* Support more markdown file endings
