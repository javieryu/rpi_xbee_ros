FROM ros:foxy

# install some utilities
RUN apt-get update && apt-get install -y \
      neovim \
      python3-pip && \
    rm -rf /var/lib/apt/lists/*

# install pylint for vscode development
RUN pip3 install pylint --upgrade

# install the xbee python library
RUN pip3 install digi-xbee