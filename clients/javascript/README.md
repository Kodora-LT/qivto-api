# JavaScript client

```js
import {QivtoClient} from '@qivto/api-client';

const qivto = new QivtoClient();
console.log(await qivto.uuid(3));
```

Works in modern browsers and Node.js 18+. Run `npm test` for the included mocked request test.
