Slim::Engine.set_default_options format: :html5, sort_attrs: false

content = File.read(File.dirname(__FILE__) + '/../views/fortunes.slim')
layout = File.read(File.dirname(__FILE__) + '/../views/layout.slim')

FORTUNE_TEMPLATE = Slim::Template.new { content }
LAYOUT_TEMPLATE = Slim::Template.new { layout }

class Fortunes < Webmachine::Resource
  include MySqlHelper

  def to_html
    results = []

    execute('SELECT * FROM Fortune', []) do |r| 
      r.each { |h| results << h }
    end

    results << [0, "Additional fortune added at request time."]
    content = FORTUNE_TEMPLATE.render(results.sort_by { |x| x[1]})
    LAYOUT_TEMPLATE.render { content }
  end
end