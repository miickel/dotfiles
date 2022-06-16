#
# Executes commands at the start of an interactive session.
#
# Authors:
#   Sorin Ionescu <sorin.ionescu@gmail.com>
#

# Source Prezto.
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi

# Customize to your needs...
export PATH="/Users/mickel/.cargo/bin:$PATH"

# FZF - Fuzzy Finder
export FZF_DEFAULT_COMMAND="rg --files --no-ignore --hidden --follow --glob \"!.git/*\""
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh 

# FNM - Node version manager
eval "$(fnm env)"
export PATH="/usr/local/opt/ruby/bin:$PATH"

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/mickel/dev/tools/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/mickel/dev/tools/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/mickel/dev/tools/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/mickel/dev/tools/google-cloud-sdk/completion.zsh.inc'; fi
