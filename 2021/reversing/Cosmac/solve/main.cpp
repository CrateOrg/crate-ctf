#include <iostream>
#include <chrono>
#include <thread>
#include "stdint.h"
#include "SDL2/SDL.h"


#include "chip8.h"

using namespace std;


// Keypad keymap
uint8_t keymap[16] = {
    SDLK_x,
    SDLK_1,
    SDLK_2,
    SDLK_3,
    SDLK_q,
    SDLK_w,
    SDLK_e,
    SDLK_a,
    SDLK_s,
    SDLK_d,
    SDLK_z,
    SDLK_c,
    SDLK_4,
    SDLK_r,
    SDLK_f,
    SDLK_v,
};

static uint8_t char2digit(char c) {
  return c - 0x30;
}

static void cycle(Chip8* chip8, int cycles) {
  for (int i = 0; i < cycles; ++i) {
    chip8->emulate_cycle();
  }
}

static void input_digit(Chip8* chip8, uint8_t digit) {
    chip8->key[digit] = 1;
    cycle(chip8, 100);
    chip8->key[digit] = 0;
    cycle(chip8, 100);
}

int main(int argc, char **argv) {

    // Command usage
    if (argc != 2) {
        cout << "Usage: chip8 <ROM file>" << endl;
        return 1;
    }

    Chip8 chip8 = Chip8();          // Initialise Chip8

    int w = 1024;                   // Window width
    int h = 512;                    // Window height

    // The window we'll be rendering to
    SDL_Window* window = NULL;

    // Initialize SDL
    if ( SDL_Init(SDL_INIT_EVERYTHING) < 0 ) {
        printf( "SDL could not initialize! SDL_Error: %s\n", SDL_GetError() );
        exit(1);
    }
    // Create window
    window = SDL_CreateWindow(
            "CHIP-8 Emulator",
            SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
            w, h, SDL_WINDOW_SHOWN
    );
    if (window == NULL){
        printf( "Window could not be created! SDL_Error: %s\n",
                SDL_GetError() );
        exit(2);
    }

    // Create renderer
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, 0);
    SDL_RenderSetLogicalSize(renderer, w, h);

    // Create texture that stores frame buffer
    SDL_Texture* sdlTexture = SDL_CreateTexture(renderer,
            SDL_PIXELFORMAT_ARGB8888,
            SDL_TEXTUREACCESS_STREAMING,
            64, 32);

    // Temporary pixel buffer
    uint32_t pixels[2048];

    int pin = 0;

    load:
    // Attempt to load ROM
    if (!chip8.load(argv[1]))
        return 2;

    cout << pin << "\n";

    // Init program
    cycle(&chip8, 1000);
    // tusental
    input_digit(&chip8, pin / 1000);
    input_digit(&chip8, (pin / 100) % 10);
    input_digit(&chip8, (pin / 10) % 10);
    input_digit(&chip8, pin % 10);
    cycle(&chip8, 2000);
    if (chip8.drawFlag) {
        chip8.drawFlag = false;

        // Store pixels in temporary buffer
        for (int i = 0; i < 2048; ++i) {
            uint8_t pixel = chip8.gfx[i];
            pixels[i] = (0x00FFFFFF * pixel) | 0xFF000000;
        }
        // Update SDL texture
        SDL_UpdateTexture(sdlTexture, NULL, pixels, 64 * sizeof(Uint32));
        // Clear screen and render
        SDL_RenderClear(renderer);
        SDL_RenderCopy(renderer, sdlTexture, NULL, NULL);
        SDL_RenderPresent(renderer);
    }
  for(;;) {
        SDL_Event e;
        while (SDL_PollEvent(&e)) {
            if (e.type == SDL_QUIT) exit(0);

            // Process keydown events
            if (e.type == SDL_KEYDOWN) {
                if (e.key.keysym.sym == SDLK_UP)
                  pin+=10;
                if (e.key.keysym.sym == SDLK_DOWN)
                  pin-=10;
                if (e.key.keysym.sym == SDLK_RIGHT)
                  pin+=1;
                if (e.key.keysym.sym == SDLK_LEFT)
                  pin-=1;
                if (e.key.keysym.sym == SDLK_ESCAPE)
                  exit(0);
              goto load;      // *gasp*, a goto statement!

            }
        }
  }
}
