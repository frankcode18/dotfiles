-- python
-- lvim.lang.python.formatters = {
--   {
--     exe = "black",
--   },
-- }

-- lvim.lang.python.linters = {
--   {
--     exe = "flake8",
--   },
-- }
local formatters = require "lvim.lsp.null-ls.formatters"
formatters.setup{{
  exe = "black",
  filetypes = {"python"}
  }}

local dap_install = require "dap-install"
dap_install.config("python", {})
