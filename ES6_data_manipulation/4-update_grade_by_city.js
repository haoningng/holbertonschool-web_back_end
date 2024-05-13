export default function updateStudentGradeByCity(list, city, newGrades) {
  return list.filter((each) => each.location === city).map((each) => {
    const grade = newGrades.filter((student) => student.studentId === each.id);
    return {
      ...each,
      grade: grade[0] ? grade[0].grade : 'N/A',
    };
  });
}
