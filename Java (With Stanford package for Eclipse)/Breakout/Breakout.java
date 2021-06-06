/*
 * File: Breakout.java
 * -------------------
 * Name:
 * Section Leader:
 * 
 * This file will eventually implement the game of Breakout.
 */

import acm.graphics.*;
import acm.program.*;
import acm.util.*;

import java.applet.*;
import java.awt.*;
import java.awt.event.*;

public class Breakout extends GraphicsProgram {

/** Width and height of application window in pixels */
	public static final int APPLICATION_WIDTH = 400;
	public static final int APPLICATION_HEIGHT = 600;

/** Dimensions of game board (usually the same) */
	private static final int WIDTH = APPLICATION_WIDTH;
	private static final int HEIGHT = APPLICATION_HEIGHT;

/** Dimensions of the paddle */
	private static final int PADDLE_WIDTH = 60;
	private static final int PADDLE_HEIGHT = 10;

/** Offset of the paddle up from the bottom */
	private static final int PADDLE_Y_OFFSET = 30;

/** Number of bricks per row */
	private static final int NBRICKS_PER_ROW = 10;

/** Number of rows of bricks */
	private static final int NBRICK_ROWS = 10;

/** Separation between bricks */
	private static final int BRICK_SEP = 2;

/** Width of a brick */
	private static final int BRICK_WIDTH =
	  (WIDTH - (NBRICKS_PER_ROW - 1) * BRICK_SEP) / NBRICKS_PER_ROW;

/** Height of a brick */
	private static final int BRICK_HEIGHT = 8;

/** Radius of the ball in pixels */
	private static final int BALL_RADIUS = 5;

/** Offset of the top brick row from the top */
	private static final int BRICK_Y_OFFSET = 70;

/** Number of turns */
	private static final int NTURNS = 3;
	private static final int DELAY = 10;
	private GRect paddle = new GRect(0,0);
	private GLabel count = new GLabel("");
	private GLabel lost = new GLabel("Play Again!", APPLICATION_WIDTH/2- new GLabel("Play Again!").getWidth()/2, APPLICATION_HEIGHT/2);
	private GRect rect = new GRect(lost.getX()-10, lost.getY()-20, lost.getWidth() + 20, lost.getHeight() + 20);
	/* Method: run() */
/** Runs the Breakout program. */
	public void run() {
		//set up ball
		GOval ball = new GOval(0,0);
		double vx = 0;
		vx = setx(vx);
		double vy = 3.0;
		setball(ball);
		//set up paddle
		setpaddle(paddle);
		//set up bricks
		setbricks();
		//count down to start game
		countdown();
		
		while(true) {
			moveball(ball, vx, vy);
			vx = checksides(ball, vx);
			vy = checktop(ball, vy);
			if(checklost(ball)) break;
			if(hitinteractionpaddle(ball, paddle, vy)) vy = -vy;
			else {
				vx = hitinteractionx(ball, vx, paddle);
				vy = hitinteractiony(ball, vy, paddle);
			}
			
			pause(DELAY);
			
		}
			
			
		
	}
	public void setbricks() {
		Color color = Color.red;
		brickRow(BRICK_Y_OFFSET, color);
		brickRow(BRICK_Y_OFFSET+BRICK_HEIGHT+BRICK_SEP, color);
		color = Color.orange;
		brickRow(BRICK_Y_OFFSET+(BRICK_HEIGHT+BRICK_SEP)*2, color);
		brickRow(BRICK_Y_OFFSET+(BRICK_HEIGHT+BRICK_SEP)*3, color);
		color = Color.yellow;
		brickRow(BRICK_Y_OFFSET+(BRICK_HEIGHT+BRICK_SEP)*4, color);
		brickRow(BRICK_Y_OFFSET+(BRICK_HEIGHT+BRICK_SEP)*5, color);
		color = Color.green;
		brickRow(BRICK_Y_OFFSET+(BRICK_HEIGHT+BRICK_SEP)*6, color);
		brickRow(BRICK_Y_OFFSET+(BRICK_HEIGHT+BRICK_SEP)*7, color);
		color = Color.cyan;
		brickRow(BRICK_Y_OFFSET+(BRICK_HEIGHT+BRICK_SEP)*8, color);
		brickRow(BRICK_Y_OFFSET+(BRICK_HEIGHT+BRICK_SEP)*9, color);
	}
	public void brickRow(int y, Color color) {
		int x = 0;
		for(int i=0; i < NBRICKS_PER_ROW; i++) {
			GRect cyan = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);
			cyan.setFilled(true);
			cyan.setFillColor(color);
			add(cyan);
			x += BRICK_WIDTH + BRICK_SEP;
		}
	}
	public void setpaddle(GRect paddle){
		paddle.setLocation(APPLICATION_WIDTH/2-PADDLE_WIDTH/2, APPLICATION_HEIGHT-PADDLE_Y_OFFSET);
		paddle.setSize(PADDLE_WIDTH, PADDLE_HEIGHT);
		paddle.setFilled(true);
		paddle.setColor(Color.BLACK);
		add(paddle);
		addMouseListeners();
	}
	public void setball(GOval ball) {
		ball.setLocation(APPLICATION_WIDTH/2-BALL_RADIUS, APPLICATION_HEIGHT/2-BALL_RADIUS+100);
		ball.setSize(2*BALL_RADIUS, 2*BALL_RADIUS);
		ball.setFilled(true);
		ball.setColor(Color.BLACK);
		add(ball);
	}
	public double setx(double vx) {
		RandomGenerator rgen = RandomGenerator.getInstance();
		vx = rgen.nextDouble(1.0,3.0);
		if(rgen.nextBoolean(.5)) vx = -vx;
		return vx;
	}
	public void countdown() {
		count.setLocation(APPLICATION_WIDTH/2-count.getWidth()/2,APPLICATION_HEIGHT/2);
		count.setLabel("3");
		add(count);
		pause(1000);
		count.setLabel("2");
		pause(1000);
		count.setLabel("1");
		pause(1000);
		remove(count);
	}
	public void mouseMoved(MouseEvent e) {
		if(e.getX() <= APPLICATION_WIDTH-PADDLE_WIDTH/2 && e.getX() >= PADDLE_WIDTH/2) {
		paddle.setLocation(e.getX()-PADDLE_WIDTH/2,APPLICATION_HEIGHT-PADDLE_Y_OFFSET);
		}
	}
	public void moveball(GOval ball, double vx, double vy) {
		ball.move(vx, vy);
	}
	public double checksides(GOval ball, double vx) {
		if(ball.getX() <= 0 || ball.getX() >= APPLICATION_WIDTH-2*BALL_RADIUS) return -vx;
		else return vx;
	}
	public double checktop(GOval ball, double vy) {
		if(ball.getY() <= 0 || getElementAt(ball.getX(),ball.getY()+2*BALL_RADIUS) == paddle || getElementAt(ball.getX()+BALL_RADIUS,ball.getY()+2*BALL_RADIUS) == paddle || getElementAt(ball.getX()+2*BALL_RADIUS,ball.getY()+2*BALL_RADIUS) == paddle || getElementAt(ball.getX()-1,ball.getY()+BALL_RADIUS) == paddle || getElementAt(ball.getX()+2*BALL_RADIUS+1,ball.getY()+BALL_RADIUS) == paddle) return -vy;
		else return vy;
	}
	public boolean checklost(GOval ball) {
		if(ball.getY() >= APPLICATION_HEIGHT-2*BALL_RADIUS) {
			add(lost);
			add(rect);
			return true;
		}
		else return false;
	}
	public boolean hitinteractionpaddle(GOval ball, GRect paddle, double vy) {
		if(ball.getY()+2*BALL_RADIUS >= APPLICATION_HEIGHT-PADDLE_Y_OFFSET-PADDLE_HEIGHT && ball.getY() + 2*BALL_RADIUS <= APPLICATION_HEIGHT-PADDLE_Y_OFFSET) {
			if(ball.getX()+2*BALL_RADIUS <= paddle.getX() && ball.getX() >= paddle.getX() + PADDLE_WIDTH) {
				return true;
			}
		}
		return false;
	}

	public double hitinteractiony(GOval ball, double vy, GRect paddle) {
		if(getElementAt(ball.getX()+BALL_RADIUS/2, ball.getY()) != null || getElementAt(ball.getX()+3*BALL_RADIUS/2, ball.getY()) != null || getElementAt(ball.getX()+BALL_RADIUS/2, ball.getY()+2*BALL_RADIUS) != null || getElementAt(ball.getX()+3*BALL_RADIUS/2, ball.getY()+2*BALL_RADIUS) != null) {
			if(getElementAt(ball.getX()+BALL_RADIUS/2, ball.getY()) != null) remove(getElementAt(ball.getX()+BALL_RADIUS/2, ball.getY()));
			if(getElementAt(ball.getX()+3*BALL_RADIUS/2, ball.getY()) != null) remove(getElementAt(ball.getX()+3*BALL_RADIUS/2, ball.getY()));
			if(getElementAt(ball.getX()+BALL_RADIUS/2, ball.getY()+2*BALL_RADIUS) != null) remove(getElementAt(ball.getX()+BALL_RADIUS/2, ball.getY()+2*BALL_RADIUS));
			if(getElementAt(ball.getX()+3*BALL_RADIUS/2, ball.getY()+2*BALL_RADIUS) != null) remove(getElementAt(ball.getX()+3*BALL_RADIUS/2, ball.getY()+2*BALL_RADIUS));
			return -vy;
		}
		else return vy;
	}
	public double hitinteractionx(GOval ball, double vx, GRect paddle) {
		if(getElementAt(ball.getX(), ball.getY()+BALL_RADIUS/2) != null || getElementAt(ball.getX(), ball.getY()+3*BALL_RADIUS/2) != null || getElementAt(ball.getX()+2*BALL_RADIUS, ball.getY()+BALL_RADIUS/2) != null || getElementAt(ball.getX()+2*BALL_RADIUS, ball.getY()+3*BALL_RADIUS/2) != null) {
			if(getElementAt(ball.getX(), ball.getY()+BALL_RADIUS/2) != null) remove(getElementAt(ball.getX(), ball.getY()+BALL_RADIUS/2));
			if(getElementAt(ball.getX(), ball.getY()+3*BALL_RADIUS/2) != null) remove(getElementAt(ball.getX(), ball.getY()+3*BALL_RADIUS/2));
			if(getElementAt(ball.getX()+2*BALL_RADIUS, ball.getY()+BALL_RADIUS/2) != null) remove(getElementAt(ball.getX()+2*BALL_RADIUS, ball.getY()+BALL_RADIUS/2));
			if(getElementAt(ball.getX()+2*BALL_RADIUS, ball.getY()+3*BALL_RADIUS/2) != null) remove(getElementAt(ball.getX()+2*BALL_RADIUS, ball.getY()+3*BALL_RADIUS/2));
			return -vx;
		}
		else return vx;
	}
}
