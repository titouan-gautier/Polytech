#pragma once

struct SStat
{
	unsigned int Stat[256];
};

struct SStat StatistiqueFichier(const char* path);
