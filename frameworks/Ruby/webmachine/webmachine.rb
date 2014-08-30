require 'bundler'
Bundler.require :default

require_relative 'resources/json_resource.rb'
require_relative 'resources/mysql_helper.rb'
Dir['resources/*.rb'].each { |r| require_relative r}

MyApp = Webmachine::Application.new do |app|
  app.routes do
    add ['plaintext'], PlainText
    add ['json'], Json
    add ['db'], SingleQuery
    add ['queries'], MultiQuery
    add ['fortunes'], Fortunes
    add ['updates'], Updates
  end

  app.configure do |config|
    config.ip      = '0.0.0.0'
    config.port    = 8080
    config.adapter = :Reel
  end
end

puts "Reel/WebMachine started on 8080..."
MyApp.run
