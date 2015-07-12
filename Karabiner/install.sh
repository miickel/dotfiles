#! /bin/sh

echo "Installing Karabiner configuration"

dir=`dirname $0`

# Add symlinks
ln -s -f ~/dev/tools/dotfiles/Karabiner/private.xml ~/Library/Application\ Support/Karabiner/private.xml

# Configure Karbiner using the Karbiner CLI
$dir/Karabiner-default.sh

echo "Karabiner configuration installed"
echo "Create a new profile for external and run Karabiner-external.sh"
