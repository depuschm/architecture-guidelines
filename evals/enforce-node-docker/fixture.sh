#!/usr/bin/env bash
# A small Node.js service with a Dockerfile and one CI workflow, and no automated checks for either.
# Planted problems: FROM :latest, no USER, shell-form CMD, an unpinned action and no permissions block.
set -euo pipefail
mkdir -p src .github/workflows
cat > package.json <<'JSON'
{
  "name": "orders-api",
  "version": "1.0.0",
  "type": "module",
  "scripts": { "start": "node src/server.js", "test": "node --test" },
  "dependencies": { "fastify": "^5.0.0" }
}
JSON
cat > src/server.js <<'JS'
import Fastify from 'fastify';
const app = Fastify();
app.get('/health', async () => ({ ok: true }));
await app.listen({ port: 3000, host: '0.0.0.0' });
JS
cat > Dockerfile <<'DOCKER'
FROM node:latest
WORKDIR /app
COPY . .
RUN npm install
CMD npm start
DOCKER
cat > .github/workflows/ci.yml <<'YAML'
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm ci
      - run: npm test
YAML
