require 'test_helper'
require 'bmore/socket_client'

class BmoreSocketClientTest < ActiveSupport::TestCase
  test 'can be instantiated' do
    assert_not_nil Bmore::SocketClient.new
    assert Bmore::SocketClient.new.host == 'localhost'
    assert Bmore::SocketClient.new.port == 35678
  end
end
