# Calling the Placeholder API

```javascript
const fetch = require('node-fetch').default;

(async () => {
  const response = await fetch('https://jsonplaceholder.typicode.com/todoz/1', {
    method: 'GET',
    headers: {
      'Accept': 'application/json'
    }
  });

  console.log('HTTP Status:', response.status);

  let bodyText = await response.text();
  let body;
  try {
    body = JSON.parse(bodyText);
  } catch {
    body = bodyText;
  }

  if (!response.ok) {
    throw new Error(`HTTP Error: ${response.status} ${response.statusText}\nError body: ${JSON.stringify(body)}`);
  }

  console.log('Success!', body);
})();
```