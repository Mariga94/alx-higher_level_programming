const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$(document).ready(function () {
  $.get(url, function (data, textStatus, jqXHR) {
    $('UL#list_movies').append(data.results.map(item => {
      return `<li>${item.title}</li>`;
    }));
  });
});
