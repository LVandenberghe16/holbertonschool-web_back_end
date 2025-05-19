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
  try {
    const fileFd = fs.openSync(file, 'r');
    const stats = fs.fstatSync(fileFd);
    const fileSize = stats.size;
    const buffer = Buffer.alloc(fileSize);
    const bytesRead = fs.readSync(fileFd, buffer, 0, fileSize, 0);
    const data = buffer.toString('utf8', 0, bytesRead);
    const dataLine = data.split('\n');
    if (dataLine.length > 0 && dataLine[dataLine.length - 1].trim() === '') {
      dataLine.pop();
    }
    dataLine.shift();
    fs.closeSync(fileFd);
    const result = parseStudents(dataLine);
    console.log(`Number of students: ${dataLine.length}\nNumber of students in CS: ${result.csCount}. List: ${result.csStudent.join(', ')}\nNumber of students in SWE: ${result.sweCount}. List: ${result.sweStudent.join(', ')}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
