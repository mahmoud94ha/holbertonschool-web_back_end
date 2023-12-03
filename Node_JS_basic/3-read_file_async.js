const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(Error('Cannot load the database'));
        return;
      }
      const byLine = data.split('\n').filter((line) => line.trim() !== '');
      let totalStudents = 0;
      const studentsByField = {};
      for (let i = 1; i < byLine.length; i += 1) {
        const elements = byLine[i].split(',');
        const field = elements[3];
        const firstname = elements[0];
        if (field) {
          if (studentsByField[field] === undefined) {
            studentsByField[field] = {};
          }
          if (studentsByField[field][firstname] === undefined) {
            studentsByField[field][firstname] = 1;
          } else {
            studentsByField[field][firstname] += 1;
          }
        }
        totalStudents += 1;
      }

      console.log(`Number of students: ${totalStudents}`);
      for (const field in studentsByField) {
        if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
          const firstnameByField = Object.keys(studentsByField[field]);
          console.log(
            `Number of students in ${field}: ${Object.values(studentsByField[field]).reduce((a, b) => a + b, 0)}. List: ${firstnameByField.join(', ')}`,
          );
        }
      }
      resolve();
    });
  });
}

module.exports = countStudents;