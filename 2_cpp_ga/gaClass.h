// gaClass.h, city3114_proc2, jake deery, 2020
#pragma once
#ifndef GACLASS_H
#define GACLASS_H

// include
#include <iostream>
#include <math.h>

// typedef - float
typedef float float32_t;
typedef double float64_t;
typedef long double float96_t;

// namespace
using std::cout;



// class def
class gaClass {
	public:
		// vars
		
		// methods
		gaClass();
		~gaClass();
	private:
		// consts -- change these to change what happens
		// this is filthy and if i gave myself more time this would be less crappy
		static const int32_t bits = 20;
		static const int32_t dims = 2;
		static const int32_t individual = bits * dims; // total bits for one individual
		static const int32_t populationSize = 1000; // no. of individuals
		static const int32_t generations = 100; // max. gens
		const float32_t mutation = 0.001; // mutation probability
		const float32_t crossover = 0.6; // crossover probability
		
		// vars
		int32_t currentGen = 0;
		int32_t zz = 0;
		float64_t totalFit = 0.0;
		
		int32_t ind[populationSize][individual];//current generation
		int32_t newInd[populationSize][individual]; // next generation
		int32_t temp[individual]; // a place to store individual data
		int32_t person1[individual]; // person one
		int32_t person2[individual]; // person two
		float64_t fitness[populationSize]; // the fitness values for the population
		float64_t normFit[populationSize]; // ??
		
		
		
		// methods
		int initPopulation();
		int getFitness();
		int viewPopulation();
		int doCrossover();
		int mutate();
		int swapPopulation();
};

#endif // GACLASS_H
