export class QivtoApiError extends Error {
  constructor(message, status, response, headers) {
    super(message); this.name = 'QivtoApiError'; this.status = status; this.response = response; this.headers = headers;
  }
}

export class QivtoClient {
  constructor({baseUrl = 'https://qivto.com/api/v1', fetchImpl = globalThis.fetch} = {}) {
    if (!fetchImpl) throw new Error('A fetch implementation is required.');
    this.baseUrl = baseUrl.replace(/\/$/, ''); this.fetch = fetchImpl;
  }
  tools(language = 'en') { return this.request(`/tools?lang=${language === 'lt' ? 'lt' : 'en'}`); }
  uuid(count = 1) { return this.request('/uuid', {method: 'POST', body: {count: Math.max(1, Math.min(100, count))}}); }
  hash(text, algorithm = 'sha256') { return this.request('/hash', {method: 'POST', body: {text, algorithm}}); }
  formatJson(json) { return this.request('/json-format', {method: 'POST', body: {json}}); }
  status() { return this.request('/status'); }
  async request(path, {method = 'GET', body} = {}) {
    const response = await this.fetch(this.baseUrl + path, {method, headers: {'Accept': 'application/json', 'Content-Type': 'application/json'}, body: body === undefined ? undefined : JSON.stringify(body)});
    const data = await response.json().catch(() => null);
    if (!data) throw new QivtoApiError('QIVTO returned invalid JSON.', response.status, null, response.headers);
    if (!response.ok) throw new QivtoApiError(data.error || 'API request failed.', response.status, data, response.headers);
    return data;
  }
}
