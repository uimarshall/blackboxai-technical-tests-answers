const axios = require('axios');
const cheerio = require('cheerio');
const j2csv = require('json2csv').Parser;
const fs = require('fs');

const music =
  'https://books.toscrape.com/catalogue/category/books/music_14/index.html';

const baseUrl = 'https://books.toscrape.com/catalogue/category/books/music_14/';
const booksData = [];

async function getBooks(url) {
  try {
    const response = await axios.get(url);
    const $ = cheerio.load(response.data);

    const books = $('article');
    books.each(function () {
      title = $(this).find('h3 a').text();
      price = $(this).find('.price_color').text();
      stock = $(this).find('.availability').text().trim();
      booksData.push({ title, price, stock });
    });

    // Handle pagination
    if ($('.next a').length > 0) {
      nextPage = baseUrl + $('.next a').attr('href');
      getBooks(nextPage);
    } else {
      const parser = new j2csv();
      const csv = parser.parse(booksData);
      fs.writeFileSync('./books.csv', csv);
    }

    console.log(booksData);
  } catch (error) {
    console.error(error);
  }
}

getBooks(music);
