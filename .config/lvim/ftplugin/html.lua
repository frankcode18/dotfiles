local formatters = require "lvim.lsp.null-ls.formatters"
formatters.setup {
  {
    exe = "prettier",
    filetypes = { "html" },
    args = { "--bracket-same-line","--no-semi", "--single-quote", "--parser <html>" },
  },
}
