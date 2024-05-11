export default async function handleResponseFromAPI(promise) {
  promise.then(() => {
    console.log('Got a response from the API');
    return {
      status: 200,
      body: 'Success',
    };
  }).catch(() => {
    const err = new Error();
    return err;
  });
}
