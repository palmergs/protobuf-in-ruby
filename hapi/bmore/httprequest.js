/**
 * @fileoverview
 * @enhanceable
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.bmore.HttpRequest');

goog.require('jspb.Message');
goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Map');
goog.require('proto.bmore.KeyValue');


/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.bmore.HttpRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.bmore.HttpRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.bmore.HttpRequest.displayName = 'proto.bmore.HttpRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.bmore.HttpRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.bmore.HttpRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.bmore.HttpRequest} msg The msg instance to transform.
 * @return {!Object}
 */
proto.bmore.HttpRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    ip: jspb.Message.getFieldWithDefault(msg, 3, ""),
    requestMethod: jspb.Message.getFieldWithDefault(msg, 4, ""),
    host: jspb.Message.getFieldWithDefault(msg, 5, ""),
    port: jspb.Message.getFieldWithDefault(msg, 6, 0),
    context: jspb.Message.getFieldWithDefault(msg, 7, ""),
    parametersMap: (f = msg.getParametersMap()) ? f.toObject(includeInstance, proto.bmore.KeyValue.toObject) : [],
    headersMap: (f = msg.getHeadersMap()) ? f.toObject(includeInstance, proto.bmore.KeyValue.toObject) : []
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.bmore.HttpRequest}
 */
proto.bmore.HttpRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.bmore.HttpRequest;
  return proto.bmore.HttpRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.bmore.HttpRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.bmore.HttpRequest}
 */
proto.bmore.HttpRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setIp(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setRequestMethod(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setHost(value);
      break;
    case 6:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setPort(value);
      break;
    case 7:
      var value = /** @type {string} */ (reader.readString());
      msg.setContext(value);
      break;
    case 8:
      var value = msg.getParametersMap();
      reader.readMessage(value, function(message, reader) {
        jspb.Map.deserializeBinary(message, reader, jspb.BinaryReader.prototype.readString, jspb.BinaryReader.prototype.readMessage, proto.bmore.KeyValue.deserializeBinaryFromReader);
         });
      break;
    case 9:
      var value = msg.getHeadersMap();
      reader.readMessage(value, function(message, reader) {
        jspb.Map.deserializeBinary(message, reader, jspb.BinaryReader.prototype.readString, jspb.BinaryReader.prototype.readMessage, proto.bmore.KeyValue.deserializeBinaryFromReader);
         });
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.bmore.HttpRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.bmore.HttpRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.bmore.HttpRequest} message
 * @param {!jspb.BinaryWriter} writer
 */
proto.bmore.HttpRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIp();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getRequestMethod();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = message.getHost();
  if (f.length > 0) {
    writer.writeString(
      5,
      f
    );
  }
  f = message.getPort();
  if (f !== 0) {
    writer.writeInt32(
      6,
      f
    );
  }
  f = message.getContext();
  if (f.length > 0) {
    writer.writeString(
      7,
      f
    );
  }
  f = message.getParametersMap(true);
  if (f && f.getLength() > 0) {
    f.serializeBinary(8, writer, jspb.BinaryWriter.prototype.writeString, jspb.BinaryWriter.prototype.writeMessage, proto.bmore.KeyValue.serializeBinaryToWriter);
  }
  f = message.getHeadersMap(true);
  if (f && f.getLength() > 0) {
    f.serializeBinary(9, writer, jspb.BinaryWriter.prototype.writeString, jspb.BinaryWriter.prototype.writeMessage, proto.bmore.KeyValue.serializeBinaryToWriter);
  }
};


/**
 * optional string ip = 3;
 * @return {string}
 */
proto.bmore.HttpRequest.prototype.getIp = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/** @param {string} value */
proto.bmore.HttpRequest.prototype.setIp = function(value) {
  jspb.Message.setField(this, 3, value);
};


/**
 * optional string request_method = 4;
 * @return {string}
 */
proto.bmore.HttpRequest.prototype.getRequestMethod = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/** @param {string} value */
proto.bmore.HttpRequest.prototype.setRequestMethod = function(value) {
  jspb.Message.setField(this, 4, value);
};


/**
 * optional string host = 5;
 * @return {string}
 */
proto.bmore.HttpRequest.prototype.getHost = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 5, ""));
};


/** @param {string} value */
proto.bmore.HttpRequest.prototype.setHost = function(value) {
  jspb.Message.setField(this, 5, value);
};


/**
 * optional int32 port = 6;
 * @return {number}
 */
proto.bmore.HttpRequest.prototype.getPort = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 6, 0));
};


/** @param {number} value */
proto.bmore.HttpRequest.prototype.setPort = function(value) {
  jspb.Message.setField(this, 6, value);
};


/**
 * optional string context = 7;
 * @return {string}
 */
proto.bmore.HttpRequest.prototype.getContext = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 7, ""));
};


/** @param {string} value */
proto.bmore.HttpRequest.prototype.setContext = function(value) {
  jspb.Message.setField(this, 7, value);
};


/**
 * map<string, KeyValue> parameters = 8;
 * @param {boolean=} opt_noLazyCreate Do not create the map if
 * empty, instead returning `undefined`
 * @return {!jspb.Map<string,!proto.bmore.KeyValue>}
 */
proto.bmore.HttpRequest.prototype.getParametersMap = function(opt_noLazyCreate) {
  return /** @type {!jspb.Map<string,!proto.bmore.KeyValue>} */ (
      jspb.Message.getMapField(this, 8, opt_noLazyCreate,
      proto.bmore.KeyValue));
};


proto.bmore.HttpRequest.prototype.clearParametersMap = function() {
  this.getParametersMap().clear();
};


/**
 * map<string, KeyValue> headers = 9;
 * @param {boolean=} opt_noLazyCreate Do not create the map if
 * empty, instead returning `undefined`
 * @return {!jspb.Map<string,!proto.bmore.KeyValue>}
 */
proto.bmore.HttpRequest.prototype.getHeadersMap = function(opt_noLazyCreate) {
  return /** @type {!jspb.Map<string,!proto.bmore.KeyValue>} */ (
      jspb.Message.getMapField(this, 9, opt_noLazyCreate,
      proto.bmore.KeyValue));
};


proto.bmore.HttpRequest.prototype.clearHeadersMap = function() {
  this.getHeadersMap().clear();
};

