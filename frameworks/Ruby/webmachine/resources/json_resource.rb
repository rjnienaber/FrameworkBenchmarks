class JsonResource < Webmachine::Resource
  def content_types_provided
    [["application/json; charset=utf-8", :to_json]]
  end

  def to_json
    create_response.to_json
  end
end