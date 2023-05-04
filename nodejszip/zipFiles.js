const JSZip = require('jszip');
const fs = require('fs');

const zip = new JSZip();

try {
  const pdfData = fs.readFileSync('example.pdf');
  zip.file('PDFFile.pdf', pdfData);

  zip.file('Textfile.txt', 'I am generating this file to be zipped\n');

  const images = ['avatar-1.jpg', 'avatar-2.jpg'];
  const img = zip.folder('images');

  for (const image of images) {
    const imageData = fs.readFileSync(image);
    img.file(image, imageData);
  }

  zip
    .generateNodeStream({ type: 'nodebuffer', streamFiles: true })
    .pipe(fs.createWriteStream('example.zip'))
    .on('finish', function () {
      console.log('example.zip created.');
    });
} catch (err) {
  console.error(err);
}
