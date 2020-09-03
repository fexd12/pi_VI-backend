import api from './router/node'

module.exports = function(app,server){
    app.use('/api',api())
}