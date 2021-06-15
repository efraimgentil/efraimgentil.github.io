FROM ruby:2.4.10 
MAINTAINER marko@codeship.com

# Install apt based dependencies required to run Rails as 
# well as RubyGems. As the Ruby image itself is based on a 
# Debian image, we use apt-get to install those.
RUN apt-get update && apt-get install -y \ 
  build-essential \ 
  nodejs

# Configure the main working directory. This is the base 
# directory used in any further RUN, COPY, and ENTRYPOINT 
# commands.
RUN mkdir -p /app 
WORKDIR /app

# Copy the Gemfile as well as the Gemfile.lock and install 
# the RubyGems. This is a separate step so the dependencies 
# will be cached unless changes to one of those two files 
# are made.
COPY Gemfile ./ 
RUN gem install bundler && bundle install --jobs 20 --retry 5

# Copy the main application.
#COPY . ./
#VOLUME /../efraimgentil.github.io/:/app/

# Expose port 3000 to the Docker host, so we can access it 
# from the outside.
EXPOSE 4000


# The main command to run when the container starts. Also 
# tell the Rails dev server to bind to all interfaces by 
# default.
CMD ["jekyll" , "server"]

#BUILD AN RUN TROUGH docker run -p 4000:4000 -v /home/efra/Enviroment/Workspaces/java-pessoal/efraimgentil.github.io:/app blog
# docker run -p 4000:4000 -v C:\Users\efrai\Documents\Workspace\efraimgentil.github.io:/app blog