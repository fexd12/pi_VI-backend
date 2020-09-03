import express from 'express';
import {tagDAO} from  '../dao/tagDAO';
import auth from '../../middlewares/auth'

module.exports = function(){
    const app = express.Router();
    app.use(auth)

    app.post('/',async (req,res)=>{
    
        let tag = req.body.tag;
        // console.log(tag);
        let dao = new tagDAO();
        
        await dao.readbyid(tag).then(async (result)=>{
            if(result === undefined){
                await dao.insertInto(tag);
                res.send('tag cadastrada com sucesso');
            }
            else{
                res.send('tag ja Cadastrada');
            }
        }).catch((a)=>{
            res.send(a);
        })
        
    });
    
    app.get('/all',async(req,res)=>{
        let dao = new tagDAO();
    
        let obj = await dao.readAll()
        res.status(200).send(JSON.stringify(obj));
        
    });
    
    app.get('/', async (req, res) => {
        let dao = new tagDAO();
    
        let obj = await dao.read();
        res.status(200).send(JSON.stringify(obj));
        
    });
    
    app.get('/userstag', async (req, res) => {
        let dao = new tagDAO();
    
        let obj = await dao.readUsersTag();
        res.status(200).send(JSON.stringify(obj));
        
    });

    return app
}