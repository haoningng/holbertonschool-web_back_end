export default function getStudentsByLocation(list, city) {
  return list.filter((each) => each.location === city);
}
