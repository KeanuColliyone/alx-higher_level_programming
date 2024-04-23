const fs = require('fs');

const [, , fileAPath, fileBPath, fileCPath] = process.argv;

fs.readFile(fileAPath, 'utf8', (err, fileAData) => {
  if (err) {
    console.error(`Error reading ${fileAPath}: ${err}`);
    return;
  }

  fs.readFile(fileBPath, 'utf8', (err, fileBData) => {
    if (err) {
      console.error(`Error reading ${fileBPath}: ${err}`);
      return;
    }

    const concatenatedData = fileAData + fileBData;

    fs.writeFile(fileCPath, concatenatedData, (err) => {
      if (err) {
        console.error(`Error writing to ${fileCPath}: ${err}`);
        return;
      }
      console.log(`Concatenation successful. Output written to ${fileCPath}`);
    });
  });
});
