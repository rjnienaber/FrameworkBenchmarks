class SingleQuery < JsonResource
  include MySqlHelper

  def create_response
    id = Random.rand(10000) + 1
    execute('SELECT * FROM World WHERE id = ?', [id]) { |r| r.fetch_hash }
  end
end
