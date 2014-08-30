class PlainText < Webmachine::Resource
  def content_types_provided
    [["text/plain; charset=utf-8", :to_text]]
  end

  def to_text
    "Hello, World!"
  end
end