#pragma once

#include "../Engine/engine.cpp"
#include "save_and_load.hpp"

#include <iostream>

namespace Program
{
    void Init()
    {
        Options::FPS = 1;
        std::cout << "Init\n";
    }

    void Update()
    {
        std::cout << "Update\n";
    }

    void End()
    {
        std::cout << "End\n";
    }
}
