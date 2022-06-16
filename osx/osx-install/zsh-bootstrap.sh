#!/usr/bin/env zsh
##################################
# THIS CODE SHOULD BE RUN IN ZSH #
##################################

# Install Prezto
git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"

setopt EXTENDED_GLOB
for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N); do
  ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"
done

# Make ZSH default shell
chsh -s /bin/zsh

# Install FNM/Node.js
curl -fsSL https://fnm.vercel.app/install | bash

echo "RUN fnm install node"
