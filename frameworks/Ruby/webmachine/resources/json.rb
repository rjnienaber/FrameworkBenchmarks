class Json < JsonResource
  def create_response
    {message: 'Hello, World!'}
  end
end
