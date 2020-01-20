--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
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


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
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


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: perfect_slot_customuser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfect_slot_customuser (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    street character varying(128) NOT NULL,
    house_nr character varying(10) NOT NULL,
    zip_code character varying(6) NOT NULL,
    city character varying(128) NOT NULL
);


ALTER TABLE public.perfect_slot_customuser OWNER TO postgres;

--
-- Name: perfect_slot_customuser_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfect_slot_customuser_groups (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.perfect_slot_customuser_groups OWNER TO postgres;

--
-- Name: perfect_slot_customuser_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.perfect_slot_customuser_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.perfect_slot_customuser_groups_id_seq OWNER TO postgres;

--
-- Name: perfect_slot_customuser_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.perfect_slot_customuser_groups_id_seq OWNED BY public.perfect_slot_customuser_groups.id;


--
-- Name: perfect_slot_customuser_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.perfect_slot_customuser_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.perfect_slot_customuser_id_seq OWNER TO postgres;

--
-- Name: perfect_slot_customuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.perfect_slot_customuser_id_seq OWNED BY public.perfect_slot_customuser.id;


--
-- Name: perfect_slot_customuser_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfect_slot_customuser_user_permissions (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.perfect_slot_customuser_user_permissions OWNER TO postgres;

--
-- Name: perfect_slot_customuser_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.perfect_slot_customuser_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.perfect_slot_customuser_user_permissions_id_seq OWNER TO postgres;

--
-- Name: perfect_slot_customuser_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.perfect_slot_customuser_user_permissions_id_seq OWNED BY public.perfect_slot_customuser_user_permissions.id;


--
-- Name: perfect_slot_datetimeslot; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfect_slot_datetimeslot (
    id integer NOT NULL,
    date_time_from timestamp with time zone NOT NULL,
    date_time_to timestamp with time zone NOT NULL,
    winning boolean NOT NULL,
    event_id integer NOT NULL
);


ALTER TABLE public.perfect_slot_datetimeslot OWNER TO postgres;

--
-- Name: perfect_slot_datetimeslot_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.perfect_slot_datetimeslot_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.perfect_slot_datetimeslot_id_seq OWNER TO postgres;

--
-- Name: perfect_slot_datetimeslot_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.perfect_slot_datetimeslot_id_seq OWNED BY public.perfect_slot_datetimeslot.id;


--
-- Name: perfect_slot_event; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfect_slot_event (
    id integer NOT NULL,
    title character varying(128) NOT NULL,
    description text NOT NULL,
    location character varying(256) NOT NULL,
    creation_time timestamp with time zone NOT NULL,
    update_time timestamp with time zone NOT NULL,
    approx_duration smallint NOT NULL,
    is_archive boolean NOT NULL,
    owner_id integer NOT NULL,
    is_in_progress boolean NOT NULL,
    is_upcoming boolean NOT NULL
);


ALTER TABLE public.perfect_slot_event OWNER TO postgres;

--
-- Name: perfect_slot_event_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.perfect_slot_event_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.perfect_slot_event_id_seq OWNER TO postgres;

--
-- Name: perfect_slot_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.perfect_slot_event_id_seq OWNED BY public.perfect_slot_event.id;


--
-- Name: perfect_slot_event_participants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfect_slot_event_participants (
    id integer NOT NULL,
    event_id integer NOT NULL,
    customuser_id integer NOT NULL
);


ALTER TABLE public.perfect_slot_event_participants OWNER TO postgres;

--
-- Name: perfect_slot_event_participants_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.perfect_slot_event_participants_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.perfect_slot_event_participants_id_seq OWNER TO postgres;

--
-- Name: perfect_slot_event_participants_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.perfect_slot_event_participants_id_seq OWNED BY public.perfect_slot_event_participants.id;


--
-- Name: perfect_slot_participantslotvote; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.perfect_slot_participantslotvote (
    id integer NOT NULL,
    vote smallint NOT NULL,
    participant_id integer NOT NULL,
    slot_id integer NOT NULL
);


ALTER TABLE public.perfect_slot_participantslotvote OWNER TO postgres;

--
-- Name: perfect_slot_participantslotvote_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.perfect_slot_participantslotvote_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.perfect_slot_participantslotvote_id_seq OWNER TO postgres;

--
-- Name: perfect_slot_participantslotvote_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.perfect_slot_participantslotvote_id_seq OWNED BY public.perfect_slot_participantslotvote.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: perfect_slot_customuser id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser ALTER COLUMN id SET DEFAULT nextval('public.perfect_slot_customuser_id_seq'::regclass);


--
-- Name: perfect_slot_customuser_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_groups ALTER COLUMN id SET DEFAULT nextval('public.perfect_slot_customuser_groups_id_seq'::regclass);


--
-- Name: perfect_slot_customuser_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.perfect_slot_customuser_user_permissions_id_seq'::regclass);


--
-- Name: perfect_slot_datetimeslot id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_datetimeslot ALTER COLUMN id SET DEFAULT nextval('public.perfect_slot_datetimeslot_id_seq'::regclass);


--
-- Name: perfect_slot_event id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_event ALTER COLUMN id SET DEFAULT nextval('public.perfect_slot_event_id_seq'::regclass);


--
-- Name: perfect_slot_event_participants id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_event_participants ALTER COLUMN id SET DEFAULT nextval('public.perfect_slot_event_participants_id_seq'::regclass);


--
-- Name: perfect_slot_participantslotvote id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_participantslotvote ALTER COLUMN id SET DEFAULT nextval('public.perfect_slot_participantslotvote_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add user	1	add_customuser
2	Can change user	1	change_customuser
3	Can delete user	1	delete_customuser
4	Can view user	1	view_customuser
5	Can add date time slot	2	add_datetimeslot
6	Can change date time slot	2	change_datetimeslot
7	Can delete date time slot	2	delete_datetimeslot
8	Can view date time slot	2	view_datetimeslot
9	Can add participant slot vote	3	add_participantslotvote
10	Can change participant slot vote	3	change_participantslotvote
11	Can delete participant slot vote	3	delete_participantslotvote
12	Can view participant slot vote	3	view_participantslotvote
13	Can add event	4	add_event
14	Can change event	4	change_event
15	Can delete event	4	delete_event
16	Can view event	4	view_event
17	Can add log entry	5	add_logentry
18	Can change log entry	5	change_logentry
19	Can delete log entry	5	delete_logentry
20	Can view log entry	5	view_logentry
21	Can add permission	6	add_permission
22	Can change permission	6	change_permission
23	Can delete permission	6	delete_permission
24	Can view permission	6	view_permission
25	Can add group	7	add_group
26	Can change group	7	change_group
27	Can delete group	7	delete_group
28	Can view group	7	view_group
29	Can add content type	8	add_contenttype
30	Can change content type	8	change_contenttype
31	Can delete content type	8	delete_contenttype
32	Can view content type	8	view_contenttype
33	Can add session	9	add_session
34	Can change session	9	change_session
35	Can delete session	9	delete_session
36	Can view session	9	view_session
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	perfect_slot	customuser
2	perfect_slot	datetimeslot
3	perfect_slot	participantslotvote
4	perfect_slot	event
5	admin	logentry
6	auth	permission
7	auth	group
8	contenttypes	contenttype
9	sessions	session
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-01-19 11:29:16.231583+01
2	contenttypes	0002_remove_content_type_name	2020-01-19 11:29:16.274777+01
3	auth	0001_initial	2020-01-19 11:29:16.516439+01
4	auth	0002_alter_permission_name_max_length	2020-01-19 11:29:16.812738+01
5	auth	0003_alter_user_email_max_length	2020-01-19 11:29:16.846329+01
6	auth	0004_alter_user_username_opts	2020-01-19 11:29:16.875769+01
7	auth	0005_alter_user_last_login_null	2020-01-19 11:29:16.912875+01
8	auth	0006_require_contenttypes_0002	2020-01-19 11:29:16.925839+01
9	auth	0007_alter_validators_add_error_messages	2020-01-19 11:29:16.952842+01
10	auth	0008_alter_user_username_max_length	2020-01-19 11:29:16.987618+01
11	auth	0009_alter_user_last_name_max_length	2020-01-19 11:29:17.019585+01
12	auth	0010_alter_group_name_max_length	2020-01-19 11:29:17.059546+01
13	auth	0011_update_proxy_permissions	2020-01-19 11:29:17.080527+01
14	perfect_slot	0001_initial	2020-01-19 11:29:17.308968+01
15	admin	0001_initial	2020-01-19 11:29:17.758363+01
16	admin	0002_logentry_remove_auto_add	2020-01-19 11:29:17.908612+01
17	admin	0003_logentry_add_action_flag_choices	2020-01-19 11:29:17.964679+01
18	perfect_slot	0002_auto_20200102_1759	2020-01-19 11:29:18.33607+01
19	perfect_slot	0003_auto_20200102_1807	2020-01-19 11:29:18.746608+01
20	perfect_slot	0004_auto_20200102_1809	2020-01-19 11:29:18.835766+01
21	perfect_slot	0005_auto_20200116_2328	2020-01-19 11:29:19.231651+01
22	sessions	0001_initial	2020-01-19 11:29:19.329155+01
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
s1is1a7146rsd3srhpzqq1jzed2hrt4h	ZTdlOGY0MzhmYTYzMTFhMzAyZDQ3ZTBlNzQ3ZDE1NTg5NDQzMGExMTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMDMwZmE2YmJjNDVkNWQ0YjAwMmFhY2U2MzBkOWQ0YThlNjkwNjc5In0=	2020-02-02 12:54:52.247987+01
v93z0w6tgovhbtuuxf03nbkawvqkni6y	NzNmYjc2NWU4N2JlY2IwYTkxNWIxNjlmZGQ4YjhmNTBhMjAxNDUyMDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYmFmZTNlYzU3ZTVmNGUwNWRkOTg5NTUzMmM2MGFlZTBhNmZhZjRkIn0=	2020-02-02 15:45:55.640095+01
vdu8ia1op39vfcnlykuo7ftkongnq0ga	NzNmYjc2NWU4N2JlY2IwYTkxNWIxNjlmZGQ4YjhmNTBhMjAxNDUyMDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYmFmZTNlYzU3ZTVmNGUwNWRkOTg5NTUzMmM2MGFlZTBhNmZhZjRkIn0=	2020-02-02 15:49:08.098667+01
lqekkhth453xexztusxcxigoklcazwnv	ZTdlOGY0MzhmYTYzMTFhMzAyZDQ3ZTBlNzQ3ZDE1NTg5NDQzMGExMTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMDMwZmE2YmJjNDVkNWQ0YjAwMmFhY2U2MzBkOWQ0YThlNjkwNjc5In0=	2020-02-02 16:49:53.388805+01
ei7um71kqqchw1ribfxykanph37i180e	ZTdlOGY0MzhmYTYzMTFhMzAyZDQ3ZTBlNzQ3ZDE1NTg5NDQzMGExMTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMDMwZmE2YmJjNDVkNWQ0YjAwMmFhY2U2MzBkOWQ0YThlNjkwNjc5In0=	2020-02-02 18:06:42.666238+01
q35hq2bmktn27egdc68ydkhu6zo89f5h	ZTdlOGY0MzhmYTYzMTFhMzAyZDQ3ZTBlNzQ3ZDE1NTg5NDQzMGExMTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyMDMwZmE2YmJjNDVkNWQ0YjAwMmFhY2U2MzBkOWQ0YThlNjkwNjc5In0=	2020-02-02 20:48:29.640724+01
rjzd0bqca5yv6hwalajhssqtoh3xkjta	NzNmYjc2NWU4N2JlY2IwYTkxNWIxNjlmZGQ4YjhmNTBhMjAxNDUyMDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYmFmZTNlYzU3ZTVmNGUwNWRkOTg5NTUzMmM2MGFlZTBhNmZhZjRkIn0=	2020-02-02 22:40:23.709596+01
d7a2kxrrerx729vnad2blxpztkqnetxo	N2MyMmNiYWYxZGE0N2MwMjY5YWY1MmJmYTRhNzkzNGY3ZjRjMmNmZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMWZmN2Q1MmY1YmQ3MDM2YjM2NDFjN2M2NjQwMGJhOTc4MWM2OTVjIn0=	2020-02-03 19:53:18.752669+01
2tokncay9sno1ekqz4m4muunpy9hyyhz	N2MyMmNiYWYxZGE0N2MwMjY5YWY1MmJmYTRhNzkzNGY3ZjRjMmNmZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMWZmN2Q1MmY1YmQ3MDM2YjM2NDFjN2M2NjQwMGJhOTc4MWM2OTVjIn0=	2020-02-03 21:11:47.767646+01
\.


--
-- Data for Name: perfect_slot_customuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.perfect_slot_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, street, house_nr, zip_code, city) FROM stdin;
2	pbkdf2_sha256$180000$J7ALRmwzPmA1$Xio0ml/TIz53mIJPtEm9ymkco0Qx2VeDtqFi1iv1A2s=	2020-01-20 19:03:44.216527+01	f	ala	Alicja	Kołaczkowska	ala@wp.pl	f	t	2020-01-19 11:32:08.096911+01	Grochowska	3	04-148	Warszawa
3	pbkdf2_sha256$180000$fr6MxCVIlyp5$yk7efnx88ZGqrQTd3h2ekjbMXHpDwSseok1oxgWx09w=	2020-01-20 21:08:29.435256+01	t	zuzanna	Zuzanna	Pończocha	zuzanna@wp.pl	t	t	2020-01-19 11:34:26.02648+01	Belgradzka	10	02-793	Warszawa
1	pbkdf2_sha256$180000$QTOR7LaJ9ttm$4rJNN1/WVTGzp69Uad5eICE7iiW6YMzVRXugGCKrj3I=	2020-01-20 21:11:47.756611+01	f	ela	Elżbieta	Karowa	ela@wp.pl	f	t	2020-01-19 11:31:08.266247+01	Marszałkowska	12	00-950	Warszawa
\.


--
-- Data for Name: perfect_slot_customuser_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.perfect_slot_customuser_groups (id, customuser_id, group_id) FROM stdin;
\.


--
-- Data for Name: perfect_slot_customuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.perfect_slot_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
\.


--
-- Data for Name: perfect_slot_datetimeslot; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.perfect_slot_datetimeslot (id, date_time_from, date_time_to, winning, event_id) FROM stdin;
1	2020-03-02 19:00:00+01	2020-03-02 22:00:00+01	f	1
2	2019-03-03 19:00:00+01	2019-03-03 21:00:00+01	f	1
3	2019-05-02 19:00:00+02	2019-05-02 23:00:00+02	f	2
5	2019-03-02 01:00:00+01	2019-03-04 01:00:00+01	f	1
6	2022-03-02 01:00:00+01	2022-03-05 01:00:00+01	f	1
7	2019-12-02 01:00:00+01	2019-12-03 01:00:00+01	f	1
8	2019-11-02 01:00:00+01	2019-11-05 01:00:00+01	f	1
9	2020-04-02 19:00:00+02	2020-04-02 23:00:00+02	f	3
10	2021-03-18 16:30:00+01	2021-03-18 18:30:00+01	f	3
4	2019-04-02 18:00:00+02	2019-04-02 22:00:00+02	f	2
\.


--
-- Data for Name: perfect_slot_event; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.perfect_slot_event (id, title, description, location, creation_time, update_time, approx_duration, is_archive, owner_id, is_in_progress, is_upcoming) FROM stdin;
3	Urodziny	Zapraszam na urodziny mojej papugi. Kończy 50 lat!	Kino Muranów	2020-01-19 12:32:45.849907+01	2020-01-19 12:35:04.710922+01	4	f	1	t	f
1	Piwko	Chodźcie, fajnie będzie	Centrum	2020-01-19 11:43:17.163538+01	2020-01-19 17:40:46.200441+01	3	f	3	t	f
2	Klub książkowy	Spotkajmy się porozmawiać o Annie Kareninie.	Marszałkowska 14, 02-004 Warszawa	2020-01-19 11:46:53.294119+01	2020-01-19 17:43:40.392155+01	4	f	3	t	f
\.


--
-- Data for Name: perfect_slot_event_participants; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.perfect_slot_event_participants (id, event_id, customuser_id) FROM stdin;
1	1	1
2	1	2
3	2	2
4	3	2
5	3	3
\.


--
-- Data for Name: perfect_slot_participantslotvote; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.perfect_slot_participantslotvote (id, vote, participant_id, slot_id) FROM stdin;
6	2	2	4
5	2	2	3
17	3	2	10
4	3	2	2
8	1	2	5
10	1	2	6
12	1	2	7
14	3	2	8
15	1	2	9
7	1	1	5
3	1	1	2
11	1	1	7
13	3	1	8
1	-2	1	1
2	-2	2	1
16	3	3	9
18	1	3	10
9	3	1	6
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 36, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 9, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 22, true);


--
-- Name: perfect_slot_customuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.perfect_slot_customuser_groups_id_seq', 1, false);


--
-- Name: perfect_slot_customuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.perfect_slot_customuser_id_seq', 3, true);


--
-- Name: perfect_slot_customuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.perfect_slot_customuser_user_permissions_id_seq', 1, false);


--
-- Name: perfect_slot_datetimeslot_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.perfect_slot_datetimeslot_id_seq', 10, true);


--
-- Name: perfect_slot_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.perfect_slot_event_id_seq', 3, true);


--
-- Name: perfect_slot_event_participants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.perfect_slot_event_participants_id_seq', 5, true);


--
-- Name: perfect_slot_participantslotvote_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.perfect_slot_participantslotvote_id_seq', 18, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: perfect_slot_customuser_groups perfect_slot_customuser__customuser_id_group_id_0e369b9e_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_groups
    ADD CONSTRAINT perfect_slot_customuser__customuser_id_group_id_0e369b9e_uniq UNIQUE (customuser_id, group_id);


--
-- Name: perfect_slot_customuser_user_permissions perfect_slot_customuser__customuser_id_permission_1d73cf80_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_user_permissions
    ADD CONSTRAINT perfect_slot_customuser__customuser_id_permission_1d73cf80_uniq UNIQUE (customuser_id, permission_id);


--
-- Name: perfect_slot_customuser_groups perfect_slot_customuser_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_groups
    ADD CONSTRAINT perfect_slot_customuser_groups_pkey PRIMARY KEY (id);


--
-- Name: perfect_slot_customuser perfect_slot_customuser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser
    ADD CONSTRAINT perfect_slot_customuser_pkey PRIMARY KEY (id);


--
-- Name: perfect_slot_customuser_user_permissions perfect_slot_customuser_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_user_permissions
    ADD CONSTRAINT perfect_slot_customuser_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: perfect_slot_customuser perfect_slot_customuser_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser
    ADD CONSTRAINT perfect_slot_customuser_username_key UNIQUE (username);


--
-- Name: perfect_slot_datetimeslot perfect_slot_datetimeslot_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_datetimeslot
    ADD CONSTRAINT perfect_slot_datetimeslot_pkey PRIMARY KEY (id);


--
-- Name: perfect_slot_event_participants perfect_slot_event_parti_event_id_customuser_id_3fc3195b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_event_participants
    ADD CONSTRAINT perfect_slot_event_parti_event_id_customuser_id_3fc3195b_uniq UNIQUE (event_id, customuser_id);


--
-- Name: perfect_slot_event_participants perfect_slot_event_participants_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_event_participants
    ADD CONSTRAINT perfect_slot_event_participants_pkey PRIMARY KEY (id);


--
-- Name: perfect_slot_event perfect_slot_event_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_event
    ADD CONSTRAINT perfect_slot_event_pkey PRIMARY KEY (id);


--
-- Name: perfect_slot_participantslotvote perfect_slot_participantslotvote_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_participantslotvote
    ADD CONSTRAINT perfect_slot_participantslotvote_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: perfect_slot_customuser_groups_customuser_id_93a70595; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_customuser_groups_customuser_id_93a70595 ON public.perfect_slot_customuser_groups USING btree (customuser_id);


--
-- Name: perfect_slot_customuser_groups_group_id_2913b2af; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_customuser_groups_group_id_2913b2af ON public.perfect_slot_customuser_groups USING btree (group_id);


--
-- Name: perfect_slot_customuser_user_permissions_customuser_id_f946a6d0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_customuser_user_permissions_customuser_id_f946a6d0 ON public.perfect_slot_customuser_user_permissions USING btree (customuser_id);


--
-- Name: perfect_slot_customuser_user_permissions_permission_id_a10af594; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_customuser_user_permissions_permission_id_a10af594 ON public.perfect_slot_customuser_user_permissions USING btree (permission_id);


--
-- Name: perfect_slot_customuser_username_213acf32_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_customuser_username_213acf32_like ON public.perfect_slot_customuser USING btree (username varchar_pattern_ops);


--
-- Name: perfect_slot_datetimeslot_event_id_4c8c9d96; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_datetimeslot_event_id_4c8c9d96 ON public.perfect_slot_datetimeslot USING btree (event_id);


--
-- Name: perfect_slot_event_owner_id_14539403; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_event_owner_id_14539403 ON public.perfect_slot_event USING btree (owner_id);


--
-- Name: perfect_slot_event_participants_customuser_id_88d7587b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_event_participants_customuser_id_88d7587b ON public.perfect_slot_event_participants USING btree (customuser_id);


--
-- Name: perfect_slot_event_participants_event_id_a3d4860c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_event_participants_event_id_a3d4860c ON public.perfect_slot_event_participants USING btree (event_id);


--
-- Name: perfect_slot_participantslotvote_participant_id_f707a493; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_participantslotvote_participant_id_f707a493 ON public.perfect_slot_participantslotvote USING btree (participant_id);


--
-- Name: perfect_slot_participantslotvote_slot_id_54be3ad3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX perfect_slot_participantslotvote_slot_id_54be3ad3 ON public.perfect_slot_participantslotvote USING btree (slot_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_perfect_slot_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_perfect_slot_customuser_id FOREIGN KEY (user_id) REFERENCES public.perfect_slot_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_customuser_groups perfect_slot_customu_customuser_id_93a70595_fk_perfect_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_groups
    ADD CONSTRAINT perfect_slot_customu_customuser_id_93a70595_fk_perfect_s FOREIGN KEY (customuser_id) REFERENCES public.perfect_slot_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_customuser_user_permissions perfect_slot_customu_customuser_id_f946a6d0_fk_perfect_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_user_permissions
    ADD CONSTRAINT perfect_slot_customu_customuser_id_f946a6d0_fk_perfect_s FOREIGN KEY (customuser_id) REFERENCES public.perfect_slot_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_customuser_groups perfect_slot_customu_group_id_2913b2af_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_groups
    ADD CONSTRAINT perfect_slot_customu_group_id_2913b2af_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_customuser_user_permissions perfect_slot_customu_permission_id_a10af594_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_customuser_user_permissions
    ADD CONSTRAINT perfect_slot_customu_permission_id_a10af594_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_datetimeslot perfect_slot_datetimeslot_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_datetimeslot
    ADD CONSTRAINT perfect_slot_datetimeslot_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.perfect_slot_event(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_event perfect_slot_event_owner_id_14539403_fk_perfect_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_event
    ADD CONSTRAINT perfect_slot_event_owner_id_14539403_fk_perfect_s FOREIGN KEY (owner_id) REFERENCES public.perfect_slot_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_event_participants perfect_slot_event_p_customuser_id_88d7587b_fk_perfect_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_event_participants
    ADD CONSTRAINT perfect_slot_event_p_customuser_id_88d7587b_fk_perfect_s FOREIGN KEY (customuser_id) REFERENCES public.perfect_slot_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_event_participants perfect_slot_event_p_event_id_a3d4860c_fk_perfect_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_event_participants
    ADD CONSTRAINT perfect_slot_event_p_event_id_a3d4860c_fk_perfect_s FOREIGN KEY (event_id) REFERENCES public.perfect_slot_event(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_participantslotvote perfect_slot_partici_participant_id_f707a493_fk_perfect_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_participantslotvote
    ADD CONSTRAINT perfect_slot_partici_participant_id_f707a493_fk_perfect_s FOREIGN KEY (participant_id) REFERENCES public.perfect_slot_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: perfect_slot_participantslotvote perfect_slot_partici_slot_id_54be3ad3_fk_perfect_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.perfect_slot_participantslotvote
    ADD CONSTRAINT perfect_slot_partici_slot_id_54be3ad3_fk_perfect_s FOREIGN KEY (slot_id) REFERENCES public.perfect_slot_datetimeslot(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

