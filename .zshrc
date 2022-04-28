# Aliases start
alias byedoc='docker stop $(docker ps -a -q)' # Kills all running docker containers
alias rmdoc='docker rm $(docker ps -a -q)' # Removes all docker containers
alias rmdocimg='docker image rm $(docker image ls -a -q)' # Removed all docker images
alias cleanenv='docker-compose down -v && docker volume prune -f && docker system prune -f' # Full wipe of environemtn
alias kdn='sudo killall -9 dotnet' # Kills all dotnet processes
alias ipe='curl ipinfo.io/ip && echo ""' # Get external IP
alias fk='sudo $(history -p !!)' # Executes last command with sudo
alias zshrc="${EDITOR:-vi} +120 ~/.zshrc && source ~/.zshrc && echo Zsh config edited and reloaded." # Opens .zshrc in vi, once exit it will source the new configuration
# Aliases end

# Functions start
# Creates backup of the file in the format file_name.{CURRENT DATE}.bak
bak() {
	NOW=$(date +"%d_%m_%Y_%H_%M_%S")
        cp -r $1 "$1.$NOW.bak"
}

# Creates backup of the file in the format file_name.{CURRENT DATE}.bak and opens the original file in Vi
# Vi can be changed to any editor by substituting vi in the last line of function with your app
# which can be run in/from terminal
ebak() {
	echo "Backup & edit - press enter to continue..."
	read nul
	NOW=$(date +"%d_%m_%Y_%H_%M_%S")
	cp -r $1 "$1.$NOW.bak"
	vi $1
}
# Functions end