export default function cleanSet(set, startString) {
  if (startString.length === 0) {
    return '';
  }
  if (typeof startString !== 'string') {
    return '';
  }
  const newArray = Array.from(set).filter((each) => each.includes(startString));
  const result = newArray.map((each) => each.slice(startString.length)).join('-');
  return result;
}
