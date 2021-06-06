/*
 * File: Hailstone.java
 * Name: 
 * Section Leader: 
 * --------------------
 * This file is the starter file for the Hailstone problem.
 */

import acm.program.*;

public class Hailstone extends ConsoleProgram {
	public void run() {
		int integer = readInt("Int; ");
		int count = 0;
		while(integer != 1) {
			if(integer%2==0) {
				integer = integer/2;
			}
			else {
				integer = integer*3+1;
			}
			println(integer);
			count++;
		}
		println("n = " + integer);
		println(count + " steps");
	}
}


