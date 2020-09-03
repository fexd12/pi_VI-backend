import express from 'express';
import {salasDAO} from '../dao/salasDAO';
import auth from '../../middlewares/auth'

module.exports = function(){
    const app = express.Router();
    app.use(auth)

    app.get('/all',async(req,res)=>{
        let dao = new salasDAO();
    
       let obj= await dao.readAll();
        res.status(200).send(JSON.stringify(obj));
        
    });
    
    app.get('/',async (req,res)=>{
        let dao = new salasDAO();
    
        let obj = await dao.read();
        res.status(200).send(JSON.stringify(obj));
    })
    
    app.post('/status',async (req,res)=>{
        let dao = new salasDAO();
        let obj={
            data:req.body.data,
            hora_inicial:req.body.hora_inicio,
            hora_final:req.body.hora_final
        }
        let response = await dao.readStatus(obj);
        res.status(200).send(JSON.stringify(response));
    })
    
    app.post('/',async(req,res)=>{
        let dao = new salasDAO;
        await dao.readbyid(req.body.nome).then(async (a)=>{
            if(a < 1){
                await dao.insertInto(req.body);    
                res.send({});
            }
        })
    })
    
    app.get('/agendamento/:sala_id',async(req,res)=>{
        let dao = new salasDAO;
        let id = req.params.sala_id;
        let result = await dao.readAgendamento(id);
        res.send(result);
    })
    
    return app
}