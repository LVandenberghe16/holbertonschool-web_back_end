export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const studentsInCity = studentList.filter((student) => student.location === city);

  const updatedStudents = studentsInCity.map((studentGrade) => {
    const gradeEntry = newGrades.find((grade) => grade.studentId === studentGrade.id);

    return {
      ...studentGrade,
      grade: gradeEntry ? gradeEntry.grade : 'N/A',
    };
  });

  return updatedStudents;
}
