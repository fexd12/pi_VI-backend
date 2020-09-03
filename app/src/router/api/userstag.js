import express from 'express';
import {userstagDAO} from '../dao/userstagDAO';
import {usersDAO} from '../dao/usersDAO';
import {tagDAO} from '../dao/tagDAO';
import auth from '../../middlewares/auth'

module.exports = function(){
    const app = express.Router();
    app.use(auth)

    app.get('/',async(req,res)=>{
        let dao = new userstagDAO();
        let obj=await dao.read();
        res.send(JSON.stringify(obj));
    });

    app.post('/',async(req,res)=>{
        let dao = new userstagDAO();
        let users = new usersDAO();
        let tag = new tagDAO();
        req.body.acesso = Number(req.body.acesso);
        await dao.insertInto(req.body).then(async (abc)=>{
            await users.UpdateUser(req.body.name)
            await tag.UpdateTag(req.body.tag)
            res.send({
                message:'vinculado com sucesso'
            })
        }).catch(err=>{
            res.send(err)
        })
        res.send({
            message:'ok'
        });
    })

    return app
}