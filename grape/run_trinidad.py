import helper
from helper import Command

def start(args, logfile, errfile):
  helper.set_database_host(args)
  jruby_version = helper.jruby_version(logfile)
  commands = [
    Command("rvm %s do bundle" % jruby_version, True),
    Command("rvm %s do bundle exec trinidad --config config/trinidad.yml" % jruby_version, False)
  ]

  return helper.run(commands, logfile, errfile)

def stop(logfile, errfile):
  return helper.stop('trinidad', logfile, errfile)
