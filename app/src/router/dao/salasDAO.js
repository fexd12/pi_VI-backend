import {criaClient} from './db'

class salasDAO{
    
    constructor() {
        this.config = { 
            table: 'sala',
            sequence: 'sala_sequence',
            fields: [
              'id',
              'nome',
              'quantidade',
              'status'
            ],
            pk: 'id'
          };
    }

    async readAll(){
        let client =  criaClient();
        await client.connect();
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table}`;
        let result = await client.query(_query);
        await client.end();
        return result.rowCount
    }

    async read(){
        let client =  criaClient();
        await client.connect();
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table}`;
        let result = await client.query(_query);
        await client.end();
        return result.rows
    }
    
    async readStatus(questionario){
        let client =  criaClient();
        await client.connect();
        let _query = `select ${this.config.fields.join(',')} from ${this.config.table} t1 where not exists (select * from agendamento t2 where t1.id = t2.sala_id and t2.data = $1 and t2.data_inicial between $2 and $3)`
        let result = await client.query(_query,[questionario.data,questionario.hora_inicial,questionario.hora_final]);
        await client.end();
        return result.rows
    }

    async delete(id){
        let client = criaClient();
        await client.connect();
        let _query = `DELETE FROM ${this.config.table} WHERE ${this.config.pk} = $1`;
        let result = await client.query(_query,[id])
        return result
    }

    async updateStatus(id){
        let client = criaClient();
        await client.connect();
        let _query = `UPDATE ${this.config.table} SET status='a' WHERE ${this.config.pk} = $1`;
        let result = await client.query(_query,[id])
        client.end()
        
        return result
    }

    async readbyid(id){
        let client = criaClient();
        await client.connect();
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table} WHERE nome = '${id}'`;
        let result = await client.query(_query);
        console.log(result);
        await client.end();
        return result.rowCount
    }

    async insertInto(questionario){
        // let query = `insert into ${this.config.table} (${this.config.fields.join(',')}) values (${this.config.fields.map(q=>'?').join(',')})`;
        let client = criaClient();
        await client.connect();
        let _query = `INSERT INTO ${this.config.table} (nome,quantidade,status) values ($1,$2,'s')`;
        let values = [questionario.nome,questionario.quantidade];
        await client.query(_query,values);
        client.end();
        return true
    }

    async readAgendamento(id){
        let client =  criaClient();
        await client.connect();
        let _query = `SELECT ag.id, ag.sala_id, ag.users_tags_id, u.name as Usuario, ag.data, ag.data_inicial as Horario_Inicial, ag.data_final as Horario_Final, t.tag, ut.acesso,s.nome as Sala
        FROM agendamento as ag
      inner join users_tag as ut
        ON ut.id = ag.users_tags_id
      INNER JOIN tags as t
        ON t.id = ut.id_tag
      INNER JOIN users as u
        on u.id = ut.id_users
      INNER JOIN sala as s
        on s.id = ag.sala_id
         where ag.sala_id = '${id}'`
        let result = await client.query(_query,[id]);
        await client.end();
        return result.rows
    }
}

export{salasDAO}