FROM ubuntu:22.04

# Install app dependencies
RUN apt-get update && apt-get install -y \
    fortune-mod \
    cowsay \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Add games to path so 'cowsay' and 'fortune' work
ENV PATH="${PATH}:/usr/games"

# Copy the script into the container
COPY wisecow.sh /usr/local/bin/wisecow.sh
RUN chmod +x /usr/local/bin/wisecow.sh

EXPOSE 4499

# Execute the script
CMD ["/usr/local/bin/wisecow.sh"]