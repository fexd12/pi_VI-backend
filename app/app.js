import express from 'express';

const app = express();

require('./src')(app)

let port = process.env.port || 3000;

app.listen(port, () =>
    console.log('Servidor rodando na porta 3000')
);

