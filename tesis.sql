--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.1
-- Dumped by pg_dump version 9.6.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO admin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO admin;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO admin;

--
-- Name: medical_categoriapregunta; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_categoriapregunta (
    id integer NOT NULL,
    texto character varying(50) NOT NULL
);


ALTER TABLE medical_categoriapregunta OWNER TO admin;

--
-- Name: medical_categoriapregunta_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_categoriapregunta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_categoriapregunta_id_seq OWNER TO admin;

--
-- Name: medical_categoriapregunta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_categoriapregunta_id_seq OWNED BY medical_categoriapregunta.id;


--
-- Name: medical_examen; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_examen (
    id integer NOT NULL,
    fecha date NOT NULL,
    paciente_id integer,
    resultado integer NOT NULL,
    tipo_id integer
);


ALTER TABLE medical_examen OWNER TO admin;

--
-- Name: medical_examen_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_examen_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_examen_id_seq OWNER TO admin;

--
-- Name: medical_examen_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_examen_id_seq OWNED BY medical_examen.id;


--
-- Name: medical_examen_respuestas; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_examen_respuestas (
    id integer NOT NULL,
    examen_id integer NOT NULL,
    respuesta_id integer NOT NULL
);


ALTER TABLE medical_examen_respuestas OWNER TO admin;

--
-- Name: medical_examen_respuestas_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_examen_respuestas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_examen_respuestas_id_seq OWNER TO admin;

--
-- Name: medical_examen_respuestas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_examen_respuestas_id_seq OWNED BY medical_examen_respuestas.id;


--
-- Name: medical_observaciones; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_observaciones (
    id integer NOT NULL,
    observacion text,
    categoria_id integer NOT NULL
);


ALTER TABLE medical_observaciones OWNER TO admin;

--
-- Name: medical_observaciones_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_observaciones_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_observaciones_id_seq OWNER TO admin;

--
-- Name: medical_observaciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_observaciones_id_seq OWNED BY medical_observaciones.id;


--
-- Name: medical_opcionpregunta; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_opcionpregunta (
    id integer NOT NULL,
    texto character varying(50) NOT NULL,
    valor integer NOT NULL
);


ALTER TABLE medical_opcionpregunta OWNER TO admin;

--
-- Name: medical_opcionpregunta_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_opcionpregunta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_opcionpregunta_id_seq OWNER TO admin;

--
-- Name: medical_opcionpregunta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_opcionpregunta_id_seq OWNED BY medical_opcionpregunta.id;


--
-- Name: medical_pregunta; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_pregunta (
    id integer NOT NULL,
    texto text NOT NULL,
    categoria_id integer
);


ALTER TABLE medical_pregunta OWNER TO admin;

--
-- Name: medical_pregunta_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_pregunta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_pregunta_id_seq OWNER TO admin;

--
-- Name: medical_pregunta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_pregunta_id_seq OWNED BY medical_pregunta.id;


--
-- Name: medical_pregunta_opciones; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_pregunta_opciones (
    id integer NOT NULL,
    pregunta_id integer NOT NULL,
    opcionpregunta_id integer NOT NULL
);


ALTER TABLE medical_pregunta_opciones OWNER TO admin;

--
-- Name: medical_pregunta_opciones_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_pregunta_opciones_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_pregunta_opciones_id_seq OWNER TO admin;

--
-- Name: medical_pregunta_opciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_pregunta_opciones_id_seq OWNED BY medical_pregunta_opciones.id;


--
-- Name: medical_puntajecategoria; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_puntajecategoria (
    id integer NOT NULL,
    categoria integer NOT NULL,
    nombre character varying(50) NOT NULL,
    minmala integer NOT NULL,
    maxmala integer NOT NULL,
    minbuena integer NOT NULL,
    maxbuena integer NOT NULL
);


ALTER TABLE medical_puntajecategoria OWNER TO admin;

--
-- Name: medical_puntajecategoria_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_puntajecategoria_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_puntajecategoria_id_seq OWNER TO admin;

--
-- Name: medical_puntajecategoria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_puntajecategoria_id_seq OWNED BY medical_puntajecategoria.id;


--
-- Name: medical_respuesta; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_respuesta (
    id integer NOT NULL,
    valor double precision,
    pregunta_id integer NOT NULL
);


ALTER TABLE medical_respuesta OWNER TO admin;

--
-- Name: medical_respuesta_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_respuesta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_respuesta_id_seq OWNER TO admin;

--
-- Name: medical_respuesta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_respuesta_id_seq OWNED BY medical_respuesta.id;


--
-- Name: medical_tipoexamen; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_tipoexamen (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL
);


ALTER TABLE medical_tipoexamen OWNER TO admin;

--
-- Name: medical_tipoexamen_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_tipoexamen_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_tipoexamen_id_seq OWNER TO admin;

--
-- Name: medical_tipoexamen_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_tipoexamen_id_seq OWNED BY medical_tipoexamen.id;


--
-- Name: medical_tipoexamen_preguntas; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE medical_tipoexamen_preguntas (
    id integer NOT NULL,
    tipoexamen_id integer NOT NULL,
    pregunta_id integer NOT NULL
);


ALTER TABLE medical_tipoexamen_preguntas OWNER TO admin;

--
-- Name: medical_tipoexamen_preguntas_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE medical_tipoexamen_preguntas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE medical_tipoexamen_preguntas_id_seq OWNER TO admin;

--
-- Name: medical_tipoexamen_preguntas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE medical_tipoexamen_preguntas_id_seq OWNED BY medical_tipoexamen_preguntas.id;


--
-- Name: profiling_facultad; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE profiling_facultad (
    id integer NOT NULL,
    nombre text NOT NULL
);


ALTER TABLE profiling_facultad OWNER TO admin;

--
-- Name: profiling_facultad_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE profiling_facultad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE profiling_facultad_id_seq OWNER TO admin;

--
-- Name: profiling_facultad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE profiling_facultad_id_seq OWNED BY profiling_facultad.id;


--
-- Name: profiling_habitsantecedents; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE profiling_habitsantecedents (
    id integer NOT NULL,
    tabaquismo boolean NOT NULL,
    diabetes boolean NOT NULL,
    hipertension boolean NOT NULL,
    iam boolean NOT NULL,
    seguimiento integer NOT NULL,
    fecha date NOT NULL,
    paciente_id integer NOT NULL
);


ALTER TABLE profiling_habitsantecedents OWNER TO admin;

--
-- Name: profiling_habitsantecedents_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE profiling_habitsantecedents_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE profiling_habitsantecedents_id_seq OWNER TO admin;

--
-- Name: profiling_habitsantecedents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE profiling_habitsantecedents_id_seq OWNED BY profiling_habitsantecedents.id;


--
-- Name: profiling_paciente; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE profiling_paciente (
    id integer NOT NULL,
    cod_paciente character varying(50) NOT NULL,
    fecha_nacimiento date NOT NULL,
    genero character varying(1) NOT NULL,
    telefono character varying(30) NOT NULL,
    estado_civil character varying(35) NOT NULL,
    estrato character varying(1) NOT NULL,
    facultad_id integer,
    regimen_salud_id integer,
    nombre character varying(50) NOT NULL,
    primer_apellido character varying(50) NOT NULL,
    segundo_apellido character varying(50) NOT NULL,
    fecha_creacion date NOT NULL
);


ALTER TABLE profiling_paciente OWNER TO admin;

--
-- Name: profiling_paciente_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE profiling_paciente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE profiling_paciente_id_seq OWNER TO admin;

--
-- Name: profiling_paciente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE profiling_paciente_id_seq OWNED BY profiling_paciente.id;


--
-- Name: profiling_regimensalud; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE profiling_regimensalud (
    id integer NOT NULL,
    nombre text NOT NULL
);


ALTER TABLE profiling_regimensalud OWNER TO admin;

--
-- Name: profiling_regimensalud_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE profiling_regimensalud_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE profiling_regimensalud_id_seq OWNER TO admin;

--
-- Name: profiling_regimensalud_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE profiling_regimensalud_id_seq OWNED BY profiling_regimensalud.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: medical_categoriapregunta id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_categoriapregunta ALTER COLUMN id SET DEFAULT nextval('medical_categoriapregunta_id_seq'::regclass);


--
-- Name: medical_examen id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_examen ALTER COLUMN id SET DEFAULT nextval('medical_examen_id_seq'::regclass);


--
-- Name: medical_examen_respuestas id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_examen_respuestas ALTER COLUMN id SET DEFAULT nextval('medical_examen_respuestas_id_seq'::regclass);


--
-- Name: medical_observaciones id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_observaciones ALTER COLUMN id SET DEFAULT nextval('medical_observaciones_id_seq'::regclass);


--
-- Name: medical_opcionpregunta id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_opcionpregunta ALTER COLUMN id SET DEFAULT nextval('medical_opcionpregunta_id_seq'::regclass);


--
-- Name: medical_pregunta id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_pregunta ALTER COLUMN id SET DEFAULT nextval('medical_pregunta_id_seq'::regclass);


--
-- Name: medical_pregunta_opciones id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_pregunta_opciones ALTER COLUMN id SET DEFAULT nextval('medical_pregunta_opciones_id_seq'::regclass);


--
-- Name: medical_puntajecategoria id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_puntajecategoria ALTER COLUMN id SET DEFAULT nextval('medical_puntajecategoria_id_seq'::regclass);


--
-- Name: medical_respuesta id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_respuesta ALTER COLUMN id SET DEFAULT nextval('medical_respuesta_id_seq'::regclass);


--
-- Name: medical_tipoexamen id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_tipoexamen ALTER COLUMN id SET DEFAULT nextval('medical_tipoexamen_id_seq'::regclass);


--
-- Name: medical_tipoexamen_preguntas id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_tipoexamen_preguntas ALTER COLUMN id SET DEFAULT nextval('medical_tipoexamen_preguntas_id_seq'::regclass);


--
-- Name: profiling_facultad id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_facultad ALTER COLUMN id SET DEFAULT nextval('profiling_facultad_id_seq'::regclass);


--
-- Name: profiling_habitsantecedents id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_habitsantecedents ALTER COLUMN id SET DEFAULT nextval('profiling_habitsantecedents_id_seq'::regclass);


--
-- Name: profiling_paciente id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_paciente ALTER COLUMN id SET DEFAULT nextval('profiling_paciente_id_seq'::regclass);


--
-- Name: profiling_regimensalud id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_regimensalud ALTER COLUMN id SET DEFAULT nextval('profiling_regimensalud_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add permission	3	add_permission
8	Can change permission	3	change_permission
9	Can delete permission	3	delete_permission
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add regimen salud	7	add_regimensalud
20	Can change regimen salud	7	change_regimensalud
21	Can delete regimen salud	7	delete_regimensalud
22	Can add habits antecedents	8	add_habitsantecedents
23	Can change habits antecedents	8	change_habitsantecedents
24	Can delete habits antecedents	8	delete_habitsantecedents
25	Can add facultad	9	add_facultad
26	Can change facultad	9	change_facultad
27	Can delete facultad	9	delete_facultad
28	Can add paciente	10	add_paciente
29	Can change paciente	10	change_paciente
30	Can delete paciente	10	delete_paciente
31	Can add opcion pregunta	11	add_opcionpregunta
32	Can change opcion pregunta	11	change_opcionpregunta
33	Can delete opcion pregunta	11	delete_opcionpregunta
34	Can add observaciones	12	add_observaciones
35	Can change observaciones	12	change_observaciones
36	Can delete observaciones	12	delete_observaciones
37	Can add examen	13	add_examen
38	Can change examen	13	change_examen
39	Can delete examen	13	delete_examen
40	Can add puntaje categoria	14	add_puntajecategoria
41	Can change puntaje categoria	14	change_puntajecategoria
42	Can delete puntaje categoria	14	delete_puntajecategoria
43	Can add pregunta	15	add_pregunta
44	Can change pregunta	15	change_pregunta
45	Can delete pregunta	15	delete_pregunta
46	Can add tipo examen	16	add_tipoexamen
47	Can change tipo examen	16	change_tipoexamen
48	Can delete tipo examen	16	delete_tipoexamen
49	Can add respuesta	17	add_respuesta
50	Can change respuesta	17	change_respuesta
51	Can delete respuesta	17	delete_respuesta
52	Can add categoria pregunta	18	add_categoriapregunta
53	Can change categoria pregunta	18	change_categoriapregunta
54	Can delete categoria pregunta	18	delete_categoriapregunta
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('auth_permission_id_seq', 54, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$36000$kYTTQZv8udlM$FCM27Z7r6rRy4PqgTjGbhyBpFRY1ZPiYUFCONskcIYg=	2017-09-23 15:10:50.63333-05	t	admin			admin@gmail.com	t	t	2017-09-23 15:10:30.636309-05
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2017-09-23 15:11:52.6474-05	1	Nunca	1	[{"added": {}}]	11	1
2	2017-09-23 15:12:11.652518-05	2	Casi Nunca	1	[{"added": {}}]	11	1
3	2017-09-23 15:13:33.283629-05	3	Casi Siempre	1	[{"added": {}}]	11	1
4	2017-09-23 15:13:41.801283-05	4	Siempre	1	[{"added": {}}]	11	1
5	2017-09-23 15:15:57.461213-05	1	P1	1	[{"added": {}}]	15	1
6	2017-09-23 15:16:03.57168-05	2	P2	1	[{"added": {}}]	15	1
7	2017-09-23 15:16:08.664062-05	3	P3	1	[{"added": {}}]	15	1
8	2017-09-23 15:16:13.389883-05	4	P4	1	[{"added": {}}]	15	1
9	2017-09-23 15:16:18.346338-05	5	P4	1	[{"added": {}}]	15	1
10	2017-09-23 15:16:22.720253-05	6	P5	1	[{"added": {}}]	15	1
11	2017-09-23 15:16:30.271957-05	7	P6	1	[{"added": {}}]	15	1
12	2017-09-23 15:16:35.975476-05	8	P7	1	[{"added": {}}]	15	1
13	2017-09-23 15:16:40.579075-05	9	P8	1	[{"added": {}}]	15	1
14	2017-09-23 15:16:46.373654-05	10	P9	1	[{"added": {}}]	15	1
15	2017-09-23 15:16:50.74127-05	11	P10	1	[{"added": {}}]	15	1
16	2017-09-23 15:16:55.613007-05	12	P11	1	[{"added": {}}]	15	1
17	2017-09-23 15:17:00.050932-05	13	P12	1	[{"added": {}}]	15	1
18	2017-09-23 15:17:04.565958-05	14	P13	1	[{"added": {}}]	15	1
19	2017-09-23 15:17:08.822155-05	15	P14	1	[{"added": {}}]	15	1
20	2017-09-23 15:17:16.162068-05	16	P15	1	[{"added": {}}]	15	1
21	2017-09-23 15:17:20.389975-05	17	P16	1	[{"added": {}}]	15	1
22	2017-09-23 15:17:25.187812-05	18	P17	1	[{"added": {}}]	15	1
23	2017-09-23 15:17:29.80423-05	19	P18	1	[{"added": {}}]	15	1
24	2017-09-23 15:17:35.172373-05	20	P19	1	[{"added": {}}]	15	1
25	2017-09-23 15:17:39.643256-05	21	P20	1	[{"added": {}}]	15	1
26	2017-09-23 15:17:44.364647-05	22	P21	1	[{"added": {}}]	15	1
27	2017-09-23 15:17:49.025702-05	23	P22	1	[{"added": {}}]	15	1
28	2017-09-23 15:17:54.517467-05	24	P23	1	[{"added": {}}]	15	1
29	2017-09-23 15:18:00.529635-05	25	P24	1	[{"added": {}}]	15	1
30	2017-09-23 15:18:15.702349-05	1	Test Asa	1	[{"added": {}}]	16	1
31	2017-09-23 17:23:49.880143-05	4	P4	3		15	1
32	2017-09-23 19:16:10.071947-05	1	Categoría 1	1	[{"added": {}}]	18	1
33	2017-09-23 19:16:13.721955-05	2	Categoría 2	1	[{"added": {}}]	18	1
34	2017-09-23 19:16:16.001307-05	3	Categoría 3	1	[{"added": {}}]	18	1
35	2017-09-23 19:16:18.72722-05	4	Categoría 4	1	[{"added": {}}]	18	1
36	2017-09-23 19:16:21.877247-05	5	Categoría 5	1	[{"added": {}}]	18	1
37	2017-09-23 19:18:30.008349-05	13	Cuando Necesito ayuda puedo recurrir a mis amigos.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
38	2017-09-23 19:19:34.03144-05	23	Si yo no puedo cuidarme puedo buscar ayuda.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
39	2017-09-23 19:20:50.340886-05	2	Reviso si las Formas que Practico habitualmente para mantener con salud, son buenas.	2	[{"changed": {"fields": ["texto"]}}]	15	1
40	2017-09-23 19:21:17.604083-05	5	Yo puedo hacer lo necesario para mantener limpio el ambiente en el que vivo.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
41	2017-09-23 19:21:24.831227-05	2	Reviso si las Formas que Practico habitualmente para mantener con salud, son buenas.	2	[{"changed": {"fields": ["categoria"]}}]	15	1
42	2017-09-23 19:21:29.283655-05	5	Yo puedo hacer lo necesario para mantener limpio el ambiente en el que vivo.	2	[]	15	1
43	2017-09-23 19:22:48.208588-05	6	Hago en primer lugar lo que sea necesario para mantenerme con Salud.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
44	2017-09-23 19:23:13.272635-05	8	Yo puedo buscar mejores formas para cuidar de mi salud que las que tengo ahora.	2	[{"changed": {"fields": ["texto"]}}]	15	1
45	2017-09-23 19:23:19.028046-05	9	Cambio la frecuencia en que me baño para mantenerme limpio.	2	[{"changed": {"fields": ["texto"]}}]	15	1
46	2017-09-23 19:23:27.384437-05	8	Yo puedo buscar mejores formas para cuidar de mi salud que las que tengo ahora.	2	[{"changed": {"fields": ["categoria"]}}]	15	1
47	2017-09-23 19:23:33.615478-05	9	Cambio la frecuencia en que me baño para mantenerme limpio.	2	[{"changed": {"fields": ["categoria"]}}]	15	1
48	2017-09-23 19:24:07.022495-05	15	Cuando obtengo información sobre mi salud pido explicaciones sobre lo que no entiendo.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
49	2017-09-23 19:24:22.774417-05	16	Yo examino mi cuerpo para ver si hay algun cambio.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
50	2017-09-23 19:24:34.095875-05	16	Yo examino mi cuerpo para ver si hay algún cambio.	2	[{"changed": {"fields": ["texto"]}}]	15	1
51	2017-09-23 19:24:46.874055-05	17	He sido capaz de cambiar hábitos que tenia muy arraigados con tal de mejorar mi salud.	2	[{"changed": {"fields": ["texto"]}}]	15	1
52	2017-09-23 19:25:01.427937-05	17	He sido capaz de cambiar hábitos que tenia muy arraigados con tal de mejorar mi salud.	2	[{"changed": {"fields": ["categoria"]}}]	15	1
53	2017-09-23 19:25:09.187483-05	16	Yo examino mi cuerpo para ver si hay algún cambio.	2	[]	15	1
54	2017-09-23 19:25:16.192709-05	17	He sido capaz de cambiar hábitos que tenia muy arraigados con tal de mejorar mi salud.	2	[]	15	1
55	2017-09-23 19:25:52.210891-05	18	Cuando tengo que tomar una nueva medicina cuento con una persona que me brinde información sobre los efectos secundarios.	2	[{"changed": {"fields": ["texto"]}}]	15	1
56	2017-09-23 19:26:09.385848-05	20	Soy capaz de evaluar que tanto me sirve lo que hago para mantenerme con salud	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
57	2017-09-23 19:26:26.474981-05	20	Soy capaz de evaluar que tanto me sirve lo que hago para mantenerme con salud	2	[]	15	1
58	2017-09-23 19:26:45.898165-05	22	Si mi salud se ve afectada yo puedo conseguir la información necesaria sobre que hacer.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
59	2017-09-23 19:27:04.702916-05	24	Puedo sacar tiempo para mi.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
60	2017-09-23 19:27:55.83829-05	1	A medida que cambian las circustancias yo voy haciendo ajustes para mantener mi salud.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
61	2017-09-23 19:28:03.704418-05	1	A medida que cambian las circunstancias yo voy haciendo ajustes para mantener mi salud.	2	[{"changed": {"fields": ["texto"]}}]	15	1
62	2017-09-23 19:28:13.167372-05	1	A medida que cambian las circunstancias yo voy haciendo ajustes para mantener mi salud.	2	[]	15	1
63	2017-09-23 19:28:29.780323-05	11	Cuando hay situaciones que me afectan yo las manejo de manera que pueda mantener mi forma de ser.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
64	2017-09-23 19:28:54.704767-05	19	Soy capaz de tomar medidas para garantizar que mi familia y yo no corramos peligro.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
65	2017-09-23 19:29:07.210945-05	25	Si presento limitaciones para movilizarme soy capaz de cuidarme como a mi me gusta.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
66	2017-09-23 19:46:41.642278-05	3	Si tengo problemas para moverme o desplazarme me las arreglo para conseguir ayuda.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
67	2017-09-23 19:47:01.771149-05	7	Me faltan las fuerzas necesarias para cuidarme como debo.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
68	2017-09-23 19:47:22.971243-05	7	Me faltan las fuerzas necesarias para cuidarme como debo.	2	[]	15	1
69	2017-09-23 19:47:32.452471-05	12	Pienso en hacer ejercicio y descansar un poco durante el día pero no llego hacerlo.	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
70	2017-09-23 19:47:47.200422-05	14	Pudo dormir lo suficiente  para sentirme descansado (a)	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
71	2017-09-23 19:48:19.739161-05	21	Debido a mis ocupaciones diarias me resulta dificil sacar tiempo para cuidarme	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
72	2017-09-23 19:48:39.355171-05	21	Debido a mis ocupaciones diarias me resulta difícil sacar tiempo para cuidarme.	2	[{"changed": {"fields": ["texto"]}}]	15	1
73	2017-09-23 19:48:53.231961-05	10	Para mantener el peso que me corresponde hago cambios en mis hábitos alimenticios	2	[{"changed": {"fields": ["texto", "categoria"]}}]	15	1
74	2017-09-23 21:47:58.74988-05	1	Prepagada	1	[{"added": {}}]	7	1
75	2017-09-23 21:48:15.194095-05	1	Ingeniería de sistemas de información	1	[{"added": {}}]	9	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 75, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	group
3	auth	permission
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	profiling	regimensalud
8	profiling	habitsantecedents
9	profiling	facultad
10	profiling	paciente
11	medical	opcionpregunta
12	medical	observaciones
13	medical	examen
14	medical	puntajecategoria
15	medical	pregunta
16	medical	tipoexamen
17	medical	respuesta
18	medical	categoriapregunta
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('django_content_type_id_seq', 18, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2017-09-23 15:08:39.325508-05
2	auth	0001_initial	2017-09-23 15:08:39.405116-05
3	admin	0001_initial	2017-09-23 15:08:39.463644-05
4	admin	0002_logentry_remove_auto_add	2017-09-23 15:08:39.481414-05
5	contenttypes	0002_remove_content_type_name	2017-09-23 15:08:39.517809-05
6	auth	0002_alter_permission_name_max_length	2017-09-23 15:08:39.526599-05
7	auth	0003_alter_user_email_max_length	2017-09-23 15:08:39.540027-05
8	auth	0004_alter_user_username_opts	2017-09-23 15:08:39.559391-05
9	auth	0005_alter_user_last_login_null	2017-09-23 15:08:39.579299-05
10	auth	0006_require_contenttypes_0002	2017-09-23 15:08:39.581569-05
11	auth	0007_alter_validators_add_error_messages	2017-09-23 15:08:39.594187-05
12	auth	0008_alter_user_username_max_length	2017-09-23 15:08:39.609879-05
13	profiling	0001_initial	2017-09-23 15:08:39.646106-05
14	profiling	0002_auto_20170912_0450	2017-09-23 15:08:39.680426-05
15	profiling	0003_habitsantecedents	2017-09-23 15:08:39.700048-05
16	medical	0001_initial	2017-09-23 15:08:39.780716-05
17	medical	0002_auto_20170914_0307	2017-09-23 15:08:40.1125-05
18	medical	0003_auto_20170914_0307	2017-09-23 15:08:40.391488-05
19	medical	0004_auto_20170923_1942	2017-09-23 15:08:40.581521-05
20	medical	0005_auto_20170923_1942	2017-09-23 15:08:40.66667-05
21	medical	0006_auto_20170923_1944	2017-09-23 15:08:40.742501-05
22	medical	0007_auto_20170923_1944	2017-09-23 15:08:40.767846-05
23	profiling	0004_paciente_fecha_creacion	2017-09-23 15:08:40.784245-05
24	sessions	0001_initial	2017-09-23 15:08:40.796812-05
25	medical	0008_auto_20170923_2008	2017-09-23 15:08:46.607621-05
26	medical	0009_auto_20170923_2015	2017-09-23 15:15:05.304207-05
27	medical	0010_auto_20170924_0012	2017-09-23 19:12:49.655777-05
28	medical	0011_auto_20170924_0017	2017-09-23 19:17:56.327704-05
29	medical	0012_auto_20170924_0020	2017-09-23 19:20:33.924656-05
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('django_migrations_id_seq', 29, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
azpt73un4dt3sqjiljtp9thpjtd98kv7	NDFjYTRiYjZiOWQyMmIxN2U4NTJjZjFiMDZjOGYwYWUwZDYyOGYxMjp7Il9hdXRoX3VzZXJfaGFzaCI6IjVkOWQwZThiMmM4NGFjMjU4OWEwZDRhMGI2NTA4YzQyYTI1N2FlZWMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2017-10-07 15:10:50.636116-05
\.


--
-- Data for Name: medical_categoriapregunta; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_categoriapregunta (id, texto) FROM stdin;
1	Categoría 1
2	Categoría 2
3	Categoría 3
4	Categoría 4
5	Categoría 5
\.


--
-- Name: medical_categoriapregunta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_categoriapregunta_id_seq', 5, true);


--
-- Data for Name: medical_examen; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_examen (id, fecha, paciente_id, resultado, tipo_id) FROM stdin;
\.


--
-- Name: medical_examen_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_examen_id_seq', 1, false);


--
-- Data for Name: medical_examen_respuestas; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_examen_respuestas (id, examen_id, respuesta_id) FROM stdin;
\.


--
-- Name: medical_examen_respuestas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_examen_respuestas_id_seq', 1, false);


--
-- Data for Name: medical_observaciones; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_observaciones (id, observacion, categoria_id) FROM stdin;
\.


--
-- Name: medical_observaciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_observaciones_id_seq', 1, false);


--
-- Data for Name: medical_opcionpregunta; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_opcionpregunta (id, texto, valor) FROM stdin;
1	Nunca	1
2	Casi Nunca	2
3	Casi Siempre	3
4	Siempre	4
\.


--
-- Name: medical_opcionpregunta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_opcionpregunta_id_seq', 4, true);


--
-- Data for Name: medical_pregunta; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_pregunta (id, texto, categoria_id) FROM stdin;
13	Cuando Necesito ayuda puedo recurrir a mis amigos.	1
23	Si yo no puedo cuidarme puedo buscar ayuda.	1
2	Reviso si las Formas que Practico habitualmente para mantener con salud, son buenas.	2
5	Yo puedo hacer lo necesario para mantener limpio el ambiente en el que vivo.	2
6	Hago en primer lugar lo que sea necesario para mantenerme con Salud.	2
8	Yo puedo buscar mejores formas para cuidar de mi salud que las que tengo ahora.	2
9	Cambio la frecuencia en que me baño para mantenerme limpio.	2
15	Cuando obtengo información sobre mi salud pido explicaciones sobre lo que no entiendo.	2
16	Yo examino mi cuerpo para ver si hay algún cambio.	2
17	He sido capaz de cambiar hábitos que tenia muy arraigados con tal de mejorar mi salud.	2
18	Cuando tengo que tomar una nueva medicina cuento con una persona que me brinde información sobre los efectos secundarios.	\N
20	Soy capaz de evaluar que tanto me sirve lo que hago para mantenerme con salud	2
22	Si mi salud se ve afectada yo puedo conseguir la información necesaria sobre que hacer.	2
24	Puedo sacar tiempo para mi.	2
1	A medida que cambian las circunstancias yo voy haciendo ajustes para mantener mi salud.	5
11	Cuando hay situaciones que me afectan yo las manejo de manera que pueda mantener mi forma de ser.	5
19	Soy capaz de tomar medidas para garantizar que mi familia y yo no corramos peligro.	5
25	Si presento limitaciones para movilizarme soy capaz de cuidarme como a mi me gusta.	5
3	Si tengo problemas para moverme o desplazarme me las arreglo para conseguir ayuda.	3
7	Me faltan las fuerzas necesarias para cuidarme como debo.	3
12	Pienso en hacer ejercicio y descansar un poco durante el día pero no llego hacerlo.	3
14	Pudo dormir lo suficiente  para sentirme descansado (a)	3
21	Debido a mis ocupaciones diarias me resulta difícil sacar tiempo para cuidarme.	3
10	Para mantener el peso que me corresponde hago cambios en mis hábitos alimenticios	4
\.


--
-- Name: medical_pregunta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_pregunta_id_seq', 25, true);


--
-- Data for Name: medical_pregunta_opciones; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_pregunta_opciones (id, pregunta_id, opcionpregunta_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	2	1
6	2	2
7	2	3
8	2	4
9	3	1
10	3	2
11	3	3
12	3	4
17	5	1
18	5	2
19	5	3
20	5	4
21	6	1
22	6	2
23	6	3
24	6	4
25	7	1
26	7	2
27	7	3
28	7	4
29	8	1
30	8	2
31	8	3
32	8	4
33	9	1
34	9	2
35	9	3
36	9	4
37	10	1
38	10	2
39	10	3
40	10	4
41	11	1
42	11	2
43	11	3
44	11	4
45	12	1
46	12	2
47	12	3
48	12	4
49	13	1
50	13	2
51	13	3
52	13	4
53	14	1
54	14	2
55	14	3
56	14	4
57	15	1
58	15	2
59	15	3
60	15	4
61	16	1
62	16	2
63	16	3
64	16	4
65	17	1
66	17	2
67	17	3
68	17	4
69	18	1
70	18	2
71	18	3
72	18	4
73	19	1
74	19	2
75	19	3
76	19	4
77	20	1
78	20	2
79	20	3
80	20	4
81	21	1
82	21	2
83	21	3
84	21	4
85	22	1
86	22	2
87	22	3
88	22	4
89	23	1
90	23	2
91	23	3
92	23	4
93	24	1
94	24	2
95	24	3
96	24	4
97	25	1
98	25	2
99	25	3
100	25	4
\.


--
-- Name: medical_pregunta_opciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_pregunta_opciones_id_seq', 100, true);


--
-- Data for Name: medical_puntajecategoria; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_puntajecategoria (id, categoria, nombre, minmala, maxmala, minbuena, maxbuena) FROM stdin;
\.


--
-- Name: medical_puntajecategoria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_puntajecategoria_id_seq', 1, false);


--
-- Data for Name: medical_respuesta; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_respuesta (id, valor, pregunta_id) FROM stdin;
\.


--
-- Name: medical_respuesta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_respuesta_id_seq', 1, false);


--
-- Data for Name: medical_tipoexamen; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_tipoexamen (id, nombre) FROM stdin;
1	Test Asa
\.


--
-- Name: medical_tipoexamen_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_tipoexamen_id_seq', 1, true);


--
-- Data for Name: medical_tipoexamen_preguntas; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY medical_tipoexamen_preguntas (id, tipoexamen_id, pregunta_id) FROM stdin;
1	1	1
2	1	2
3	1	3
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	1	11
12	1	12
13	1	13
14	1	14
15	1	15
16	1	16
17	1	17
18	1	18
19	1	19
20	1	20
21	1	21
22	1	22
23	1	23
24	1	24
25	1	25
\.


--
-- Name: medical_tipoexamen_preguntas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('medical_tipoexamen_preguntas_id_seq', 25, true);


--
-- Data for Name: profiling_facultad; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY profiling_facultad (id, nombre) FROM stdin;
1	Ingeniería de sistemas de información
\.


--
-- Name: profiling_facultad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('profiling_facultad_id_seq', 1, true);


--
-- Data for Name: profiling_habitsantecedents; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY profiling_habitsantecedents (id, tabaquismo, diabetes, hipertension, iam, seguimiento, fecha, paciente_id) FROM stdin;
\.


--
-- Name: profiling_habitsantecedents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('profiling_habitsantecedents_id_seq', 1, false);


--
-- Data for Name: profiling_paciente; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY profiling_paciente (id, cod_paciente, fecha_nacimiento, genero, telefono, estado_civil, estrato, facultad_id, regimen_salud_id, nombre, primer_apellido, segundo_apellido, fecha_creacion) FROM stdin;
2	123456789	1992-05-12	M	3114563245	Unión Libre	3	1	1	Diego	Angulo	Perez	2017-09-24
3	123456789	1992-05-12	M	3156437892	Soltero	4	1	1	Diego	Angulo	Perez	2017-09-24
1	123456789	1992-12-05	M	3168309653	Casado	4	1	1	Gerson	Yarce	Franco	2017-09-24
\.


--
-- Name: profiling_paciente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('profiling_paciente_id_seq', 3, true);


--
-- Data for Name: profiling_regimensalud; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY profiling_regimensalud (id, nombre) FROM stdin;
1	Prepagada
\.


--
-- Name: profiling_regimensalud_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('profiling_regimensalud_id_seq', 1, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: medical_categoriapregunta medical_categoriapregunta_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_categoriapregunta
    ADD CONSTRAINT medical_categoriapregunta_pkey PRIMARY KEY (id);


--
-- Name: medical_examen medical_examen_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_examen
    ADD CONSTRAINT medical_examen_pkey PRIMARY KEY (id);


--
-- Name: medical_examen_respuestas medical_examen_respuestas_examen_id_respuesta_id_bfd77c9c_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_examen_respuestas
    ADD CONSTRAINT medical_examen_respuestas_examen_id_respuesta_id_bfd77c9c_uniq UNIQUE (examen_id, respuesta_id);


--
-- Name: medical_examen_respuestas medical_examen_respuestas_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_examen_respuestas
    ADD CONSTRAINT medical_examen_respuestas_pkey PRIMARY KEY (id);


--
-- Name: medical_observaciones medical_observaciones_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_observaciones
    ADD CONSTRAINT medical_observaciones_pkey PRIMARY KEY (id);


--
-- Name: medical_opcionpregunta medical_opcionpregunta_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_opcionpregunta
    ADD CONSTRAINT medical_opcionpregunta_pkey PRIMARY KEY (id);


--
-- Name: medical_pregunta_opciones medical_pregunta_opcione_pregunta_id_opcionpregun_8b04f7d2_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_pregunta_opciones
    ADD CONSTRAINT medical_pregunta_opcione_pregunta_id_opcionpregun_8b04f7d2_uniq UNIQUE (pregunta_id, opcionpregunta_id);


--
-- Name: medical_pregunta_opciones medical_pregunta_opciones_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_pregunta_opciones
    ADD CONSTRAINT medical_pregunta_opciones_pkey PRIMARY KEY (id);


--
-- Name: medical_pregunta medical_pregunta_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_pregunta
    ADD CONSTRAINT medical_pregunta_pkey PRIMARY KEY (id);


--
-- Name: medical_puntajecategoria medical_puntajecategoria_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_puntajecategoria
    ADD CONSTRAINT medical_puntajecategoria_pkey PRIMARY KEY (id);


--
-- Name: medical_respuesta medical_respuesta_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_respuesta
    ADD CONSTRAINT medical_respuesta_pkey PRIMARY KEY (id);


--
-- Name: medical_tipoexamen medical_tipoexamen_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_tipoexamen
    ADD CONSTRAINT medical_tipoexamen_pkey PRIMARY KEY (id);


--
-- Name: medical_tipoexamen_preguntas medical_tipoexamen_pregu_tipoexamen_id_pregunta_i_a257816f_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_tipoexamen_preguntas
    ADD CONSTRAINT medical_tipoexamen_pregu_tipoexamen_id_pregunta_i_a257816f_uniq UNIQUE (tipoexamen_id, pregunta_id);


--
-- Name: medical_tipoexamen_preguntas medical_tipoexamen_preguntas_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_tipoexamen_preguntas
    ADD CONSTRAINT medical_tipoexamen_preguntas_pkey PRIMARY KEY (id);


--
-- Name: profiling_facultad profiling_facultad_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_facultad
    ADD CONSTRAINT profiling_facultad_pkey PRIMARY KEY (id);


--
-- Name: profiling_habitsantecedents profiling_habitsantecedents_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_habitsantecedents
    ADD CONSTRAINT profiling_habitsantecedents_pkey PRIMARY KEY (id);


--
-- Name: profiling_paciente profiling_paciente_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_paciente
    ADD CONSTRAINT profiling_paciente_pkey PRIMARY KEY (id);


--
-- Name: profiling_regimensalud profiling_regimensalud_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_regimensalud
    ADD CONSTRAINT profiling_regimensalud_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: medical_examen_paciente_id_bc525995; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_examen_paciente_id_bc525995 ON medical_examen USING btree (paciente_id);


--
-- Name: medical_examen_respuestas_examen_id_d4575408; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_examen_respuestas_examen_id_d4575408 ON medical_examen_respuestas USING btree (examen_id);


--
-- Name: medical_examen_respuestas_respuesta_id_182a6e85; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_examen_respuestas_respuesta_id_182a6e85 ON medical_examen_respuestas USING btree (respuesta_id);


--
-- Name: medical_examen_tipo_id_cdd90c3c; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_examen_tipo_id_cdd90c3c ON medical_examen USING btree (tipo_id);


--
-- Name: medical_observaciones_categoria_id_02006cb8; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_observaciones_categoria_id_02006cb8 ON medical_observaciones USING btree (categoria_id);


--
-- Name: medical_pregunta_categoria_id_c265f7c9; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_pregunta_categoria_id_c265f7c9 ON medical_pregunta USING btree (categoria_id);


--
-- Name: medical_pregunta_opciones_opcionpregunta_id_a15522dc; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_pregunta_opciones_opcionpregunta_id_a15522dc ON medical_pregunta_opciones USING btree (opcionpregunta_id);


--
-- Name: medical_pregunta_opciones_pregunta_id_42802dc8; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_pregunta_opciones_pregunta_id_42802dc8 ON medical_pregunta_opciones USING btree (pregunta_id);


--
-- Name: medical_respuesta_pregunta_id_8ebf10b1; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_respuesta_pregunta_id_8ebf10b1 ON medical_respuesta USING btree (pregunta_id);


--
-- Name: medical_tipoexamen_preguntas_pregunta_id_bccf10aa; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_tipoexamen_preguntas_pregunta_id_bccf10aa ON medical_tipoexamen_preguntas USING btree (pregunta_id);


--
-- Name: medical_tipoexamen_preguntas_tipoexamen_id_b8c0193c; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX medical_tipoexamen_preguntas_tipoexamen_id_b8c0193c ON medical_tipoexamen_preguntas USING btree (tipoexamen_id);


--
-- Name: profiling_habitsantecedents_paciente_id_007a9739; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX profiling_habitsantecedents_paciente_id_007a9739 ON profiling_habitsantecedents USING btree (paciente_id);


--
-- Name: profiling_paciente_facultad_id_b26746a6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX profiling_paciente_facultad_id_b26746a6 ON profiling_paciente USING btree (facultad_id);


--
-- Name: profiling_paciente_regimen_salud_id_aecdb775; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX profiling_paciente_regimen_salud_id_aecdb775 ON profiling_paciente USING btree (regimen_salud_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_examen medical_examen_paciente_id_bc525995_fk_profiling_paciente_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_examen
    ADD CONSTRAINT medical_examen_paciente_id_bc525995_fk_profiling_paciente_id FOREIGN KEY (paciente_id) REFERENCES profiling_paciente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_examen_respuestas medical_examen_respu_examen_id_d4575408_fk_medical_e; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_examen_respuestas
    ADD CONSTRAINT medical_examen_respu_examen_id_d4575408_fk_medical_e FOREIGN KEY (examen_id) REFERENCES medical_examen(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_examen_respuestas medical_examen_respu_respuesta_id_182a6e85_fk_medical_r; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_examen_respuestas
    ADD CONSTRAINT medical_examen_respu_respuesta_id_182a6e85_fk_medical_r FOREIGN KEY (respuesta_id) REFERENCES medical_respuesta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_examen medical_examen_tipo_id_cdd90c3c_fk_medical_tipoexamen_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_examen
    ADD CONSTRAINT medical_examen_tipo_id_cdd90c3c_fk_medical_tipoexamen_id FOREIGN KEY (tipo_id) REFERENCES medical_tipoexamen(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_observaciones medical_observacione_categoria_id_02006cb8_fk_medical_p; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_observaciones
    ADD CONSTRAINT medical_observacione_categoria_id_02006cb8_fk_medical_p FOREIGN KEY (categoria_id) REFERENCES medical_puntajecategoria(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_pregunta medical_pregunta_categoria_id_c265f7c9_fk_medical_c; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_pregunta
    ADD CONSTRAINT medical_pregunta_categoria_id_c265f7c9_fk_medical_c FOREIGN KEY (categoria_id) REFERENCES medical_categoriapregunta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_pregunta_opciones medical_pregunta_opc_opcionpregunta_id_a15522dc_fk_medical_o; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_pregunta_opciones
    ADD CONSTRAINT medical_pregunta_opc_opcionpregunta_id_a15522dc_fk_medical_o FOREIGN KEY (opcionpregunta_id) REFERENCES medical_opcionpregunta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_pregunta_opciones medical_pregunta_opc_pregunta_id_42802dc8_fk_medical_p; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_pregunta_opciones
    ADD CONSTRAINT medical_pregunta_opc_pregunta_id_42802dc8_fk_medical_p FOREIGN KEY (pregunta_id) REFERENCES medical_pregunta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_respuesta medical_respuesta_pregunta_id_8ebf10b1_fk_medical_pregunta_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_respuesta
    ADD CONSTRAINT medical_respuesta_pregunta_id_8ebf10b1_fk_medical_pregunta_id FOREIGN KEY (pregunta_id) REFERENCES medical_pregunta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_tipoexamen_preguntas medical_tipoexamen_p_pregunta_id_bccf10aa_fk_medical_p; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_tipoexamen_preguntas
    ADD CONSTRAINT medical_tipoexamen_p_pregunta_id_bccf10aa_fk_medical_p FOREIGN KEY (pregunta_id) REFERENCES medical_pregunta(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: medical_tipoexamen_preguntas medical_tipoexamen_p_tipoexamen_id_b8c0193c_fk_medical_t; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY medical_tipoexamen_preguntas
    ADD CONSTRAINT medical_tipoexamen_p_tipoexamen_id_b8c0193c_fk_medical_t FOREIGN KEY (tipoexamen_id) REFERENCES medical_tipoexamen(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: profiling_habitsantecedents profiling_habitsante_paciente_id_007a9739_fk_profiling; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_habitsantecedents
    ADD CONSTRAINT profiling_habitsante_paciente_id_007a9739_fk_profiling FOREIGN KEY (paciente_id) REFERENCES profiling_paciente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: profiling_paciente profiling_paciente_facultad_id_b26746a6_fk_profiling; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_paciente
    ADD CONSTRAINT profiling_paciente_facultad_id_b26746a6_fk_profiling FOREIGN KEY (facultad_id) REFERENCES profiling_facultad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: profiling_paciente profiling_paciente_regimen_salud_id_aecdb775_fk_profiling; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY profiling_paciente
    ADD CONSTRAINT profiling_paciente_regimen_salud_id_aecdb775_fk_profiling FOREIGN KEY (regimen_salud_id) REFERENCES profiling_regimensalud(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

