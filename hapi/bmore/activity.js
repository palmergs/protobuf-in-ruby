/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.bmore.Activity');

goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Message');
goog.require('proto.bmore.Chat');
goog.require('proto.bmore.HttpRequest');


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
proto.bmore.Activity = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, proto.bmore.Activity.oneofGroups_);
};
goog.inherits(proto.bmore.Activity, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.bmore.Activity.displayName = 'proto.bmore.Activity';
}
/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.bmore.Activity.oneofGroups_ = [[4,5]];

/**
 * @enum {number}
 */
proto.bmore.Activity.EventCase = {
  EVENT_NOT_SET: 0,
  REQUEST: 4,
  CHAT: 5
};

/**
 * @return {proto.bmore.Activity.EventCase}
 */
proto.bmore.Activity.prototype.getEventCase = function() {
  return /** @type {proto.bmore.Activity.EventCase} */(jspb.Message.computeOneofCase(this, proto.bmore.Activity.oneofGroups_[0]));
};



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
proto.bmore.Activity.prototype.toObject = function(opt_includeInstance) {
  return proto.bmore.Activity.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.bmore.Activity} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.bmore.Activity.toObject = function(includeInstance, msg) {
  var f, obj = {
    sentAt: jspb.Message.getFieldWithDefault(msg, 1, 0),
    messageNumber: jspb.Message.getFieldWithDefault(msg, 2, 0),
    sender: jspb.Message.getFieldWithDefault(msg, 3, ""),
    request: (f = msg.getRequest()) && proto.bmore.HttpRequest.toObject(includeInstance, f),
    chat: (f = msg.getChat()) && proto.bmore.Chat.toObject(includeInstance, f)
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
 * @return {!proto.bmore.Activity}
 */
proto.bmore.Activity.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.bmore.Activity;
  return proto.bmore.Activity.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.bmore.Activity} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.bmore.Activity}
 */
proto.bmore.Activity.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setSentAt(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setMessageNumber(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setSender(value);
      break;
    case 4:
      var value = new proto.bmore.HttpRequest;
      reader.readMessage(value,proto.bmore.HttpRequest.deserializeBinaryFromReader);
      msg.setRequest(value);
      break;
    case 5:
      var value = new proto.bmore.Chat;
      reader.readMessage(value,proto.bmore.Chat.deserializeBinaryFromReader);
      msg.setChat(value);
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
proto.bmore.Activity.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.bmore.Activity.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.bmore.Activity} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.bmore.Activity.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getSentAt();
  if (f !== 0) {
    writer.writeInt64(
      1,
      f
    );
  }
  f = message.getMessageNumber();
  if (f !== 0) {
    writer.writeInt32(
      2,
      f
    );
  }
  f = message.getSender();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getRequest();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      proto.bmore.HttpRequest.serializeBinaryToWriter
    );
  }
  f = message.getChat();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      proto.bmore.Chat.serializeBinaryToWriter
    );
  }
};


/**
 * optional int64 sent_at = 1;
 * @return {number}
 */
proto.bmore.Activity.prototype.getSentAt = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.bmore.Activity.prototype.setSentAt = function(value) {
  jspb.Message.setField(this, 1, value);
};


/**
 * optional int32 message_number = 2;
 * @return {number}
 */
proto.bmore.Activity.prototype.getMessageNumber = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/** @param {number} value */
proto.bmore.Activity.prototype.setMessageNumber = function(value) {
  jspb.Message.setField(this, 2, value);
};


/**
 * optional string sender = 3;
 * @return {string}
 */
proto.bmore.Activity.prototype.getSender = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/** @param {string} value */
proto.bmore.Activity.prototype.setSender = function(value) {
  jspb.Message.setField(this, 3, value);
};


/**
 * optional HttpRequest request = 4;
 * @return {?proto.bmore.HttpRequest}
 */
proto.bmore.Activity.prototype.getRequest = function() {
  return /** @type{?proto.bmore.HttpRequest} */ (
    jspb.Message.getWrapperField(this, proto.bmore.HttpRequest, 4));
};


/** @param {?proto.bmore.HttpRequest|undefined} value */
proto.bmore.Activity.prototype.setRequest = function(value) {
  jspb.Message.setOneofWrapperField(this, 4, proto.bmore.Activity.oneofGroups_[0], value);
};


proto.bmore.Activity.prototype.clearRequest = function() {
  this.setRequest(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.bmore.Activity.prototype.hasRequest = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional Chat chat = 5;
 * @return {?proto.bmore.Chat}
 */
proto.bmore.Activity.prototype.getChat = function() {
  return /** @type{?proto.bmore.Chat} */ (
    jspb.Message.getWrapperField(this, proto.bmore.Chat, 5));
};


/** @param {?proto.bmore.Chat|undefined} value */
proto.bmore.Activity.prototype.setChat = function(value) {
  jspb.Message.setOneofWrapperField(this, 5, proto.bmore.Activity.oneofGroups_[0], value);
};


proto.bmore.Activity.prototype.clearChat = function() {
  this.setChat(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.bmore.Activity.prototype.hasChat = function() {
  return jspb.Message.getField(this, 5) != null;
};


