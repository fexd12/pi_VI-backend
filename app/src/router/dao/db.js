import {Client} from 'pg';
require('dotenv').config();

function criaClient(){

    return new Client({
        user: process.env.USER,
        host: process.env.HOST,
        database: process.env.DATABASE,
        password: process.env.PASS,
        port:process.env.PORT_HOST,
        ssl:true,
        rejectUnauthorized: true
    });
}

export {
    criaClient
}