local map = require("core.utils").map
local opts = { noremap = true, silent = true }

local term_opts = { silent = true }

-- Shorten function name
local keymap = vim.api.nvim_set_keymap

--Remap space as leader key
keymap("", "<Space>", "<Nop>", opts)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Deleting Files and Folders --
keymap("n", "<leader>del", ":!rm %<CR>", opts)

-- Reload Lua Keymapping [ ref - https://github.com/svermeulen/vimpeccable#runtime-reloading-of-entire-vimrc-plugin]
keymap("n", "<leader>rl", ":luafile .config/nvim/lua/custom/mappings.lua<CR>:echo' ✓  Reloaded nvim lua configs'<CR>", opts)


--Copy paste from system clipboard --
keymap("n", "<C-c>", '"+yy', opts)
keymap("v", "p", '"_dP', opts)               --paste from external clipboard in visual mode --
-- Duplicate Lines --
keymap("n", "<A-d>", ":t.<CR>", opts)

-- Find and replace --
keymap("n", "<C-h>", ':%s//', opts)

-- Visual Block / indenting mode  --
keymap("v", "<", "<gv", opts)
keymap("v", ">", ">gv", opts)

-- Move text up and down
keymap("x", "<A-j>", ":move '>+1<CR>gv-gv", opts)
keymap("x", "<A-k>", ":move '<-2<CR>gv-gv", opts)
-- keymap("x", "J", ":move '>+1<CR>gv-gv", opts)
-- keymap("x", "K", ":move '<-2<CR>gv-gv", opts)

-- Resize with arrows
keymap("n", "<C-Up>", ":resize +2<CR>", opts)
keymap("n", "<C-Down>", ":resize -2<CR>", opts)
keymap("n", "<C-Left>", ":vertical resize -2<CR>", opts)
keymap("n", "<C-Right>", ":vertical resize +2<CR>", opts)

-----------------------------------------------------------------------

-- telescope
map("n", "<leader>fp", ":Telescope media_files <CR>")
map("n", "<leader>te", ":Telescope <CR>")

--help menu
-- map("n", "<leader>ch", ":lua require('nvchad.cheatsheet').show() <CR>")

-- truezen
map("n", "<leader>ta", ":TZAtaraxis <CR>")
map("n", "<leader>tm", ":TZMinimalist <CR>")
map("n", "<leader>tf", ":TZFocus <CR>")

