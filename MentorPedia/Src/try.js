const fs = require('fs');
const path = require('path');
const directoryPath = './jsonfiles';
const outputFileName = 'combinedData.json';

fs.readdir(directoryPath, (err, files) => {
    if (err) {
        console.error('Error reading directory:', err);
        return;
    }
    // Array to hold the data from all files
    let combinedData = [];

    // Loop through each file
    files.forEach(file => {
        // Check if file has .json extension
        if (path.extname(file) === '.json') {
            try {
                // Read file content and parse JSON
                const data = fs.readFileSync(path.join(directoryPath, file), 'utf8');
                const jsonData = JSON.parse(data);
                // Concatenate data to combinedData array
                combinedData = combinedData.concat(jsonData);
            } catch (err) {
                console.error(`Error reading or parsing file '${file}':`, err);
            }
        }
    });

    // Write the combined data to the output file
    fs.writeFile(outputFileName, JSON.stringify(combinedData, null, 2), err => {
        if (err) {
            console.error('Error writing combined data to file:', err);
            return;
        }
        console.log(`Combined data successfully written to '${outputFileName}'.`);
    });
});
