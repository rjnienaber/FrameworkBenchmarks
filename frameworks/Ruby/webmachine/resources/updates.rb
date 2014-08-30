class Updates < JsonResource
  include MySqlHelper

  def create_response
    query_string = Rack::Utils.parse_query(request.uri.query)
    queries = query_string['queries'].to_i
    queries = 1 if queries < 1
    queries = 500 if queries > 500

    results = (1..queries).map do
      id = Random.rand(10000) + 1
      execute('SELECT * FROM World WHERE id = ?', [id]) { |r| r.fetch_hash}
    end

    #mass update
    values = results.map { |h| ['(', h['id'], ',', Random.rand(10000) + 1, ')', ','] }.flatten[0..-2].join
    sql = "INSERT INTO `World` (`id`,`randomNumber`) VALUES #{values} ON DUPLICATE KEY UPDATE `World`.`randomNumber` = VALUES(`randomNumber`)"
    execute(sql)
    
    results
  end
end