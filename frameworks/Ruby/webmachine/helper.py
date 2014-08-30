import os
import subprocess
import time
import re

class CommandHelper(object):
  def __init__(self, logfile, errfile, args=None):
    self.args = args
    self.logfile = logfile
    self.errfile = errfile
    self.args = args
    if args:
      self.cwd = args.troot
    else:
      self.cwd = os.environ['TROOT']

  def jruby_run(self, command, wait_for_exit=True):
    command_with_env = "{0} rvm jruby-1.7.13 do bundle exec {1}".format(self._db_host(), command)
    return self.run(command_with_env, wait_for_exit)

  def ruby_run(self, command, wait_for_exit=True):
    command_with_env = "{0} rvm ruby-2.1.2 do bundle exec {1}".format(self._db_host(), command)
    return self.run(command_with_env, wait_for_exit)

  def rbx_run(self, command, wait_for_exit=True):
    command_with_env = "{0} rvm rbx-2.2.10 do bundle exec {1}".format(self._db_host(), command)
    return self.run(command_with_env, wait_for_exit)

  def run(self, command, wait_for_exit=True):
    self.logfile.write('Running: {0}\n'.format(command))
    try:
      if wait_for_exit:
        subprocess.check_call(command, shell=True, cwd=self.cwd, stderr=self.errfile, stdout=self.logfile)
      else:
        subprocess.Popen(command, shell=True, cwd=self.cwd, stderr=self.errfile, stdout=self.logfile)
    except subprocess.CalledProcessError:
      return 1
    return 0

  def run_with_output(self, command):
    p = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    return p.communicate()

  def _db_host(self):
    return "DB_HOST={0}".format(self.args.database_host or 'localhost')

  def stop(self, partial_command):
    output, _ = self.run_with_output('ps aux')
    for line in output.splitlines():
      if partial_command in line and 'run-tests' not in line:
        pid = int(line.split(None, 2)[1])
        os.kill(pid, 15)

    #extra check to kill by port if need be
    counter = 0
    while True:
      output, _ = self.run_with_output('lsof -i tcp:8080')
      if output == '' or counter == 60:
        #throw error?
        break
      lines = output.split(os.linesep)[1:]
      matches = [re.search('^\w+\s+(?P<pid>\d+)', line) for line in lines]
      pids = map(lambda y: int(y.groupdict()['pid']), filter(lambda x: x != None, matches))
      for pid in pids:
        os.kill(pid, 15)
      time.sleep(0.5)

    self.run('rm -rf tmp/*', True)
    return 0

def start(server, args, logfile, errfile):
  helper = CommandHelper(logfile, errfile, args)
  if server == 'jruby-puma':
    return helper.jruby_run('puma -t 8:32 -b tcp://0.0.0.0:8080 -e production', False)
  if server == 'mri-puma':
    return helper.ruby_run('puma -t 8:32 -w 8 --preload -b tcp://0.0.0.0:8080 -e production', False)
  if server == 'thin':
    return helper.ruby_run('thin start -C config/thin.yml', False)
  if server == 'torqbox':
    return helper.jruby_run('torqbox -b 0.0.0.0 -E production', False)
  if server == 'trinidad':
    return helper.jruby_run('trinidad --config config/trinidad.yml', False)
  if server == 'unicorn':
    helper.run('sudo /usr/local/nginx/sbin/nginx -c $TROOT/config/nginx.conf', True)
    return helper.ruby_run('unicorn -E production -c config/unicorn.rb', False)


def stop(server, logfile, errfile):
  helper = CommandHelper(logfile, errfile)
  if server == 'unicorn':
    helper.run('sudo /usr/local/nginx/sbin/nginx -s stop -c $TROOT/config/nginx.conf', True)
  return helper.stop(server)