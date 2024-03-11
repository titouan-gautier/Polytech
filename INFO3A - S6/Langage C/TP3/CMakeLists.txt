cmake_minimum_required(VERSION 3.28)
project(TP3 C)

set(CMAKE_C_STANDARD 11)

add_executable(TP3 main.c
        liste.h
        liste.c
        listeBlocMemoire.h
        listeBlocMemoire.c)
