import express from 'express';
import moment from 'moment';
import {agendamentoDAO} from '../dao/agendamentoDAO';
import auth from '../../middlewares/auth'

module.exports = function(){
    const app  = express.Router()
    app.use(auth)

    app.get('/',async (req,res) => {
        let tag = req.query.tag
        let dao = new agendamentoDAO();
    
        let date = moment().utcOffset('-0300');
    
        let result = await dao.read(tag);
    
        if(result == undefined){
            res.status(200).send('tag nao possui agendamento')
        }else{
    
            let hora_atual  = date.format("HH:mm");
            result.horario_final = result.horario_final.trim();
            let horaConferir = moment(result.horario_final,"HH:mm",true);
    
            if(moment(hora_atual,"HH:mm").isSameOrBefore(horaConferir) ){
                let obj={
                    liga:1
                }
                res.send(obj);
            }else{
                let obj={
                    liga:0
                }
                res.send(obj);
            }
        }
    })

    return app;

}()
