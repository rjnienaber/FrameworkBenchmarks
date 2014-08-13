import helper
from helper import Command

def start(args, logfile, errfile):
  helper.set_database_host(args)
  ruby_version = helper.ruby_version(logfile)
  commands = [
    Command("rvm %s do bundle" % ruby_version, True),
    Command("rvm %s do bundle exec puma -t 8:32 -w 8 --preload -b tcp://0.0.0.0:8080 -e production" % ruby_version, False)
  ]

  return helper.run(commands, logfile, errfile)

def stop(logfile, errfile):
  return helper.stop('puma', logfile, errfile)
