const fs = require('node:fs');

function parseStudents(dataLine) {
  const csStudent = [];
  let csCount = 0;
  const sweStudent = [];
  let sweCount = 0;
  for (let i = 0; i < dataLine.length; i += 1) {
    const studentsData = dataLine[i].split(',');
    if (studentsData[3] === 'CS') {
      csCount += 1;
      csStudent.push(studentsData[1]);
    } else if (studentsData[3] === 'SWE') {
      sweCount += 1;
      sweStudent.push(studentsData[1]);
    }
  }
  return {
    csCount,
    csStudent,
    sweCount,
    sweStudent,
  };
}

function countStudents(file) {
  return new Promise((resolve, reject) => {
    fs.readFile(file, 'utf8', (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }
      const dataLine = data.split('\n');
      if (dataLine.length > 0 && dataLine[dataLine.length - 1].trim() === '') {
        dataLine.pop();
      }
      dataLine.shift();
      const result = parseStudents(dataLine);
      return resolve(`Number of students: ${dataLine.length}\nNumber of students in CS: ${result.csCount}. List: ${result.csStudent.join(', ')}\nNumber of students in SWE: ${result.sweCount}. List: ${result.sweStudent.join(', ')}`);
    });
  });
}

module.exports = countStudents;
