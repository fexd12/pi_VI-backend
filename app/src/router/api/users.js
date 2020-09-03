import express from 'express';
import {usersDAO} from '../dao/usersDAO';
import auth from '../../middlewares/auth'

module.exports = function(){
    const app = express.Router();
    app.use(auth)
    
    app.get('/all',async(req,res)=>{
        let dao = new usersDAO();

        let obj = await dao.readAll();
        res.send(JSON.stringify(obj));
    });

    app.get('/',async (req,res)=>{
        let dao = new usersDAO();

        let obj = await dao.read();
        res.send(JSON.stringify(obj));
    })

    app.get('/userstag',async (req,res)=>{
        let dao = new usersDAO();

        let obj = await dao.readUsersTag();
        res.send(JSON.stringify(obj));
    })

    app.post('/',async(req,res)=>{
        let dao = new usersDAO;
        await dao.readbyid(req.body.name).then(async (a)=>{
            if(a < 1){
                await dao.insertInto(req.body);
            }
        })
        res.send({})
    })

    app.post('/sxadas',async (req,res)=>{
        let dao = new UsuariosDAO();
    
        let hash = bcrypt.hashSync(req.body.senha,8);
        let objUser ={
            usuario:req.body.usuario,
            senha:hash
        }
        await dao.insertInto(objUser);
    
        res.send('usuario criado');
    })


    app.put('/:id',async (req,res)=>{
        let dao = new usersDAO;
        await dao.update(req.body);
        res.send({});
    })

    app.delete('/:id',async (req,res)=>{
        let dao = new usersDAO;
        
        await dao.delete(req.params.id);
        res.send({});
    })

    return app
}