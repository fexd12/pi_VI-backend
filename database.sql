--DATABASE : POSTGRESQL

-- Database: pi_v

-- DROP DATABASE pi_v;

CREATE DATABASE pi_v
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: public.tags

-- DROP TABLE public.tags;

CREATE TABLE public.tags
(
    id integer NOT NULL,
    tag text COLLATE pg_catalog."default" NOT NULL,
    state integer,
    created_at date,
    update_at date,
    CONSTRAINT tags_pkey PRIMARY KEY (id)
        INCLUDE(id)
)

TABLESPACE pg_default;

ALTER TABLE public.tags
    OWNER to postgres;


-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
    id integer NOT NULL,
    name character(200) COLLATE pg_catalog."default" NOT NULL,
    created_at date,
    update_at date,
    CONSTRAINT users_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to postgres;

-- Table: public.users_tag

-- DROP TABLE public.users_tag;

CREATE TABLE public.users_tag
(
    id integer NOT NULL,
    id_tag integer,
    id_users integer,
    CONSTRAINT id PRIMARY KEY (id)
        INCLUDE(id),
    CONSTRAINT id_tag FOREIGN KEY (id_tag)
        REFERENCES public.tags (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT id_users FOREIGN KEY (id_users)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.users_tag
    OWNER to postgres;

-- SEQUENCE: public.tag_sequence

-- DROP SEQUENCE public.tag_sequence;

CREATE SEQUENCE public.tag_sequence
    INCREMENT 1
    START 1
    MINVALUE 0
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.tag_sequence
    OWNER TO postgres;

-- SEQUENCE: public.users_sequence

-- DROP SEQUENCE public.users_sequence;

CREATE SEQUENCE public.users_sequence
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.users_sequence
    OWNER TO postgres;

-- SEQUENCE: public.users_tag_sequence

-- DROP SEQUENCE public.users_tag_sequence;

CREATE SEQUENCE public.users_tag_sequence
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.users_tag_sequence
    OWNER TO postgres;

ALTER TABLE public.users_tag
    ADD COLUMN acesso integer;

CREATE SEQUENCE public.sala_sequence
    INCREMENT 1
    START 1;

ALTER SEQUENCE public.sala_sequence
    OWNER TO postgres;

CREATE SEQUENCE public.agendamento_sequence
    INCREMENT 1
    START 1;

ALTER SEQUENCE public.agendamento_sequence
    OWNER TO postgres;

ALTER TABLE public.tags
    ALTER COLUMN id SET DEFAULT nextval('tag_sequence');

ALTER TABLE public.users
    ALTER COLUMN id SET DEFAULT nextval('users_sequence');

ALTER TABLE public.users_tag
    ALTER COLUMN id SET DEFAULT nextval('users_tag_sequence');

CREATE TABLE public.sala
(
    id integer NOT NULL DEFAULT nextval('sala_sequence'),
    nome "char" NOT NULL,
    quantidade integer NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE public.sala
    OWNER to postgres;

CREATE TABLE public.agendamento
(
    id integer NOT NULL DEFAULT nextval('agendamento_sequence'),
    sala_id integer NOT NULL,
    users_id integer NOT NULL,
    data_inicial date NOT NULL,
    data_final date NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (sala_id)
        REFERENCES public.sala (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    FOREIGN KEY (users_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE public.agendamento
    OWNER to postgres;

ALTER TABLE public.agendamento
    ALTER COLUMN data_inicial TYPE timestamp(6) without time zone ;

ALTER TABLE public.agendamento
    ALTER COLUMN data_final TYPE timestamp(6) without time zone ;

ALTER TABLE public.users DROP COLUMN update_at;

ALTER TABLE public.users DROP COLUMN created_at;

ALTER TABLE public.users
    ADD COLUMN email "char" NOT NULL;

ALTER TABLE public.sala
    ALTER COLUMN nome TYPE character(200);

ALTER TABLE public.sala
    ADD COLUMN status character(1) NOT NULL;

ALTER TABLE public.users
    ADD COLUMN status character(1) NOT NULL;

ALTER TABLE public.tags
    ADD COLUMN status character(1) NOT NULL;

ALTER TABLE public.agendamento
    RENAME data_inicial TO data;

ALTER TABLE public.agendamento
    ALTER COLUMN data TYPE timestamp(6) with time zone ;

ALTER TABLE public.agendamento
    RENAME data_final TO data_inicial;

ALTER TABLE public.agendamento
    ALTER COLUMN data_inicial TYPE timestamp(6) with time zone ;

ALTER TABLE public.agendamento
    ADD COLUMN data_final timestamp(6) with time zone;

ALTER TABLE public.agendamento
    RENAME users_id TO users_tags_id;

ALTER TABLE public.agendamento
    ALTER COLUMN data_final SET NOT NULL;

ALTER TABLE public.agendamento
    ADD FOREIGN KEY (users_tags_id)
    REFERENCES public.users_tag (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

