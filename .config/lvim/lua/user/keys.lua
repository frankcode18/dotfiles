-- keymappings [view all the defaults by pressing <leader>Lk]
lvim.leader = "space"

-- add your own keymapping
lvim.keys.normal_mode["<C-s>"] = ":w<cr>"
-- unmap a default keymapping
-- lvim.keys.normal_mode["<C-Up>"] = ""
-- edit a default keymapping
-- lvim.keys.normal_mode["<C-q>"] = ":q<cr>"

-- Which key
lvim.builtin.which_key.mappings["P"] = { "<cmd>Telescope projects<CR>", "Projects" }
lvim.builtin.which_key.mappings["m"] = {
  name = "Others",
  n = {":HopChar1<CR>", "1 Char"},
  m = {":HopChar2<CR>", "2 Char"},
  l = {":HopLine<CR>", "Line"},
  s = {":Bracey<CR>", "Start Server"},
  q = {":BraceyStop<CR>", "Exit Server"},
  r = {":BraceyReload<CR>", "Reload Server"},
  e = {":SymbolsOutline<CR>", "Variables Menu"},
  p = {
    name = "+Terminal",
    m = { ":TermExec cmd='flowetch' size=13 direction=horizontal<CR>", "Horizontal" },
    v = { ":ToggleTerm size=45 direction=vertical<CR>", "Vertical" },
    f = { ":ToggleTerm size=13 direction=float<CR>", "Float" },
    g = { ":ToggleTerm size=13 direction=horizontal<CR>", "Git" },
  },
}

-- Telescope
local _, actions = pcall(require, "telescope.actions")
lvim.builtin.telescope.defaults.mappings = {
  -- for input mode
  i = {
    ["<C-j>"] = actions.move_selection_next,
    ["<C-k>"] = actions.move_selection_previous,
    ["<C-n>"] = actions.cycle_history_next,
    ["<C-p>"] = actions.cycle_history_prev,
  },
  -- for normal mode
  n = {
    ["<C-j>"] = actions.move_selection_next,
    ["<C-k>"] = actions.move_selection_previous,
  },
}

