cmake_minimum_required(VERSION 3.28)
project(2023 C)

set(CMAKE_C_STANDARD 11)

add_executable(2023 main.c
        stats.c
        stats.h
        arbre.c
        arbre.h
)
