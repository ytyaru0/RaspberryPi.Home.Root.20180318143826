#!/usr/local/bin/bats
@test "test Hello" {
    load ../src/C
    [ "Hello" = `EchoHello` ]
}
