#!/bin/sh

# Restore config.rb, Gemfile and Gemfile.lock
cp /opt/publisher/* .

# Run the site
bundle exec middleman serve