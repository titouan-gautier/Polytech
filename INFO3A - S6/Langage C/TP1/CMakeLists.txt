cmake_minimum_required(VERSION 3.27)
project(TP1 C)

set(CMAKE_C_STANDARD 11)

add_executable(TP1 main.c
        automate.c
        stack.c
        stack.h
        automate.h)
