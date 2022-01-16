-- Additional Plugins

lvim.plugins = {
  { "mfussenegger/nvim-jdtls" },
  {"folke/tokyonight.nvim"},
  {"eddyekofo94/gruvbox-flat.nvim"},
  {'google/vim-maktaba'},
  {'google/vim-codefmt'},
  {
    "folke/trouble.nvim",
    cmd = "TroubleToggle",
  },
  {
    "turbio/bracey.vim",
    cmd = {"Bracey", "BracyStop", "BraceyReload", "BraceyEval"},
    run = "npm install --prefix server",
  },
  {
    "phaazon/hop.nvim",
    event = "BufRead",
    config = function()
      require("hop").setup()
      --   vim.api.nvim_set_keymap("n", "s", ":HopChar2<cr>", { silent = true })
      --   vim.api.nvim_set_keymap("n", "S", ":HopWord<cr>", { silent = true })
    end,
  },
  {
    "norcalli/nvim-colorizer.lua",
    config = function()
      require("user.colorizer").config()
    end,
  },
  {
    "ray-x/lsp_signature.nvim",
    event = "BufRead",
    config = function()
      require ("lsp_signature").setup()
    end
  },
  {
    "simrat39/symbols-outline.nvim",
    cmd = "SymbolsOutline",
  },
  { "rcarriga/nvim-dap-ui",
    requires = "mfussenegger/nvim-dap",
    config = function()
      require("user.dapui").config()
    end
  },

  {
    'rose-pine/neovim',
    as = 'rose-pine',
    tag = 'v0.1.0', -- Optional tag release
  },
  {
    'dylanaraps/wal.vim',
  },
  {
    'srcery-colors/srcery-vim'
  },
}
-- Additional Config

-- vim.g.gruvbox_flat_style = "hard"
vim.g.rose_pine_variant='moon'
