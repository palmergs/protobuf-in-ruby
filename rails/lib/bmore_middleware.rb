require 'rack'
require 'bmore/messages_pb'

class BmoreMiddleware

  def initialize app
    @app = app
  end

  def call env
    request = Rack::Request.new(env)
    message = Bmore::HttpRequest.new(ip: request.ip.to_s,
        request_method: request.request_method.to_s,
        host: request.host.to_s,
        port: request.port.to_i,
        script: request.script.to_s,
        path: request.path_info.to_s)
    append_parameters(message, request)
    append_headers(message, request)

    if BmoreClient.block?(request)
      [ 403, {}, [ "BOOM!" ]]
    else
      @app.call(env)
    end
  end

  def append_headers message, request
    request.each_header do |key, value|
      kv = bmore.KeyValue(key: key.to_s)
      if value.is_a?(Enumerable)
        value.each do |v|
          kv.value << v.to_s
        end
      else
        kv.value << value.to_s
      end
      message.headers[key.to_s] = kv
    end

  end

  def append_parameters message, request
    request.params.each do |key, value|
      recurse_append_params(message, request, key, value)
    end
  end

  def recurse_append_params message, request, key, value
    if value.is_a?(Hash)
      value.each do |nested_key, nested_value|
        recurse_append_params(message, 
            request, 
            "#{ key }.#{ nested_key }",
            nested_value)
      end
    elsif value.is_a?(Enumerable)
      kv = bmore.KeyValue(key: key.to_s)
      value.each do |v|
        kv.value << v.to_s
      end
      message.parameters["#{ key }[]"] = kv
    else
      kv = bmore.KeyValue(key: key.to_s)
      kv.value << value.to_s
      message.parameters[key] = kv
    end
  end
end
