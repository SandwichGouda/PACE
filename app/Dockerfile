# Use the official Node.js image as the base image
FROM node:latest

# Set the working directory
ADD . /home/pace_dev/app
WORKDIR /home/pace_dev/app

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

CMD ["npm","run","dev"]