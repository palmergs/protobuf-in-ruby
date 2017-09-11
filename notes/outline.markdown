Google Protobuf in Ruby

* Protobuf
  * Google's Data Interchange Format
  * "language-neutral" and "platform-neutral"
  * For "serialization of structured data"

* Pros
  * Use models across languages
  * Efficient size

* Cons
  * Loss of some ruby idioms
  * Adds a binary dependency (google-protobuf)
  * Adds a build dependency (protoc)

* Why I started looking at it?
  * Initial architecture
    * Rack Middleware
    * Ruby Service
    * Communication between Middleware and Service 
      * Marshaled Ruby Objects
      * Middleware is a dependency of service so models are shared
  * New architecture: Support Django/WSGI 
    * WSGI (similar to Rack)
    * Ruby Service
    * Communicatio between Middleware and Service
      * Replace marshaled objects with JSON
      * Python code maintains it's own models in parallet to Ruby
  * Instead: investigate Protobuf

* MammalWare
	* Social media and enterprise web application monitoring
  * Looking for investors!
  * Minimum Viable Product: Fowards HTTP requests to TheLair™ for security analysis

* Message Definitions
  * proto v1 internal to Google and never pubished
  * proto v2: C++, Java, Python, Go
  * proto v3: C++, Java, C#, Python, Go, Ruby, JavaScript

* Proto v3
  * Structure
    * `syntax="proto3";`
    * CamelCase for Messages
    * underscore_case for fields
    * Converted to appropriate style for generated language

    ```protobuf
		syntax = "proto3";
		
		package bmore;
		
		message Activity {
			int64 sent_at = 1;
			int32 message_number = 2;
			string sender = 3;
			oneof event {
				bmore.HttpRequest request = 4;
				bmore.Chat chat = 5;
			}
		}
    ```

  * Numbered Tags
    * Identify the field
    * Should not be changed; use 'reserved' to identify a deprecated field
    * Can be added
    * Whole numbers only
    * 19000 - 19999 reserved; max 2^29-1
  * Scalar fields
    * There is no nil or empty value
      * All fields have default values
      * Attempting to set a scalar field to nil is a TypeError

      ```ruby
      r = Bmore::HttpRequest.new
      r.ip = nil # => TypeError: Invalid argument for string field
      ```

    * String
      * string
      * String encoded as UTF-8
      * Default to empty string
    * Bytes
      * bytes
      * String encoded as ASCII-8bit
      * Default to empty string
    * Decimal
      * Signed:
        * int32, int64, sint32, sint64, fixed32, fixed64, sfixed32, sfixed64

        ```ruby
        chat = Bmore::Chat.new
        chat.count = 2**32+1 # => RangeError: integer 4294967297 too big to convert to `unsigned int'
        ```

      * Unsigned:
        * uint32, uint64
        * Type is the same but enforced at runtime

        ```ruby
        chat = Bmore::Chat.new
        chat.count = -1 # => Range Error: Assigning negative value to unsigned integer field.
        ```

      * Bignum or Fixnum
      * Default to 0
    * Float
      * double, float
      * Float
      * Default to 0.0
    * Boolean
      * bool
      * TrueClass, FalseClass
      * Default to false
  * Enums
    * Share the namespace of the enclosing object
      * Can't repeat names within the same scope
    * Ruby allows for access through intermediate module
      * MyMessage::EnumName::ENUM_VALUE
      * Can be set using the enum value or a symbol
    * Beware of equality checks
      * "Recognized" enums are converted to symbols

      ```ruby
      Bmore::Chat::Priority::MEDIUM # => 1
      chat = Bmore::Chat.new
      chat.priority = Bmore::Chat::Priority::MEDIUM
      chat.priority == Bmore::Chat::Priority::MEDIUM # => false!
      chat.priority # => :MEDIUM
      ```

    * The generated Class has methods for converting enum fields values to symbols

      ```ruby
      MyMessage::MyEnum.resolve(:VALUE) # => 1
      MyMessage::MuEnum.lookup(1) # => :VALUE
      ```

  * Sub-message Fields
    * Unlike scalar fields can be set to nil

    ```ruby
    chat = Bmore::Chat.new
    chat.emoticon # => nil
    chat.emoticon = Bmore::Emoticon.new(name: "smiley face")
    ```

  * Lists
    * "repeated" keyword
    * Default to an empty "array-like" structure
    * Items can be added individually
    * Scalar items can be added using `+=` 
    * Sub-message arrays must be added individually (bug?)

    ```ruby
    chat = Bmore::Chat.new
    chat.tags << "wombat" # => ok
    chat.tags += [ "weasel", "marmot", "groundhog" ] # => ok
    chat.tags = [ "marmoset", "tamarin" ] # => TypeError: Expected repeated field array

    convo = Bmore::Conversation.new
    convo.chats += [ chat ] # => TypeError: Repeated field array has wrong message/enum class
    convo.chats << chat # => ok
    ```
  
  * Oneof
    * Allows one sub-message to be set in a field
    * The specific field name is used
    * Setting a value removes any value previously set

    ```ruby
    a = Bmore::Activity.new # => <Bmore::Activity: ... request: nil, chat: nil>
    a.chat = Bmore::Chat.new # => <Bmore::Activity: ... request: nil, chat: <Bmore::Chat: >
    a.request = Bmore::HttpRequest.new # => <Bmore::Activity: ... request: <Bmore::HttpRequest: >, chat: nil >
    ```

    * There is no magic for setting the "oneof" field directly

    ```ruby
    a = Bmore::Activity.new
    a.event # => nil
    a.chat = Bmore::Chat.new
    a.event # => :chat
    a.request = Bmore::HttpRequest.new
    a.event # => :request
    a.event = Bmore::Chat.new # => RuntimeError: Oneof accessors are read-only.
    ```

  * Maps and Sets
    * Keys must be strings or integral types
    * Values may be any scalar or message type
    * Use delete to delete key

    ```ruby
    hr = Bmore::HttpRequest.new
    hr.parameters['test'] = Bmore::KeyValue.new
    hr.parameters['test'] = nil # => <Bmore::HttpRequest: parameters: {"test"=>nil}
    hr.parameters.delete('test') # => <Bmore::HttpRequest: parameters: {} 
    ```

    * Sets (not native)
      * Implement a map< type >bool for strings or integral types
      * Sets of messages or floats will need a unique key
    * Map missing some common ruby methods (e.g. empty?)
  * Initialization
    * Keyword fields in initializer allowed
    * Hash with symbols allowed ... to one level
    * Not a lot of ruby syntactic niceties:
      * no `?` form for boolean fields

* Message Compilation
  * protoc command line tool 
    * https://github.com/google/protobuf/releases
    * brew install protobuf => 3.4
  * Multiple languages can be specified in one call
  * `protoc` takes directory into account when generating code
    * can be overriden with --proto_path

    ```bash
    protoc --ruby_out=rails/lib/bmore --python_out=django/chat/bmore --js_out=hapi/bmore --proto_path=protobuf protobuf/messages.proto
    ```

  * Go
		* Requires a special package
    * Can not be generated on the same call as other languages

    ```bash
    PATH=~/go/bin:$PATH
    protoc --go_out=go/src/bmore --proto_path=protobuf protobuf/messages.proto
    ```
* Using Protobuf classes
  * gem "google-protobuf", "~> 3.4.0.2"
  * Pure ruby implementation available 
    * https://github.com/ruby-protobuf/protobuf
		* "version 2.5.0 currently supported"
