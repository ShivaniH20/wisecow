# Use a small Linux image
FROM alpine:3.18

# Set the working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Make the script executable
RUN chmod +x wisecow.sh

# Expose the port that the script serves on (default 8000)
EXPOSE 8000

# Run the script when the container starts
CMD ["./wisecow.sh"]
