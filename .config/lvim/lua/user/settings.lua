local options = {
  fillchars = [[vert:⠀,eob:⠀]], -- remove the blank chars end of file ~
  guifont = "SFMono:h10", -- the font used in graphical neovim applications
  titlestring = "%<%F%=%l/%L - nvim", -- what the title of the window will be set to
  relativenumber = false, -- set relative numbered lines
  tabstop = 2,
  -- foldmethod = "indent",
}
for k, v in pairs(options) do 
  vim.opt[k] = v
end
