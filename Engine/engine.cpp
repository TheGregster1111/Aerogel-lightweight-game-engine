#pragma once

#include "../options.hpp"
#include "audio.hpp"
#include "classes.hpp"
#include "game_objects.hpp"
#include "input.hpp"
#include "localization.hpp"
#include "physics.hpp"
#include "Renderer/renderer.hpp"
#include "../Program/main.hpp"

#include <iostream>
#include <thread>
#include <cmath>
#include <fstream>
#include <cstring>
#include <gtk/gtk.h>

#define Log(x) logFile << x << "\n\n"

// Update

gboolean main_update(gpointer data)
{
    Program::Update();
    Renderer::Update();

    std::this_thread::sleep_for(std::chrono::microseconds(int(round(1'000'000 / Options::FPS))));

    return true;
}

// Init and end
int main(int argc, char const *argv[])
{
    bool running = true;
    std::cout << argv[0] << "\n";

    #ifdef _WIN32
    char pathSeparator = '\\';
    #else
    char pathSeparator = '/';
    #endif
    std::string path = "";
    std::string buffer = "";
    for (int i = 0; argv[0][i] != '\0'; i++)
    {
        buffer += argv[0][i];
        if (argv[0][i] == pathSeparator)
            path += buffer;
    }

    std::cout << buffer << "\n";

    std::ofstream logFile(path + "log.txt");
    Log("Initializing - Start");

    Program::Init();
    Window::Init(Options::WindowHeight, Options::WindowWidth, Options::WindowTitle, logFile, Options::FPS);

    Log("Initializing - End");

    /* while (running)
    {
        Program::Update();
        Renderer::Update();

        std::this_thread::sleep_for(std::chrono::microseconds(int(round(1'000'000/Options::FPS))));
    } */

    Log("Program end - Start");
       
    Program::End();

    Log("Program end - End");
    return 0;
}
