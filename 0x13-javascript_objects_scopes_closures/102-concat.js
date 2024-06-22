#!/usr/bin/node
const fs = require('fs');

try {
  // Read the contents of the first source file
  const source1 = fs.readFileSync(process.argv[2], 'utf8');

  // Read the contents of the second source file
  const source2 = fs.readFileSync(process.argv[3], 'utf8');

  // Write the concatenated contents to the destination file
  fs.writeFileSync(process.argv[4], source1 + source2);

  console.log(`Successfully concatenated ${process.argv[2]} and ${process.argv[3]} into ${process.argv[4]}`);
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}
