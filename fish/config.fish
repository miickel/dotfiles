set -g -x PATH /usr/local/bin $PATH

set fish_greeting ""

set -gx RBENV_ROOT /usr/local/var/rbenv
. (rbenv init -|psub)

alias l "gls -BFhovX --color=auto --group-directories-first --time-style=long-iso"
alias ll "gls -ABFhovX --color=auto --group-directories-first --time-style=long-iso"

# Get OS X Software Updates, and update installed Ruby gems, Homebrew, npm, and their installed packages
alias update='sudo softwareupdate -i -a; brew update; brew upgrade; brew cleanup; npm update npm -g; npm update -g; sudo gem update --system; sudo gem update'

# IP addresses
alias ip="dig +short myip.opendns.com @resolver1.opendns.com"
alias localip="ipconfig getifaddr en0"
alias ips="ifconfig -a | grep -o 'inet6\? \(addr:\)\?\s\?\(\(\([0-9]\+\.\)\{3\}[0-9]\+\)\|[a-fA-F0-9:]\+\)' | awk '{ sub(/inet6? (addr:)? ?/, \"\"); print }'"

# Recursively delete `.DS_Store` files
alias cleanup="find . -type f -name '*.DS_Store' -ls -delete"

# Show/hide hidden files in Finder
alias show="defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder"
alias hide="defaults write com.apple.finder AppleShowAllFiles -bool false && killall Finder"

# Enhanced WHOIS lookups
alias whois="whois -h whois-servers.net"

function gs -d "Git Status"
  git status
end

function gg -d "Commit all"
  git commit -v -a -m "$argv"
end
