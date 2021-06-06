import acm.program.*;


public class QuadSolver extends ConsoleProgram {

	double sol1,sol2;

	public void run() {
		double a,b,c, discriminant, xvertex, yvertex;
		a=1; //need to set a value other than 0 so we get into the main loop
		println("Welcome to the Quad Solver!");
		println();
		println();
		while (a!=0) {
			println("Please input values for a,b and c. a=0 quits the program.");
			a = readDouble("a: ");
			//breaks when a = 0
			if(a != 0) {
				b = readDouble("b: ");
				c = readDouble("c: ");
	
				//work out domain, range, U or n shape and vertex coordinates here
				
				//finds u or n shape, domain of a parabola is always R
				if(a > 0) println("This Parabola is a u shape.");
				else println("This Parabola is a n shape.");
				println("The domain is all real numbers.");
				
				//finds the vertex, then finds range based off of vertex and a
				xvertex = -b/(2*a);
				xvertex = Math.round(xvertex*100)/100.0;
				yvertex = vertex_yval(a, b, c, xvertex);
				yvertex = Math.round(yvertex*100)/100.0;
				if(a > 0) println("y >= " + yvertex);
				else println("y <= " + yvertex);
				println("The vertex is at (" + xvertex + ", " + yvertex + ")");
				println();
				
				//finds discriminant
				discriminant = discriminant(a,b,c);
				discriminant = Math.round(discriminant*100)/100.0;
				println("The discriminant is " + discriminant);
				
				//finds number of solutions based off of discriminant value, and the value of solutions
				if(discriminant < 0) {
					println("There are 0 solutions");
				}
				else if(discriminant == 0) {
					println("There is 1 solution");
					println("x = " + xvertex);
				}
				else {
					println("There are 2 solutions");
					solve(a, b, c, discriminant);
					println("x = " + sol1 + ", " + sol2);
				}
			}




			//I leave the rest up to you to figure out!!
			//you must use any methods that are set up below, and can also make your own.
		}
		println("Have a nice day!");

	}

	private double discriminant (double a,double b, double c) {
		double disc=b*b-4*a*c;

		//calculate and return the discriminant


		return disc;
	}

	private double vertex_yval(double a,double b, double c, double xvertex) {
		// calculate the y-value of the vertex, given the x value 
		// (you'll need to calculate that separately and send it into this method)
		double yvertex=a*xvertex*xvertex+b*xvertex+c;



		return yvertex;
	}


	private void solve (double a, double b, double c, double discriminant) {
		//calculate the two solutions and put them into sol1 and sol2
		// to do a squareroot, use a line like :
		//double d=Math.sqrt(23);
		sol1 = (-b+Math.sqrt(discriminant))/2*a;
		sol2 = (-b-Math.sqrt(discriminant))/2*a;



	}
}

