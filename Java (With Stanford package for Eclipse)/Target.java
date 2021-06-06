/*
 * File: Target.java
 * Name: 
 * Section Leader: 
 * -----------------
 * This file is the starter file for the Target problem.
 */

import acm.graphics.*;
import acm.program.*;
import java.awt.*;

public class Target extends GraphicsProgram {	
	public static final int APPLICATION_HEIGHT= 300;
	public static final int APPLICATION_WIDTH=300;
	public void run() {
		/* You fill this in. */
		GOval red1 = new GOval((APPLICATION_WIDTH/2)-36, (APPLICATION_HEIGHT/2)-36, 72, 72);
		red1.setFilled(true);
		red1.setColor(Color.RED);
		add(red1);
		GOval white = new GOval((APPLICATION_WIDTH/2)-23, (APPLICATION_HEIGHT/2)-23, 46, 46);
		white.setFilled(true);
		white.setColor(Color.WHITE);
		add(white);
		GOval red2 = new GOval((APPLICATION_WIDTH/2)-10, (APPLICATION_HEIGHT/2)-10, 20, 20);
		red2.setFilled(true);
		red2.setColor(Color.RED);
		add(red2);
	}
}
