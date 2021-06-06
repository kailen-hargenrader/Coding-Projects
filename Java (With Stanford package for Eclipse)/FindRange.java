/*
 * File: FindRange.java
 * Name: 
 * Section Leader: 
 * --------------------
 * This file is the starter file for the FindRange problem.
 */

import acm.program.*;

public class FindRange extends ConsoleProgram {
	public void run() {
		/* You fill this in */
		/* You fill this in */
		int now = readInt("?: ");
		if(now == 0) {
			println("No input");
		}
		else {
		int lowest = now;
		int highest = now;		
		while(now != 0) {
			now = readInt("?: ");
			if(now<lowest && now != 0) {
				lowest = now;
			}
			if (now>highest) {
				highest = now;
			}
		}
		println("smallest " + lowest);
		println("highest " + highest);
		}
		}
	}


