/*
Write a well documented (commented) program, "Point", which implements a Point data 
type with the following constructor: [MO4.2, MO4.3]

Point(double x, double y, double z) and, the following API: 
-double distanceto(Point q) it returns the Euclidean distance between this and q.
-The Euclidean distance between (x1, y1, z1) and (x2, y2, z2) is defined as sqrt( (x1-x2)^2 + (y1-y2)^2) + (z1-z2)^2).
-String toString() – it returns the string representation of the point. An example would be (2.3,4.5,3.0).
-Write a main method in the class that is used to test it.
-It should create two Point objects using input provided by the user on the command-line.
-Then it should print out the two points followed by their Euclidean distance

A sample run would be as follows.

>java Point 2.1 3.0 3.5 4 5.2 3.5
The first point is (2.1,3.0,3.5)
The second point is (4.0,5.2,3.5)
Their Euclidean distance is 2.90
*/



	//Create class Point and declare final double variables x,y,z for coordinates
public class Point{ 			
	double x;					
	double y;
	double z;

		//Initializes a point given as input with THIS keyword
	public Point(double x, double y, double z){			
		this.x = x;
		this.y = y;
		this.z = z;
}
		//Returns Euclidean distance between the points stored and call math.sqrt method
	public double distanceTo(Point second){  	  
		double dx = this.x - second.x;				
		double dy = this.y - second.y;
		double dz = this.z - second.z;
	return Math.sqrt(dx*dx + dy*dy + dz*dz);		 
 }
			//Call toString method to return the string representation of the point
		public String toString(){ return "(" + x + "," + y + "," + z + ")";    
 }

		//Call main method. Declare and initialize variables a,b,c,d,e,f and call parseDouble method.
public static void main(String[] args){				
	double a = Double.parseDouble(args[0]);			
	double b = Double.parseDouble(args[1]);			
	double c = Double.parseDouble(args[2]);			
	double d = Double.parseDouble(args[3]);
	double e = Double.parseDouble(args[4]);			
	double f = Double.parseDouble(args[5]);			
		
		//Delare point type and initialize. 
	Point t = new Point(a, b, c);					
	Point w = new Point(d, e, f);					
		
		//Call print method
	System.out.println("The first point is " + t);									
	System.out.println("The second point is " + w);									
	System.out.println("Their Euclidean distance is " + t.distanceTo(w));			
	}
 }
