import cors from 'cors';
import bodyParser from 'body-parser';
import morgan from 'morgan';
import express from 'express';
import path from 'path';

let rfs = require('rotating-file-stream')

module.exports = function(app) {
    // const app = express()

    let accessLogStream = rfs.createStream('access.log',{
        interval:'1d',
        path:path.join(process.cwd(),'logs',)
    })

    app.use(cors());
    app.use(express.json());
    app.use(bodyParser.urlencoded({extended:true}));
    app.use(morgan('combined',{stream:accessLogStream}));
}