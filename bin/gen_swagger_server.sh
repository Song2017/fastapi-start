#!/usr/bin/env sh

# configuration
input="server/data/demo.yaml"
output="swagger-server"
type="python-fastapi"
pkg_name="http_server"
pkg_version="0.0.1"

source ./bin/generate_swagger_lib.sh
generate_swagger_lib $input $output $type $pkg_name $pkg_version