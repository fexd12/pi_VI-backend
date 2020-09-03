import jwt, { decode } from 'jsonwebtoken';

module.exports = function(req, res, next) {
    var token = req.headers['x-access-token'];

    if(token) {
        jwt.verify(token,'secret',function(err,decoded){
            if(err) return  res.status(500).send({success: false, message: 'Failed to authenticate token.'});   
            req.usuario = decode.usuario;    
            next();
        });

    }
    else {
        // se não tiver o token, retornar o erro 403
        res.status(403).send({ 
            success: false, 
            message: 'Não há token.' 
        });      
    }
}