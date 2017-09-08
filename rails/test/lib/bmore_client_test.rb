require 'test_helper'
require 'bmore_client'

class BmoreClientTest < ActiveSupport::TestCase
  test 'can be instantiated' do
    assert_not_nil BmoreClient.new
    assert BmoreClient.new.host == 'localhost'
    assert BmoreClient.new.port == 35678
  end
end
