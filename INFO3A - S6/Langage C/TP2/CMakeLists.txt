cmake_minimum_required(VERSION 3.28)
project(TP2 C)

set(CMAKE_C_STANDARD 11)

add_executable(TP2 main.c
        test.h
        test.c
        sort.c
        sort.h
        comparator.c
        comparator.h)
