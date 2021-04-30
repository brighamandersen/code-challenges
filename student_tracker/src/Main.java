import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final int NUM_STUDENTS = 10;
        final int NUM_COURSES = 5;
        Student[] students = new Student[NUM_STUDENTS];
        Scanner scanner = new Scanner(System.in);
        boolean isValidInput = true;

        System.out.println("Hi professor!  Welcome to Student Tracker.");
        System.out.println("You have " + NUM_STUDENTS + " students.  Enter their information below.\n");

        for (int i = 0; i < NUM_STUDENTS; i++) {
            // Input student ID
            System.out.print("Enter ID for student #" + (i + 1) + ":  ");
            students[i] = new Student();
            students[i].setIdNum(scanner.next());

            for (int j = 0; j < NUM_COURSES; j++) {
                CollegeCourse course = new CollegeCourse();

                // Input course ID
                System.out.print("\tEnter course ID #" + (j + 1) + ":  ");
                course.setCourseId(scanner.next());

                // Input credit hours
                do {
                    try {
                        System.out.print("\t\tEnter # of credit hours:  ");
                        int hours = scanner.nextInt();
                        isValidInput = true;
                        course.setCreditHours(hours);

                    } catch (InputMismatchException e) {
                        isValidInput = false;
                        System.out.println("Invalid input. Number required.");
                        scanner.nextLine();
                    }
                } while (!isValidInput);

                // Input letter grade
                do {
                    System.out.print("\t\tEnter letter grade:  ");
                    char grade = scanner.next().charAt(0);

                    if (grade == 'a' || grade == 'b'|| grade == 'c' || grade == 'd'|| grade == 'f') {
                        isValidInput = true;
                        course.setLetterGrade(grade);
                    } else {
                        isValidInput = false;
                        System.out.println("Invalid input.  Valid letter grades are A, B, C, D, and F.");
                        scanner.nextLine();
                    }
                } while (!isValidInput);

                students[i].setCourse(course, j);
            }
            System.out.println();
        }

        // Print results
        System.out.println("-----------------------------------");
        System.out.println("Saved Student Information\n");
        for (int i = 0; i < NUM_STUDENTS; i++) {

            System.out.println("Student #" + (i + 1) + " ID:  " + students[i].getIdNum());

            for (int j = 0; j < NUM_COURSES; j++) {
                CollegeCourse curCourse = students[i].getCourse(j);
                System.out.println("\tCourse #" + (j + 1) + " ID:  " + curCourse.getCourseId());
                System.out.println("\t\t# of credit hours:  " + curCourse.getCreditHours());
                System.out.println("\t\tLetter grade:  " + curCourse.getLetterGrade());
            }
            System.out.println();
        }

    }
}
