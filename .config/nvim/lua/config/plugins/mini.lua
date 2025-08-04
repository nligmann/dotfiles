return {
  { 
    'echasnovski/mini.nvim', 
    version = '*',
    config = function()
	    local statusline = require "mini.statusline"
	    local icons = require "mini.icons"
	    icons.setup()
	    statusline.setup {use_icons = true}
    end
    },

}
