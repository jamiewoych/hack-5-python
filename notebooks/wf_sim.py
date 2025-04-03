#!/usr/bin/env python
"""
WF model in a script
"""

import argparse
import random
    
def init(N, f):
    pop = []
    frac = N*f
    for i in range(N):
        if i < frac:
            pop.append(1)
        else:
            pop.append(0)
    return(pop)

def step(pop):
    N = len(pop)
    new_pop = random.choices(pop, k = N)
    return(new_pop)

def wf(N, f, ngens, verbose =False): #add outfile
    if args.verbose:
        print("verbosity is on")
    pop = init(N, f)
    
    #if outfile write file, else:
    for i in range(ngens):
        pop = step(pop)
    x = (sum(pop)/N)
    return(f"generations= {ngens} ; f= {x} ; N={N}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", help ="population", dest='N', type=int, default =10)
    parser.add_argument("-f", help="frequency", dest='f', type=float, default=0.2)
    parser.add_argument("-g", help="ngens", dest='ngens', type=int, default=1)
    #parser.add_argument("-o", help ="write out community state at each given step", dest=outfile, default=stdout ,type=argparse.FileType('w') , action=?)
    
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action ="store_true")
    args = parser.parse_args()   

    if args.verbose:
        print(args)
 
    print(wf(N=args.N, f=args.f, ngens=args.ngens, verbose=args.verbose))
    



        
    
    