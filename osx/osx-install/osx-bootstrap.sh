#!/usr/bin/env bash

echo "Bootstrapping..."

# Check for Homebrew, install if we don't have it
if test ! $(which brew); then
    echo "Installing homebrew..."
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

# Update homebrew recipes
brew update

# Install GNU core utilities (those that come with OS X are outdated)
brew install coreutils
brew install gnu-sed --with-default-names
brew install gnu-tar --with-default-names
brew install gnu-indent --with-default-names
brew install gnu-which --with-default-names

# Install GNU `find`, `locate`, `updatedb`, and `xargs`, g-prefixed
brew install findutils

# Install Bash 4
brew install bash

PACKAGES=(
zsh
zsh-completions
ffmpeg
git
graphviz
imagemagick
jq
elixir
python
python3
pypy
ssh-copy-id
tree
wget
fzf
mas
bat
reattach-to-user-namespace
youtube-dl
ag
ripgrep
broot
neovim
)

echo "Installing packages..."
brew install ${PACKAGES[@]}

echo "Cleaning up..."
brew cleanup

CASKS=(
viscosity
karabiner-elements
google-chrome
chromium
firefox
visual-studio-code
spotify
docker
github
obsidian
sublime-merge
tableplus
pgadmin4
raycast
devdocs
ableton-live-suite

qlcolorcode
qlstephen
qlmarkdown
quicklook-json
qlprettypatch
quicklook-csv
webpquicklook
suspicious-package
)

echo "Installing cask apps..."
brew install ${CASKS[@]} --cask

echo "Installing AppStore apps..."

# Amphetamine
mas install 937984704

# Bitwarden
mas install 1137397744

# Flow
mas install 1423210932

# Tailscale
mas install 1470499037

# Dato
mas install 1470584107

echo "Installing fonts..."
brew tap homebrew/cask-fonts

FONTS=(
font-sourcecodepro-nerd-font
font-source-code-pro-for-powerline
font-sourcecodepro-nerd-font-mono
font-roboto
font-clear-sans
font-fira-code-nerd-font
)

brew install ${FONTS[@]} --cask

echo "Done, now open zsh and run next script."
