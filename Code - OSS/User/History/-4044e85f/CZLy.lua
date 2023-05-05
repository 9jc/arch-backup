-- IMPORTANT NOTE : This is default config, so dont change anything here.
-- chadrc overrides this file

local M = {}

M.options = {

   -- load your options here or load module with options1
   user = function() end,

   nvChad = {
      -- updater
      update_url = "https://github.com/NvChad/NvChad",
      update_branch = "main",
   },
   terminal = {
      behavior = {
         close_on_exit = true,
      },
      window = {
         vsplit_ratio = 0.5,
         split_ratio = 0.4,
      },
      location = {
         horizontal = "rightbelow",
         vertical = "rightbelow",
         float = {
           relative = 'editor',
           row = 0.3,
           col = 0.25,
           width = 0.5,
           height = 0.4,
           border = "single",
         }
      },
   },
}

---- UI -----

M.ui = {
   hl_override = "",
   colors = "", -- path of your file that contains colors
   theme = "onedark", -- default theme
   transparency = false,
}

M.plugins = {
   override = {},

   options = {
      packer = {
         init_file = "plugins.packerInit",
      },
      lspconfig = {
         setup_lspconf = "", -- path of lspconfig file
      },
      statusline = {
         style = "default", -- default/round/slant/block/arrow
      },
   },

   -- add, modify, remove plugins
   user = {},
}

-- non plugin only
M.mappings = {
   misc = function() end,
}

return M
