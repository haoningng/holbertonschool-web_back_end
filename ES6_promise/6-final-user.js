import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((values) => {
      const newList = [];
      for (const each of values) {
        newList.push({
          status: each.status,
          value: each.status === 'fulfilled' ? each.value : each.reason.message,
        });
      }
      return newList;
    });
}
