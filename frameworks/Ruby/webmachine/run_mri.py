from helper import CommandHelper

def start(args, logfile, errfile):
  command = CommandHelper(logfile, errfile, args)
  return command.ruby_run("ruby webmachine.rb", False)

def stop(logfile, errfile):
  return CommandHelper(logfile, errfile).stop('webmachine')
