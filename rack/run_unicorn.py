import helper
from helper import Command

from os.path import expanduser
home = expanduser("~")

def start(args, logfile, errfile):
  helper.set_database_host(args)
  ruby_version = helper.ruby_version(logfile)
  commands = [
    Command("rvm %s do bundle" % ruby_version, True),
    Command("sudo /usr/local/nginx/sbin/nginx -c " + home + "/FrameworkBenchmarks/rack/config/nginx.conf", True),
    Command("rvm %s do bundle exec unicorn -E production -c config/unicorn.rb" % ruby_version, False)
  ]

  return helper.run(commands, logfile, errfile)

def stop(logfile, errfile):
  helper.run([Command("sudo /usr/local/nginx/sbin/nginx -s stop", True)], logfile, errfile)
  return helper.stop('unicorn', logfile, errfile)