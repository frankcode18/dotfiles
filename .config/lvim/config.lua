-- general
require "user.plugins"
require "user.keys"
require "user.lsp"
require "user.bufferline"
require "user.settings"

lvim.log.level = "warn"
lvim.format_on_save = false
lvim.colorscheme = "rose-pine"

-- LSP
lvim.lsp.diagnostics.virtual_text = false
-- vim.g.nvim_tree_indent_markers = 1 --"0 by default, this option shows indent markers when folders are open
vim.list_extend(lvim.lsp.override, { "java", "jdtls" })

-- vim.cmd [[autocmd CursorHoldI * silent! lua vim.lsp.buf.signature_help()]]
-- Builtins
lvim.builtin.dashboard.active = true
lvim.builtin.terminal.active = true
lvim.builtin.dap.active =true
lvim.builtin.bufferline.active = true
lvim.builtin.cmp.experimental.ghost_text = false
lvim.builtin.telescope.defaults.path_display = { "smart" }
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

--for fish user
vim.opt.shell = "/bin/bash"

