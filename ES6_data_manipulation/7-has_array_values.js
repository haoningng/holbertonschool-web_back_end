export default function hasValuesFromArray(set, array) {
  if (array.filter((each) => set.has(each)).length === array.length) {
    return true;
  }
  return false;
}
