/*
 * File: Fibonacci.java
 * --------------------
 * This program is a stub for the Fibonacci problem, which finds the
 * Fibonacci series up to a terminal value.
 */

import acm.program.*;

public class Fibonacci extends ConsoleProgram {

	public void run() {
		int fib = 0;
		int fib2 = 1;
		while(fib < 10000) {
			println(fib);
			fib = fib + fib2;
			fib2 = fib - fib2;
			}
		// You fill this in
	}

}

