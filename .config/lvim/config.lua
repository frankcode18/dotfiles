  --[[
lvim is the global options object

Linters should be
filled in as strings with either
a global executable or a path to
an executable
]]
--for fish user
vim.opt.shell = "/bin/bash"

-- general
require "user.plugins"
require "user.keys"
require "user.lsp"
require "user.bufferline"

lvim.builtin.dap.active =true
lvim.log.level = "warn"
lvim.format_on_save = false
-- lvim.colorscheme = "shades_of_purple"
lvim.colorscheme = "rose-pine"

-- LSP
lvim.lsp.diagnostics.virtual_text = false

-- TODO: User Config for predefined plugins
-- After changing plugin config exit and reopen LunarVim, Run :PackerInstall :PackerCompile
lvim.builtin.dashboard.active = true
lvim.builtin.terminal.active = true
lvim.builtin.nvimtree.setup.view.side = "left"
lvim.builtin.nvimtree.show_icons.git = 0

-- if you don't want all the parsers change this to a table of the ones you want
lvim.builtin.treesitter.ensure_installed = {
  "bash",
  "c",
  "javascript",
  "json",
  "lua",
  "python",
  "typescript",
  "css",
  "rust",
  "java",
  "yaml",
}

lvim.builtin.treesitter.ignore_install = { "haskell" }
lvim.builtin.treesitter.highlight.enabled = true

-- Autocommands (https://neovim.io/doc/user/autocmd.html)
-- lvim.autocommands.custom_groups = {
--   { "BufWinEnter", "*.lua", "setlocal ts=8 sw=8" },
-- }
