#!/bin/bash

fw_depends rvm nginx java

rvm install rbx-2.2.10
# Some gems seem to fail when installing on travis
# clearing at the cache so it always retrieves new ones
export LC_ALL=en_US.UTF-8 
export LANG=en_US.UTF-8
rvm rbx-2.2.10 do rvm --force gemset empty
rvm rbx-2.2.10@global do rvm --force gemset empty
rvm rbx-2.2.10@global do gem install bundler -v=1.6.2
rvm rbx-2.2.10 do bundle install --jobs=1 --retry=3 --gemfile=$TROOT/Gemfile

rvm install 2.1.2
rvm 2.1.2 do bundle install --gemfile=$TROOT/Gemfile

rvm install jruby-1.7.13
rvm jruby-1.7.13 do bundle install --gemfile=$TROOT/Gemfile
