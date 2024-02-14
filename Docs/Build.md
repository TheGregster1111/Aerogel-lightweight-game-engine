# How to build game

Open CMakeLists.txt and edit this line based on OS.
```CMake
add_custom_command(
    TARGET GAME_EXECUTABLE POST_BUILD
    COMMAND cp -R Assets/ Build/Assets    # Linux   <<<
    #COMMAND                              # Windows <<<
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Copying assets..."
)
```
\
\
Then enter these two commands into the terminal:

```shell
user@pc:~/Aerogel$ cmake .
user@pc:~/Aerogel$ cmake --build .
```