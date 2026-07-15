import test from 'node:test';
import assert from 'node:assert/strict';
import {QivtoClient} from '../src/index.js';

test('hash sends the expected request', async () => {
  const calls = [];
  const client = new QivtoClient({fetchImpl: async (url, options) => { calls.push({url, options}); return {ok: true, status: 200, headers: new Headers(), json: async () => ({hash: 'abc'})}; }});
  assert.deepEqual(await client.hash('QIVTO'), {hash: 'abc'});
  assert.equal(calls[0].url, 'https://qivto.com/api/v1/hash');
  assert.equal(JSON.parse(calls[0].options.body).text, 'QIVTO');
});
