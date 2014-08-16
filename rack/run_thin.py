import helper
from helper import Command

def start(args, logfile, errfile):
  helper.set_database_host(args)
  ruby_version = helper.ruby_version(logfile)
  commands = [
    Command("rvm %s do bundle" % ruby_version, True),
    Command("rvm %s do bundle exec thin start -C config/thin.yml" % ruby_version, False)
  ]

  return helper.run(commands, logfile, errfile)

def stop(logfile, errfile):
  helper.run([Command('rm -rf tmp/*', True)], logfile, errfile)  
  return helper.stop('thin', logfile, errfile)
