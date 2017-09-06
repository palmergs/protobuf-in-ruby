protoc --ruby_out=rails/app/models/bmore --python_out=django/chat/bmore --js_out=hapi/bmore --proto_path=protobuf protobuf/messages.proto

PATH=~/go/bin:$PATH
protoc --go_out=go/src/bmore --proto_path=protobuf protobuf/messages.proto
