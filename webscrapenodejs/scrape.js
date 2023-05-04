const axios = require('axios');
const cheerio = require('cheerio');

const music =
  'https://books.toscrape.com/catalogue/category/books/music_14/index.html';

async function getMusicBooks(url) {
  try {
    const response = await axios.get(url);
    const $ = cheerio.load(response.data);
    const category = $('h1').text();
    console.log(category);
  } catch (error) {
    console.error(error);
  }
}

getMusicBooks(music);
