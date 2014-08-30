#general setup
host = ENV['DB_HOST'] || '127.0.0.1'
DB_CONFIG = [host, 'benchmarkdbuser', 'benchmarkdbpass', 'hello_world']
Mysql.tcpsocket_class = Celluloid::IO::TCPSocket

module MySqlHelper
  def execute(sql, args=[], &block)
    mysql = Mysql.connect(*DB_CONFIG)
    mysql.charset = 'utf8'
    begin
      statement = mysql.prepare(sql)
      result = statement.execute(*args)
      block.call(result) if block
    ensure
      mysql.close
    end
  end
end