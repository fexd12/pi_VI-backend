import express from 'express'
import path from 'path'
import autoload from 'express-autoload-routes'

module.exports = function(){
    let app = express.Router()
    let pathBase = path.join(__dirname,'/api')

    autoload(pathBase).then(route=>{
        app.use(route)
    }).catch(err=>{console.log(err)})

    app.get('/',function(req,res){
        res.send('hello world')
    })
    
    require('../middlewares/globals/commons')(app)
    return app;
}