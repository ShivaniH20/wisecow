# Use small Linux image
FROM alpine:3.18

# Install Python
RUN apk add --no-cache python3 py3-pip bash

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . /app

# Make the script executable
RUN chmod +x wisecow.sh

# Expose port
EXPOSE 8000

# Run the script
CMD ["./wisecow.sh"]
