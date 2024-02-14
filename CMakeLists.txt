cmake_minimum_required(VERSION 3.19)

project(GAME_NAME)

set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/Build)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})

find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

include_directories(${GTK_INCLUDE_DIRS})
link_directories(GAME_EXECUTABLE ${GTK3_LIBRARY_DIRS})

add_executable(GAME_EXECUTABLE "Engine/engine.cpp")

add_custom_target(
    run ALL
    COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/compile.py ${CMAKE_CURRENT_SOURCE_DIR}
)
add_custom_command(
    OUTPUT log    
    DEPENDS GAME_EXECUTABLE
    COMMAND cp -R Ass path_to_destination/    # Linux
    #COMMAND    # Windows
)

target_link_libraries(GAME_EXECUTABLE ${GTK3_LIBRARIES})