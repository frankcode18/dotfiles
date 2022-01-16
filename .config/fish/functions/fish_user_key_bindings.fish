function fish_user_key_bindings
  # vim-like
  bind \ck fish_vi_key_bindings
  bind \cq fish_default_key_bindings

  # prevent iterm2 from closing when typing Ctrl-D (EOF)
  bind \cd delete-char
end
