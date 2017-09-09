require 'test_helper'
require 'bmore/middleware'

class BmoreMiddlewareTest < ActiveSupport::TestCase
  test 'can be instantiated' do
    assert_not_nil Bmore::Middleware.new(nil)
  end
end

