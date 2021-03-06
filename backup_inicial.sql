PGDMP         $            
    x            PI_VI    12.4    12.2 V    `           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            a           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            b           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            c           1262    16426    PI_VI    DATABASE     w   CREATE DATABASE "PI_VI" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF8' LC_CTYPE = 'en_US.UTF8';
    DROP DATABASE "PI_VI";
                postgres    false            d           0    0    SCHEMA public    ACL     �   REVOKE ALL ON SCHEMA public FROM cloudsqladmin;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO cloudsqlsuperuser;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   cloudsqlsuperuser    false    3            �            1259    16434    acesso    TABLE     S   CREATE TABLE public.acesso (
    id_acesso integer NOT NULL,
    descricao text
);
    DROP TABLE public.acesso;
       public         heap    postgres    false            �            1259    16432    acesso_id_acesso_seq    SEQUENCE     �   CREATE SEQUENCE public.acesso_id_acesso_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.acesso_id_acesso_seq;
       public          postgres    false    204            e           0    0    acesso_id_acesso_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.acesso_id_acesso_seq OWNED BY public.acesso.id_acesso;
          public          postgres    false    203            �            1259    16530    agendamento    TABLE     �   CREATE TABLE public.agendamento (
    id_agendamento integer NOT NULL,
    data date,
    horario_inicio time without time zone,
    horario_final time without time zone,
    sala_id integer NOT NULL,
    usuario_id integer NOT NULL,
    uuid text
);
    DROP TABLE public.agendamento;
       public         heap    postgres    false            �            1259    16528    agendamento_id_agendamento_seq    SEQUENCE     �   CREATE SEQUENCE public.agendamento_id_agendamento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.agendamento_id_agendamento_seq;
       public          postgres    false    216            f           0    0    agendamento_id_agendamento_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.agendamento_id_agendamento_seq OWNED BY public.agendamento.id_agendamento;
          public          postgres    false    215            �            1259    16427    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false            �            1259    16548    cadastro_usuario    TABLE     �   CREATE TABLE public.cadastro_usuario (
    id_cadastro integer NOT NULL,
    senha text NOT NULL,
    usuario_id integer NOT NULL
);
 $   DROP TABLE public.cadastro_usuario;
       public         heap    postgres    false            �            1259    16546     cadastro_usuario_id_cadastro_seq    SEQUENCE     �   CREATE SEQUENCE public.cadastro_usuario_id_cadastro_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.cadastro_usuario_id_cadastro_seq;
       public          postgres    false    218            g           0    0     cadastro_usuario_id_cadastro_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.cadastro_usuario_id_cadastro_seq OWNED BY public.cadastro_usuario.id_cadastro;
          public          postgres    false    217            �            1259    16445    funcao    TABLE     S   CREATE TABLE public.funcao (
    id_funcao integer NOT NULL,
    descricao text
);
    DROP TABLE public.funcao;
       public         heap    postgres    false            �            1259    16443    funcao_id_funcao_seq    SEQUENCE     �   CREATE SEQUENCE public.funcao_id_funcao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.funcao_id_funcao_seq;
       public          postgres    false    206            h           0    0    funcao_id_funcao_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.funcao_id_funcao_seq OWNED BY public.funcao.id_funcao;
          public          postgres    false    205            �            1259    16566    sala_status    TABLE     �   CREATE TABLE public.sala_status (
    sala_status_id integer NOT NULL,
    sala_id integer NOT NULL,
    ar text,
    luzes text,
    projetor text,
    limpeza text
);
    DROP TABLE public.sala_status;
       public         heap    postgres    false            �            1259    16564    sala_status_sala_status_id_seq    SEQUENCE     �   CREATE SEQUENCE public.sala_status_sala_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.sala_status_sala_status_id_seq;
       public          postgres    false    220            i           0    0    sala_status_sala_status_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.sala_status_sala_status_id_seq OWNED BY public.sala_status.sala_status_id;
          public          postgres    false    219            �            1259    16456 	   sala_tipo    TABLE     Y   CREATE TABLE public.sala_tipo (
    sala_tipo_id integer NOT NULL,
    descricao text
);
    DROP TABLE public.sala_tipo;
       public         heap    postgres    false            �            1259    16454    sala_tipo_sala_tipo_id_seq    SEQUENCE     �   CREATE SEQUENCE public.sala_tipo_sala_tipo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.sala_tipo_sala_tipo_id_seq;
       public          postgres    false    208            j           0    0    sala_tipo_sala_tipo_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.sala_tipo_sala_tipo_id_seq OWNED BY public.sala_tipo.sala_tipo_id;
          public          postgres    false    207            �            1259    16480    salas    TABLE        CREATE TABLE public.salas (
    id_sala integer NOT NULL,
    numero text,
    quantidade integer,
    sala_tipo_id integer
);
    DROP TABLE public.salas;
       public         heap    postgres    false            �            1259    16478    salas_id_sala_seq    SEQUENCE     �   CREATE SEQUENCE public.salas_id_sala_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.salas_id_sala_seq;
       public          postgres    false    212            k           0    0    salas_id_sala_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.salas_id_sala_seq OWNED BY public.salas.id_sala;
          public          postgres    false    211            �            1259    16467    tag    TABLE     W   CREATE TABLE public.tag (
    id_tag integer NOT NULL,
    tag text,
    ativo text
);
    DROP TABLE public.tag;
       public         heap    postgres    false            �            1259    16465    tag_id_tag_seq    SEQUENCE     �   CREATE SEQUENCE public.tag_id_tag_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.tag_id_tag_seq;
       public          postgres    false    210            l           0    0    tag_id_tag_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.tag_id_tag_seq OWNED BY public.tag.id_tag;
          public          postgres    false    209            �            1259    16498    usuario    TABLE     �   CREATE TABLE public.usuario (
    id_usuario integer NOT NULL,
    nome text NOT NULL,
    email text NOT NULL,
    ativo text,
    funcao_id integer,
    acesso_id integer,
    tag_id integer
);
    DROP TABLE public.usuario;
       public         heap    postgres    false            �            1259    16496    usuario_id_usuario_seq    SEQUENCE     �   CREATE SEQUENCE public.usuario_id_usuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.usuario_id_usuario_seq;
       public          postgres    false    214            m           0    0    usuario_id_usuario_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.usuario_id_usuario_seq OWNED BY public.usuario.id_usuario;
          public          postgres    false    213            �           2604    16437    acesso id_acesso    DEFAULT     t   ALTER TABLE ONLY public.acesso ALTER COLUMN id_acesso SET DEFAULT nextval('public.acesso_id_acesso_seq'::regclass);
 ?   ALTER TABLE public.acesso ALTER COLUMN id_acesso DROP DEFAULT;
       public          postgres    false    203    204    204            �           2604    16533    agendamento id_agendamento    DEFAULT     �   ALTER TABLE ONLY public.agendamento ALTER COLUMN id_agendamento SET DEFAULT nextval('public.agendamento_id_agendamento_seq'::regclass);
 I   ALTER TABLE public.agendamento ALTER COLUMN id_agendamento DROP DEFAULT;
       public          postgres    false    216    215    216            �           2604    16551    cadastro_usuario id_cadastro    DEFAULT     �   ALTER TABLE ONLY public.cadastro_usuario ALTER COLUMN id_cadastro SET DEFAULT nextval('public.cadastro_usuario_id_cadastro_seq'::regclass);
 K   ALTER TABLE public.cadastro_usuario ALTER COLUMN id_cadastro DROP DEFAULT;
       public          postgres    false    218    217    218            �           2604    16448    funcao id_funcao    DEFAULT     t   ALTER TABLE ONLY public.funcao ALTER COLUMN id_funcao SET DEFAULT nextval('public.funcao_id_funcao_seq'::regclass);
 ?   ALTER TABLE public.funcao ALTER COLUMN id_funcao DROP DEFAULT;
       public          postgres    false    206    205    206            �           2604    16569    sala_status sala_status_id    DEFAULT     �   ALTER TABLE ONLY public.sala_status ALTER COLUMN sala_status_id SET DEFAULT nextval('public.sala_status_sala_status_id_seq'::regclass);
 I   ALTER TABLE public.sala_status ALTER COLUMN sala_status_id DROP DEFAULT;
       public          postgres    false    219    220    220            �           2604    16459    sala_tipo sala_tipo_id    DEFAULT     �   ALTER TABLE ONLY public.sala_tipo ALTER COLUMN sala_tipo_id SET DEFAULT nextval('public.sala_tipo_sala_tipo_id_seq'::regclass);
 E   ALTER TABLE public.sala_tipo ALTER COLUMN sala_tipo_id DROP DEFAULT;
       public          postgres    false    207    208    208            �           2604    16483    salas id_sala    DEFAULT     n   ALTER TABLE ONLY public.salas ALTER COLUMN id_sala SET DEFAULT nextval('public.salas_id_sala_seq'::regclass);
 <   ALTER TABLE public.salas ALTER COLUMN id_sala DROP DEFAULT;
       public          postgres    false    211    212    212            �           2604    16470 
   tag id_tag    DEFAULT     h   ALTER TABLE ONLY public.tag ALTER COLUMN id_tag SET DEFAULT nextval('public.tag_id_tag_seq'::regclass);
 9   ALTER TABLE public.tag ALTER COLUMN id_tag DROP DEFAULT;
       public          postgres    false    209    210    210            �           2604    16501    usuario id_usuario    DEFAULT     x   ALTER TABLE ONLY public.usuario ALTER COLUMN id_usuario SET DEFAULT nextval('public.usuario_id_usuario_seq'::regclass);
 A   ALTER TABLE public.usuario ALTER COLUMN id_usuario DROP DEFAULT;
       public          postgres    false    213    214    214            M          0    16434    acesso 
   TABLE DATA           6   COPY public.acesso (id_acesso, descricao) FROM stdin;
    public          postgres    false    204   4c       Y          0    16530    agendamento 
   TABLE DATA           u   COPY public.agendamento (id_agendamento, data, horario_inicio, horario_final, sala_id, usuario_id, uuid) FROM stdin;
    public          postgres    false    216   qc       K          0    16427    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    202   �c       [          0    16548    cadastro_usuario 
   TABLE DATA           J   COPY public.cadastro_usuario (id_cadastro, senha, usuario_id) FROM stdin;
    public          postgres    false    218   �c       O          0    16445    funcao 
   TABLE DATA           6   COPY public.funcao (id_funcao, descricao) FROM stdin;
    public          postgres    false    206   ,d       ]          0    16566    sala_status 
   TABLE DATA           \   COPY public.sala_status (sala_status_id, sala_id, ar, luzes, projetor, limpeza) FROM stdin;
    public          postgres    false    220   xd       Q          0    16456 	   sala_tipo 
   TABLE DATA           <   COPY public.sala_tipo (sala_tipo_id, descricao) FROM stdin;
    public          postgres    false    208   �d       U          0    16480    salas 
   TABLE DATA           J   COPY public.salas (id_sala, numero, quantidade, sala_tipo_id) FROM stdin;
    public          postgres    false    212   e       S          0    16467    tag 
   TABLE DATA           1   COPY public.tag (id_tag, tag, ativo) FROM stdin;
    public          postgres    false    210   <e       W          0    16498    usuario 
   TABLE DATA           _   COPY public.usuario (id_usuario, nome, email, ativo, funcao_id, acesso_id, tag_id) FROM stdin;
    public          postgres    false    214   ce       n           0    0    acesso_id_acesso_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.acesso_id_acesso_seq', 4, true);
          public          postgres    false    203            o           0    0    agendamento_id_agendamento_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.agendamento_id_agendamento_seq', 1, true);
          public          postgres    false    215            p           0    0     cadastro_usuario_id_cadastro_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.cadastro_usuario_id_cadastro_seq', 2, true);
          public          postgres    false    217            q           0    0    funcao_id_funcao_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.funcao_id_funcao_seq', 5, true);
          public          postgres    false    205            r           0    0    sala_status_sala_status_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.sala_status_sala_status_id_seq', 1, true);
          public          postgres    false    219            s           0    0    sala_tipo_sala_tipo_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.sala_tipo_sala_tipo_id_seq', 8, true);
          public          postgres    false    207            t           0    0    salas_id_sala_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.salas_id_sala_seq', 1, true);
          public          postgres    false    211            u           0    0    tag_id_tag_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.tag_id_tag_seq', 2, true);
          public          postgres    false    209            v           0    0    usuario_id_usuario_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.usuario_id_usuario_seq', 2, true);
          public          postgres    false    213            �           2606    16442    acesso acesso_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.acesso
    ADD CONSTRAINT acesso_pkey PRIMARY KEY (id_acesso);
 <   ALTER TABLE ONLY public.acesso DROP CONSTRAINT acesso_pkey;
       public            postgres    false    204            �           2606    16535    agendamento agendamento_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_pkey PRIMARY KEY (id_agendamento);
 F   ALTER TABLE ONLY public.agendamento DROP CONSTRAINT agendamento_pkey;
       public            postgres    false    216            �           2606    16431 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    202            �           2606    16556 &   cadastro_usuario cadastro_usuario_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.cadastro_usuario
    ADD CONSTRAINT cadastro_usuario_pkey PRIMARY KEY (id_cadastro);
 P   ALTER TABLE ONLY public.cadastro_usuario DROP CONSTRAINT cadastro_usuario_pkey;
       public            postgres    false    218            �           2606    16558 0   cadastro_usuario cadastro_usuario_usuario_id_key 
   CONSTRAINT     q   ALTER TABLE ONLY public.cadastro_usuario
    ADD CONSTRAINT cadastro_usuario_usuario_id_key UNIQUE (usuario_id);
 Z   ALTER TABLE ONLY public.cadastro_usuario DROP CONSTRAINT cadastro_usuario_usuario_id_key;
       public            postgres    false    218            �           2606    16453    funcao funcao_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.funcao
    ADD CONSTRAINT funcao_pkey PRIMARY KEY (id_funcao);
 <   ALTER TABLE ONLY public.funcao DROP CONSTRAINT funcao_pkey;
       public            postgres    false    206            �           2606    16574    sala_status sala_status_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.sala_status
    ADD CONSTRAINT sala_status_pkey PRIMARY KEY (sala_status_id);
 F   ALTER TABLE ONLY public.sala_status DROP CONSTRAINT sala_status_pkey;
       public            postgres    false    220            �           2606    16576 #   sala_status sala_status_sala_id_key 
   CONSTRAINT     a   ALTER TABLE ONLY public.sala_status
    ADD CONSTRAINT sala_status_sala_id_key UNIQUE (sala_id);
 M   ALTER TABLE ONLY public.sala_status DROP CONSTRAINT sala_status_sala_id_key;
       public            postgres    false    220            �           2606    16464    sala_tipo sala_tipo_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.sala_tipo
    ADD CONSTRAINT sala_tipo_pkey PRIMARY KEY (sala_tipo_id);
 B   ALTER TABLE ONLY public.sala_tipo DROP CONSTRAINT sala_tipo_pkey;
       public            postgres    false    208            �           2606    16490    salas salas_numero_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.salas
    ADD CONSTRAINT salas_numero_key UNIQUE (numero);
 @   ALTER TABLE ONLY public.salas DROP CONSTRAINT salas_numero_key;
       public            postgres    false    212            �           2606    16488    salas salas_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.salas
    ADD CONSTRAINT salas_pkey PRIMARY KEY (id_sala);
 :   ALTER TABLE ONLY public.salas DROP CONSTRAINT salas_pkey;
       public            postgres    false    212            �           2606    16475    tag tag_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (id_tag);
 6   ALTER TABLE ONLY public.tag DROP CONSTRAINT tag_pkey;
       public            postgres    false    210            �           2606    16477    tag tag_tag_key 
   CONSTRAINT     I   ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_tag_key UNIQUE (tag);
 9   ALTER TABLE ONLY public.tag DROP CONSTRAINT tag_tag_key;
       public            postgres    false    210            �           2606    16508    usuario usuario_email_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_email_key UNIQUE (email);
 C   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_email_key;
       public            postgres    false    214            �           2606    16510    usuario usuario_nome_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_nome_key UNIQUE (nome);
 B   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_nome_key;
       public            postgres    false    214            �           2606    16506    usuario usuario_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    214            �           2606    16512    usuario usuario_tag_id_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_tag_id_key UNIQUE (tag_id);
 D   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_tag_id_key;
       public            postgres    false    214            �           2606    16536 $   agendamento agendamento_sala_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_sala_id_fkey FOREIGN KEY (sala_id) REFERENCES public.salas(id_sala);
 N   ALTER TABLE ONLY public.agendamento DROP CONSTRAINT agendamento_sala_id_fkey;
       public          postgres    false    3506    212    216            �           2606    16541 '   agendamento agendamento_usuario_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuario(id_usuario);
 Q   ALTER TABLE ONLY public.agendamento DROP CONSTRAINT agendamento_usuario_id_fkey;
       public          postgres    false    3512    214    216            �           2606    16559 1   cadastro_usuario cadastro_usuario_usuario_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cadastro_usuario
    ADD CONSTRAINT cadastro_usuario_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuario(id_usuario);
 [   ALTER TABLE ONLY public.cadastro_usuario DROP CONSTRAINT cadastro_usuario_usuario_id_fkey;
       public          postgres    false    214    218    3512            �           2606    16577 $   sala_status sala_status_sala_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sala_status
    ADD CONSTRAINT sala_status_sala_id_fkey FOREIGN KEY (sala_id) REFERENCES public.salas(id_sala);
 N   ALTER TABLE ONLY public.sala_status DROP CONSTRAINT sala_status_sala_id_fkey;
       public          postgres    false    3506    220    212            �           2606    16491    salas salas_sala_tipo_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.salas
    ADD CONSTRAINT salas_sala_tipo_id_fkey FOREIGN KEY (sala_tipo_id) REFERENCES public.sala_tipo(sala_tipo_id);
 G   ALTER TABLE ONLY public.salas DROP CONSTRAINT salas_sala_tipo_id_fkey;
       public          postgres    false    212    208    3498            �           2606    16513    usuario usuario_acesso_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_acesso_id_fkey FOREIGN KEY (acesso_id) REFERENCES public.acesso(id_acesso);
 H   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_acesso_id_fkey;
       public          postgres    false    214    204    3494            �           2606    16518    usuario usuario_funcao_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_funcao_id_fkey FOREIGN KEY (funcao_id) REFERENCES public.funcao(id_funcao);
 H   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_funcao_id_fkey;
       public          postgres    false    214    3496    206            �           2606    16523    usuario usuario_tag_id_fkey    FK CONSTRAINT     {   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES public.tag(id_tag);
 E   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_tag_id_fkey;
       public          postgres    false    3500    210    214            M   -   x�3�t+���2�J-.)�,��2�tL����rS�b���� �r�      Y      x������ � �      K      x�K�H17156HJ3J����� ,�      [   d   x��1�0й9Gg���V~w$fXY�HL����gN�>���L����,+��8�ާ�ʘM�O�O5��FGݽ�죂I��~*�� ��<      O   <   x�3����-H�J�2�tL����,.)JL�/�2�IM��L��2�(�OK-.���qqq ̒j      ]      x������ � �      Q   z   x�3��IL�/J,9��(3_!%U�9?���$1%�(���C�%3=�$1�˘381'Q!9?W!�(?+�$��˄ӵ����J�����\.S���\.3LCS�3����1d@zW�d&'*p��qqq +�?	      U      x������ � �      S      x�3�tL��������� �2      W   /   x�3�tL����,.)JL�/�L���^r~.g0�	�1�!W� [�     