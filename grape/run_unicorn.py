import helper
from helper import Command

def start(args, logfile, errfile):
  helper.set_database_host(args)
  ruby_version = helper.ruby_version(logfile)
  commands = [
    Command("rvm %s do bundle" % ruby_version, True),
    Command("rvm %s do bundle exec unicorn -E production -c config/unicorn.rb" % ruby_version, False)
  ]

  return helper.run(commands, logfile, errfile)

def stop(logfile, errfile):
  return helper.stop('unicorn', logfile, errfile)
