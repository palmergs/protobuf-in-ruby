require 'bmore/messages_pb'
require 'pp'

class BmoreClient

  attr_reader :host, :port

  def initialize host: 'localhost', port: 35678
    @messages_sent = 0
    @host = host
    @port = port
  end

  def block? request
    message = build_from(request)
    response = send_message(message, Bmore::Firewall)
    response ? response.block_it : false
  end

  def say chat
    message = build_from(chat)
    send_message(message, Bmore::Conversation)
  end

  def time_ms
    (Time.now.to_f / 1000).to_i
  end

  def build_from event
    activity = Bmore::Activity.new(sent_at: time_ms, 
        message_number: (@messages_sent += 1),
        sender: 'Rails')
    
    case event
    when Bmore::HttpRequest
      activity.request = event
    when Bmore::Chat
      activity.chat = event
    else
      raise "Unexpected event"
    end

    activity
  end

  def send_message message, expected_response
    encoded = Bmore::Activity.encode(message)
    socket = TCPSocket.new(host, port)
    written = socket.write(encoded)
    socket.close_write

    response = socket.read
    decoded = expected_response.decode(response)
    decoded
  rescue => e
    pp "Unable to send message :: #{ e }"
    nil
  ensure
    socket.close if socket
  end
end
