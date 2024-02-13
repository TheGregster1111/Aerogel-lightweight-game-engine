#include "../options.hpp"
#include "audio.hpp"
#include "classes.hpp"
#include "game_objects.hpp"
#include "input.hpp"
#include "localization.hpp"
#include "physics.hpp"
#include "Renderer/renderer.hpp"
#include "../Program/main.hpp"

#include <thread>
#include <cmath>

int main(int argc, char const *argv[])
{
    Program::Init();

    while (true)
    {
        Program::Update();

        std::this_thread::sleep_for(std::chrono::milliseconds(int(round(1'000'000/Options::FPS))));
    }
       
    //Call Program::End() before exit
    return 0;
}
