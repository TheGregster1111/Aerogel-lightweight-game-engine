# How to build game

Open CMakeLists.txt and switch which COMMAND is commented based on OS.
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

```console
user@pc:~/Aerogel$ cmake .
user@pc:~/Aerogel$ cmake --build .
```