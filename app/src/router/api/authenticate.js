import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';
import { usersDAO } from '../dao/usersDAO';
import express from 'express';

module.exports = function(){
    const app = express.Router();

    app.get('/',async(req,res)=>{
        var token = req.headers['x-access-token'];

        if(token) {
            jwt.verify(token,'secret',function(err,decoded){
                if(err) return  res.status(403).send({success: false, message: 'Failed to authenticate token.'});   
                res.send({
                    success:true,
                    message:'token valido'
                })
            });
    
        }
        else {
            // se não tiver o token, retornar o erro 403
            res.status(403).send({ 
                success: false, 
                message: 'Não há token.' 
            });      
        }
    })

    app.post('/',async (req,res)=>{
        let dao  = new usersDAO();
    
        await dao.readbyid(req.body.usuario).then(result => {
            bcrypt.compare(req.body.senha,result.SENHA,(err,match)=>{
                if(err){
                    res.json({
                        error:true,
                        name:'InvalidCredentialsError'
                    })
                }
                if(match){
                    let token = jwt.sign({usuario:result.usuario},'secret',{expiresIn:Math.floor(Date.now() / 1000) + (60 * 60)});
                    return res.json({
                        success:true,
                        user:req.body.usuario,
                        message:'token criado',
                        bearer:token
                    });
                }else{
                    res.json({
                        error:true,
                        name:'InvalidCredentialsError'
                    })
                }
            });
        }).catch((err)=>{
            res.send(err)
        })
    })

    return app;
}();
