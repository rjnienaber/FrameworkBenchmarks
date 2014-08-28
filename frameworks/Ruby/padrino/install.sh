#!/bin/bash

fw_depends rvm nginx java

# Some gems seem to fail when installing on travis
# clearing at the cache so it always retrieves new ones
export LC_ALL=en_US.UTF-8 
export LANG=en_US.UTF-8
rvm install rbx-2.2.10
rvm rbx-2.2.10@global do gem uninstall bundler --force -x
rvm rbx-2.2.10@global do gem install bundler -v=1.6.2
rvm rbx-2.2.10 do bundle install --jobs=1 --retry=3 --gemfile=$TROOT/Gemfile

rvm install ruby-2.0.0-p0
rvm ruby-2.0.0-p0 do bundle install --gemfile=$TROOT/Gemfile

rvm install jruby-1.7.8
rvm jruby-1.7.8 do bundle install --gemfile=$TROOT/Gemfile
