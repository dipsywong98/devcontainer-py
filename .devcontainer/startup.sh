poetry install
poetry run pre-commit install

git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
sed -i -e 's/ZSH_THEME="devcontainers"/ZSH_THEME="powerlevel10k\/powerlevel10k"/g' ~/.zshrc
cp .devcontainer/.p10k.zsh ~/.p10k.zsh
echo '[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> ~/.zshrc
