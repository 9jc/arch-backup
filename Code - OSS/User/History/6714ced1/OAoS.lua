local present, ts_config = pcall(require, "nvim-treesitter.configs")

if not present then
   return
end

local default = {
   ensure_installed = {
      "lua",
      "python",
      "json",
      "vim",
   },
   highlight = {
      enable = true,
      use_languagetree = true,
   },
   disable = { "c", "java", "css", "html" },

}

require'nvim-treesitter.configs'.setup {
   incremental_selection = {
     enable = true,
     keymaps = {
       init_selection = "gnn",
       node_incremental = "grn",
       scope_incremental = "grc",
       node_decremental = "grm",
     },
   },
 }

 require'nvim-treesitter.configs'.setup {
   indent = {
     enable = true
   }
 }

 
local M = {}
M.setup = function(override_flag)
   if override_flag then
      default = require("core.utils").tbl_override_req("nvim_treesitter", default)
   end
   ts_config.setup(default)
end

return M
