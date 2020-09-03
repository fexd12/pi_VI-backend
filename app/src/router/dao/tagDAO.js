import {criaClient} from './db'

class tagDAO{
    constructor() {
        this.config = { 
            table: 'tags',
            sequence: 'taq_sequence',
            fields: [
              'id',
              'tag',
              'status'
            ],
            pk: 'id'
          };
    }

    async readAll(){
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table}`;
        const client = criaClient();
        await client.connect();
        let result = await client.query(_query);

        await client.end();

        return result.rowCount
    }

    async readUsersTag(){
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table} where status='s'`;
        const client = criaClient();
        await client.connect();
        let result = await client.query(_query);

        await client.end();

        return result.rows
    }

    async read(){
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table}`;
        const client = criaClient();
        await client.connect();
        let result = await client.query(_query);

        await client.end();

        return result.rows
    }

    async readbyid(tag){
        const client = criaClient();

        await client.connect();
        let _query = `SELECT ${this.config.fields.join(',')} FROM ${this.config.table} WHERE tag = '${tag}'`;
        let result = await client.query(_query);
        await client.end();
        if(result.rowCount > 0){
            return result.rows[0]
        }else{
            return undefined
        }

    }

    async insertInto(tag){
        // let query = `insert into ${this.config.table} (${this.config.fields.join(',')}) values (${this.config.fields.map(q=>'?').join(',')})`;
        
        const client = criaClient();
        await client.connect();
        let _query = `INSERT INTO ${this.config.table} (tag, status) values ('${tag}','s')`;
        // console.log(_query);
        let resut = await client.query(_query);
        await client.end();
        
        return true
    }
    async UpdateTag(id){
        let client = criaClient();
        await client.connect();
        let _query = `UPDATE ${this.config.table} SET status='a' WHERE ${this.config.pk} = $1`;
        let result = await client.query(_query,[id])
        await client.end();
        return result
    }
}

export {tagDAO};