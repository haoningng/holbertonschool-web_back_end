export default function createReportObject(employeesList) {
  const object = {
    allEmployees: { ...employeesList },
  };

  object.getNumberOfDepartments = (employeesList) => Object.keys(employeesList).length;

  return object;
}
