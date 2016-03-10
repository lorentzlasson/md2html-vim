import os
import neovim

@neovim.plugin
class Main(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.autocmd('BufEnter', pattern='*.md', eval='expand("<afile>")', sync=True)
    def on_bufenter(self, filename):
        self.htmlfile= filename.split(".")[0] + ".html"

    @neovim.autocmd('BufWritePost', pattern='*.md', eval='expand("<afile>")', sync=False)
    def on_bufwritepost(self, filename):
        os.system("md2html " + filename + " > " + self.htmlfile)
        self.nvim.out_write("genereated " + self.htmlfile+ "\n")
