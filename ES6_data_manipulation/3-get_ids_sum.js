export default function getStudentIdsSum(list) {
  const newList = list.map((each) => each.id);
  return newList.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
}
