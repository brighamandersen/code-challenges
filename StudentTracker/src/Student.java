public class Student {
    private String idNum;
    private CollegeCourse[] courses;

    Student() {
        courses = new CollegeCourse[5];
    }

    public String getIdNum() {
        return idNum;
    }

    public void setIdNum(String idNum) {
        this.idNum = idNum;
    }

    public CollegeCourse getCourse(int pos) {
        return courses[pos];
    }

    public void setCourse(CollegeCourse course, int pos) {
        courses[pos] = course;
    }
}
