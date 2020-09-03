import {criaClient} from './db'

class userstagDAO{
    
    constructor() {
        this.config = { 
            table: 'users_tag',
            sequence: 'users_tag_sequence',
            fields: [
              'id_tag',
              'id_users',
              'acesso'
            ],
            pk: 'id'
        };
    }

    async read(){
        let client  = criaClient();
        await client.connect();
        let _query = `SELECT ut.id,u.name, t.tag, ut.acesso
        FROM users_tag as ut
    INNER JOIN tags as t
        ON t.id = ut.id_tag
    INNER JOIN users as u
        on u.id = ut.id_users`;
        let result = await client.query(_query);
        await client.end();
        return result.rows

    }

    async insertInto(questionario){
        let client = criaClient();
        await client.connect();
        let i=1
        let _query = `insert into ${this.config.table} (${this.config.fields.join(',')}) values ($1,$2,$3)`;
        let values=[
            questionario.tag,
            questionario.name,
            Number(questionario.acesso)
        ];
        await client.query(_query,values);
        await client.end();
        return true
    }

    async readbyid(id){
        let client  = criaClient();
        await client.connect();
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table} WHERE ${this.config.pk} = $1`

        let result = await client.query(_query,[id]);
        client.end();
        return result.rows

    }
}


export{userstagDAO}