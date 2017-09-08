require 'test_helper'
require 'bmore_middleware'

class BmoreMiddlewareTest < ActiveSupport::TestCase
  test 'can be instantiated' do
    assert_not_nil BmoreMiddleware.new(nil)
  end
end

