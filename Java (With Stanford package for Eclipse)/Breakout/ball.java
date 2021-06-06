import acm.graphics.*;
import acm.program.*;
import acm.util.*;

import java.applet.*;
import java.awt.*;
import java.awt.event.*;
public class ball extends GOval{
	
	double vx;
	double vy = -2.0;
	long initiateTime = System.currentTimeMillis();
	
	public ball(double x, double y, double width, double height) {
		super(x, y, width, height);
		vx = setx(vx);
	}
	
	public double setx(double vx) {
		RandomGenerator rgen = RandomGenerator.getInstance();
		vx = rgen.nextDouble(1.0,2.0);
		if(rgen.nextBoolean(.5)) vx = -vx;
		return vx;
	}
	public void pause() {
		pause(1000);
	}
}
