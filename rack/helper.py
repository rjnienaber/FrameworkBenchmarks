import os
import subprocess
from collections import namedtuple

import setup_util

Command = namedtuple('Command', ['command', 'wait_for_exit'])

def set_database_host(args):
  database_host = args.database_host or 'localhost'
  database_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/database.yml')
  setup_util.replace_text(database_file, "  host:.*", "  host: " + database_host)

def jruby_version(logfile):
  return _get_ruby_version('jruby', logfile)

def ruby_version(logfile):
  return _get_ruby_version('ruby', logfile)

def run(commands, logfile, errfile):
  params = {'shell': True, 'cwd': _get_cwd(), 'stderr': errfile, 'stdout': logfile}
  try:
    for command in commands:   
      logfile.write("Running command: %s\n" % command.command)   
      if command.wait_for_exit:
        subprocess.check_call(command.command, **params)
      else:
        subprocess.Popen(command.command, **params)
  except subprocess.CalledProcessError:
    return 1
  return 0

def run_with_output(command, logfile):
  logfile.write("Running command: %s\n" % command)   
  return subprocess.check_output(command, cwd=_get_cwd(), stderr=subprocess.STDOUT, shell=True)  

def stop(partial_command, logfile, errfile):
  p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
  out, err = p.communicate()
  for line in out.splitlines():
    if partial_command in line and 'run-tests' not in line:
      pid = int(line.split(None, 2)[1])
      os.kill(pid, 15)
  return 0

def _get_ruby_version(impl, logfile):
  rvm_output = run_with_output('rvm list', logfile)
  rubies = sorted(filter(lambda x: impl in x, rvm_output.split()))
  if len(rubies) < 1:
    raise Exception('No rvm %s found' % impl)
  return rubies[-1]

def _get_cwd():
  return os.path.basename(os.path.normpath(os.path.dirname(os.path.realpath(__file__))))