import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const newList = [];
  newList.push(new ClassRoom(19));
  newList.push(new ClassRoom(20));
  newList.push(new ClassRoom(34));
  return newList;
}
