export default function getListStudentIds(list) {
  if (Array.isArray(list)) {
    return list.map((each) => each.id);
  }
  return [];
}
