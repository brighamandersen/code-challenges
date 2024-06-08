// Find the country with the highest population programmatically
// Use foreign key ids to join data together and determine the country
// with the highest population based on the city/population data available

// Test input

const countries = [
  { id: 1, name: 'USA' },
  { id: 2, name: 'England' },
  { id: 3, name: 'Russia' },
  { id: 4, name: 'New Zealand' }
];

const cities = [
  { id: 1, countryId: 1, name: 'New York' },
  { id: 2, countryId: 1, name: 'Seattle' },
  { id: 3, countryId: 1, name: 'Los Angeles' },
  { id: 4, countryId: 1, name: 'Houston' },
  { id: 5, countryId: 1, name: 'San Diego' },
  { id: 6, countryId: 2, name: 'London' },
  { id: 7, countryId: 2, name: 'Manchester' },
  { id: 8, countryId: 3, name: 'Moscow' },
  { id: 9, countryId: 3, name: 'Novosibirsk' },
  { id: 10, countryId: 4, name: 'Auckland' },
  { id: 11, countryId: 4, name: 'Wellington' }
];

const populations = [
  { id: 1, cityId: 1, amount: 8419000 },
  { id: 2, cityId: 2, amount: 724305 },
  { id: 3, cityId: 3, amount: 3967000 },
  { id: 4, cityId: 4, amount: 2310000 },
  { id: 5, cityId: 5, amount: 1410000 },
  { id: 6, cityId: 6, amount: 8982000 },
  { id: 7, cityId: 7, amount: 553230 },
  { id: 8, cityId: 8, amount: 11920000 },
  { id: 9, cityId: 9, amount: 1511000 },
  { id: 10, cityId: 10, amount: 1657000 },
  { id: 11, cityId: 11, amount: 212700 }
];

// My Solution

countries.forEach((country) => {
  let countryPopulationSum = 0;
  cities.forEach((city) => {
    if (country.id === city.countryId) {
      populations.forEach((population) => {
        if (city.id === population.cityId) {
          countryPopulationSum += population.amount;
        }
      });
    }
  });
  country.population = countryPopulationSum;
});

let topCountry = countries[0];
countries.forEach((country) => {
  if (country.population > topCountry.population) {
    topCountry = country;
  }
});

console.log({ topCountry });
