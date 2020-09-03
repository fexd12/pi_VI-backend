import { criaClient } from "./db";

class agendamentoDAO {
  constructor() {
    this.config = {
      table: "agendamento",
      sequence: "agendamento_sequence",
      fields: [
        "id",
        "sala_id",
        "users_tags_id",
        "data",
        "data_inicial",
        "data_final",
      ],
      pk: "id",
    };
  }

  async readAll() {
    let client = criaClient();
    await client.connect();
    let _query = `SELECT ${this.config.fields.join(",")} FROM ${
      this.config.table
    }`;
    let result = await client.query(_query);
    await client.end();
    return result.rowCount;
  }

  async read(tag) {
    let client = criaClient();
    await client.connect();
    let _query = `SELECT u.name as Usuario, ag.data, ag.data_inicial as Horario_Inicial, ag.data_final as Horario_Final, t.tag, ut.acesso,s.nome as Sala
    FROM agendamento as ag
  inner join users_tag as ut
    ON ut.id = ag.users_tags_id
  INNER JOIN tags as t
    ON t.id = ut.id_tag
  INNER JOIN users as u
    on u.id = ut.id_users
  INNER JOIN sala as s
    on s.id = ag.sala_id
     where t.tag = '${tag}'`;
    let result = await client.query(_query);
    await client.end();
    if(result.rowCount<1){
      return undefined
    }else{
      return result.rows[0];
    }
  }

  async readStatus() {
    let client = criaClient();
    await client.connect();
    let _query = `SELECT ${this.config.fields.join(",")} FROM ${
      this.config.table
    } where status = 's'`;
    let result = await client.query(_query);
    await client.end();
    return result.rows;
  }

  async delete(id) {
    let client = criaClient();
    await client.connect();
    let _query = `DELETE FROM ${this.config.table} WHERE ${this.config.pk} = $1`;
    let result = await client.query(_query, [id]);
    return result;
  }

  async update(questionario) {
    let client = criaClient();
    await client.connect();
    let _query = `UPDATE ${this.config.table} SET nome=$1, quantidade=$2 WHERE ${this.config.pk} = $3`;
    let result = await client.query(_query, [
      questionario.nome,
      questionario.quantidade,
      questionario.id,
    ]);
    await client.end();
    return result;
  }

  async readbyid(id) {
    let client = criaClient();
    await client.connect();
    let _query = `SELECT ${this.config.fields.join(",")} FROM ${
      this.config.table
    } WHERE ${this.config.pk} = ${id}`;
    let result = await client.query(_query);
    await client.end();
    return result.rows;
  }

  async insertInto(questionario) {
    // let query = `insert into ${this.config.table} (${this.config.fields.join(',')}) values (${this.config.fields.map(q=>'?').join(',')})`;
    let client = criaClient();
    await client.connect();
    let _query = `INSERT INTO ${this.config.table} (sala_id,users_tags_id,data,data_inicial,data_final) values ($1,$2,$3,$4,$5)`;
    let values = [
      questionario.sala,
      questionario.name,
      questionario.data,
      questionario.horaInicio,
      questionario.horaFinal,
    ];
    await client.query(_query, values);
    await client.end();
    return true;
  }
}

export { agendamentoDAO };
