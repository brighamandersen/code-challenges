function lodash_get(obj, path) {
  // Grab each field in path, separated by '.'s
  const pathArr = path.split('.');

  // Loop through the fields and drill down the object
  let current = obj;
  for (const field of pathArr) {
    current = current[field];

    // Just break out early if we can't find the field
    if (!current) return current;
  }
  return current;
}

const user = {
  name: 'John Doe',
  address: {
    city: 'San Francisco'
  }
};

// Valid cases
console.log(lodash_get(user, 'name'));
console.log(lodash_get(user, 'address.city'));

// Invalid cases
console.log(lodash_get(user, 'name.first'));
console.log(lodash_get(user, 'address.country'));
