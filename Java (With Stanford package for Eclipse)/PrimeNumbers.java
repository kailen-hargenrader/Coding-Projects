/*
 * File: Car_Dice.java
 * --------------------
 * This program is a stub for the Assignment 8, which finds the
 * number of rolls it takes to win a car!!
 */

import acm.program.*;

import acm.util.RandomGenerator;

import java.util.*;

public class PrimeNumbers extends ConsoleProgram {

	public void run() {
		// You fill this in
		int sentinel = readInt("What is the maximum value: ");
		ArrayList<Integer> primes = new ArrayList<Integer>();
		for(int i = 0; i <= sentinel;i++) {
			if(primes.size() <= 1) {
				primes.add(i);
				
			
			}
			else{
				boolean prime = true;
				for(int j = 2; j<primes.size(); j++) {
					if(i%primes.get(j) == 0) {
						prime = false;
						break;
					}
				}
				if(prime == true) {
					primes.add(i);
					println(i);
				}
				
						
			}
		}
	}	
}

