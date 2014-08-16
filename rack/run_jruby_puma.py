import helper
from helper import Command

def start(args, logfile, errfile):
  helper.set_database_host(args)
  jruby_version = helper.jruby_version(logfile)
  commands = [
    Command("rvm %s do bundle" % jruby_version, True),
    Command("rvm %s do bundle exec puma -b tcp://0.0.0.0:8080 -e production" % jruby_version, False)
  ]

  return helper.run(commands, logfile, errfile)

def stop(logfile, errfile):
  return helper.stop('puma', logfile, errfile)
