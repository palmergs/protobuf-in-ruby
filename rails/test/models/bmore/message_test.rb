require 'test_helper'
require 'bmore/messages_pb'

class MessageTest < ActiveSupport::TestCase
  test 'Activity' do
    assert_not_nil Bmore::Activity.new
  end

  test 'Firewall' do
    assert_not_nil Bmore::Firewall.new
  end

  test 'Conversation' do
    assert_not_nil Bmore::Conversation.new
  end

  test 'HttpRequest' do
    assert_not_nil Bmore::HttpRequest.new
  end

  test 'KeyValue' do
    assert_not_nil Bmore::KeyValue.new
  end

  test 'Chat' do  
    assert_not_nil Bmore::Chat.new
    assert Bmore::Chat::Priority::LOW == 0
    assert Bmore::Chat::ContentType::TEXT == 0
  end
end
