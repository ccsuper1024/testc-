cmake_minimum_required(VERSION 3.20)
project(testEventLoop)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGE} -g -Wall")
message(STATUS "This is Binary dir" ${testEventLoop_BINARY_DIR})
message(STATUS "This is Source dir" ${testEventLoop_SOURCE_DIR})
file(GLOB SRC ./*.cc)
add_executable(testEventLoop ${SRC})