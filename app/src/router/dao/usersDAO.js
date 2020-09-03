import {criaClient} from './db'

class usersDAO{
    
    constructor() {
        this.config = { 
            table: 'users',
            sequence: 'users_sequence',
            fields: [
              'id',
              'name',
              'email',
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
    
    async delete(id){
        let client = criaClient();
        await client.connect();
        let _query = `DELETE FROM ${this.config.table} WHERE ${this.config.pk} = $1`;
        let result = await client.query(_query,[id])
        return result
    }

    async update(questionario){
        let client = criaClient();
        await client.connect();
        let _query = `UPDATE ${this.config.table} SET name=$1, email=$2 WHERE ${this.config.pk} = $3`;
        let result = await client.query(_query,[questionario.name,questionario.email,questionario.id])
        await client.end();
        return result
    }
    
    async UpdateUser(id){
        let client = criaClient();
        await client.connect();
        let _query = `UPDATE ${this.config.table} SET status='a' WHERE ${this.config.pk} = $1`;
        let result = await client.query(_query,[id])
        await client.end();
        
        return result
    }

    async readbyid(id){
        let client = criaClient();
        await client.connect();
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table} WHERE name = '${id}'`;
        let result = await client.query(_query);
        await client.end();
        return result.rowCount
    }

    async insertInto(questionario){
        // let query = `insert into ${this.config.table} (${this.config.fields.join(',')}) values (${this.config.fields.map(q=>'?').join(',')})`;
        let client = criaClient();
        await client.connect();
        let _query = `INSERT INTO ${this.config.table} (name,email,status) values ($1,$2,'s')`;
        let values = [questionario.name,questionario.email];
        await client.query(_query,values);
        await client.end();
        return true
    }

    async readUsersTag(){
        let client =  criaClient();
        await client.connect();
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table} where status = 's'`;
        let result = await client.query(_query);
        await client.end();
        return result.rows
    }
}

export{usersDAO}