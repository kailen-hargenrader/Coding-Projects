/*
 * File: ChangeMachine.java
 * 
 */

import acm.program.*;

public class ChangeMachine extends ConsoleProgram {
	// you will only use these instance variables if you move up to the second level
	private int numDollars=10;
	private int numQuarters=10;
	private int numDimes=10;
	private int numNickels=10;
	private int numPennies=10;
	
	public void run() {
		println("Welcome to my vending machine!!");
		double itemPrice=readDouble("What is the price of the item(s) you are purchasing (only 2 d.p. please!) ?");
		double dollarInput=readDouble("How much money are you putting into the machine (only 2 d.p. please!) ?");

		while (itemPrice!=0.00) {
			int changeTotal=(int)((dollarInput - itemPrice)*100);
			println("The total change is: " + changeTotal + " cents.");

			// Here is where your code will go (at least for the first part!!
			int droppedDollars = 0;
			while(changeTotal >= 100 && numDollars > 0) {
				droppedDollars += 1;
				changeTotal -= 100;
				numDollars -= 1;
			}
			int droppedQuarters = 0;
			while(changeTotal >= 25 && numQuarters > 0) {
				droppedQuarters += 1;
				changeTotal -= 25;
				numQuarters -= 1;
			}
			int droppedDimes = 0;
			while(changeTotal >= 10 && numDimes > 0) {
				droppedDimes += 1;
				changeTotal -= 10;
				numDimes -=1;
			}
			int droppedNickels = 0;
			while(changeTotal >= 5 && numNickels > 0) {
				droppedNickels += 1;
				changeTotal -= 5;
				numNickels -= 1;
			}
			int droppedPennies = 0;
			while(changeTotal >= 1 && numPennies > 0) {
				droppedPennies += 1;
				changeTotal -= 1;
				numPennies -= 1;
			}
			if(changeTotal != 0) {
				println("No possible change!");
			}
			else {
				while(droppedDollars >0) {
					dropCoin(100);
					droppedDollars -= 1;
				}
				while(droppedQuarters >0) {
					dropCoin(25);
					droppedQuarters -= 1;
				}
				while(droppedDimes >0) {
					dropCoin(10);
					droppedDimes -= 1;
				}
				while(droppedNickels >0) {
					dropCoin(5);
					droppedNickels -= 1;
				}
				while(droppedPennies >0) {
					dropCoin(1);
					droppedPennies -= 1;
				}
			}
				

			itemPrice=readDouble("What is the price of the item(s) you are purchasing (only 2 d.p. please!) ?");
			dollarInput=readDouble("How much money are you putting into the machine (only 2 d.p. please!) ?");
		}
		
	}
	
	private void dropCoin(int val) {
		
		if (val == 100) {
			println("Dollar");
			// in real-life code there would be an actual call to a physical
			//mechanism that would drop the actual coin here!
		}
		else if (val == 25) {
			println("Quarter");
			// in real-life code there would be an actual call to a physical
			//mechanism that would drop the actual coin here!
		}
		else if (val == 10) {
			println("Dime");
			// in real-life code there would be an actual call to a physical
			//mechanism that would drop the actual coin here!
		}
		else if (val == 5) {
			println("Nickel");
			// in real-life code there would be an actual call to a physical
			//mechanism that would drop the actual coin here!
		}
		else if (val == 1) {
			println("Penny");
			// in real-life code there would be an actual call to a physical
			//mechanism that would drop the actual coin here!
		}
		else println("Not a coin value!!");
	}
}