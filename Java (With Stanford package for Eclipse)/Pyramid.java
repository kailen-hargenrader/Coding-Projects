/*
 * File: Pyramid.java
 * Name: 
 * Section Leader: 
 * ------------------
 * This file is the starter file for the Pyramid problem.
 * It includes definitions of the constants that match the
 * sample run in the assignment, but you should make sure
 * that changing these values causes the generated display
 * to change accordingly.
 */

import acm.graphics.*;
import acm.program.*;
import java.awt.*;

public class Pyramid extends GraphicsProgram {
	
/** Width of each brick in pixels */
	private static final int BRICK_WIDTH = 30;

/** Width of each brick in pixels */
	private static final int BRICK_HEIGHT = 12;

/** Number of bricks in the base of the pyramid */
	private static int BRICKS_IN_BASE = 14;
	
	public static final int APPLICATION_HEIGHT=(BRICKS_IN_BASE+4)*BRICK_HEIGHT;
	public static final int APPLICATION_WIDTH=(BRICKS_IN_BASE+4)*BRICK_WIDTH;
	public void run() {
		/* You fill this in. */
		int BRICK_START = (APPLICATION_WIDTH-BRICKS_IN_BASE*BRICK_WIDTH)/2;
		int BRICK_DOWN = (APPLICATION_HEIGHT-BRICK_WIDTH);
		for(int j = 0; j < BRICKS_IN_BASE; j++) {
			
			for(int i = 0; i < (BRICKS_IN_BASE-j); i++){
				
				add(new GRect(BRICK_START, BRICK_DOWN, BRICK_WIDTH, BRICK_HEIGHT));
				BRICK_START += BRICK_WIDTH;
			}
			
			BRICK_START = BRICK_START-BRICK_WIDTH*(BRICKS_IN_BASE-j-1)-BRICK_WIDTH/2;
			BRICK_DOWN = BRICK_DOWN-BRICK_HEIGHT;
		}
	}
}

