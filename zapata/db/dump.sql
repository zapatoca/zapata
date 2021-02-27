--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2 (Debian 13.2-1.pgdg100+1)
-- Dumped by pg_dump version 13.2 (Debian 13.2-1.pgdg100+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: buildings; Type: TABLE; Schema: public; Owner: zapata
--

CREATE TABLE public.buildings (
    id integer NOT NULL,
    address character varying,
    flats integer
);


ALTER TABLE public.buildings OWNER TO zapata;

--
-- Name: buildings_id_seq; Type: SEQUENCE; Schema: public; Owner: zapata
--

CREATE SEQUENCE public.buildings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.buildings_id_seq OWNER TO zapata;

--
-- Name: buildings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zapata
--

ALTER SEQUENCE public.buildings_id_seq OWNED BY public.buildings.id;


--
-- Name: fees; Type: TABLE; Schema: public; Owner: zapata
--

CREATE TABLE public.fees (
    id bigint,
    "Apartment" bigint,
    "Fee_type" text,
    "Amount" bigint,
    project bigint,
    "Jan" bigint,
    "Feb" bigint,
    "Balance" bigint,
    "Alert" boolean
);


ALTER TABLE public.fees OWNER TO zapata;

--
-- Name: incidents; Type: TABLE; Schema: public; Owner: zapata
--

CREATE TABLE public.incidents (
    id integer NOT NULL,
    description character varying
);


ALTER TABLE public.incidents OWNER TO zapata;

--
-- Name: incidents_id_seq; Type: SEQUENCE; Schema: public; Owner: zapata
--

CREATE SEQUENCE public.incidents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.incidents_id_seq OWNER TO zapata;

--
-- Name: incidents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zapata
--

ALTER SEQUENCE public.incidents_id_seq OWNED BY public.incidents.id;


--
-- Name: income; Type: TABLE; Schema: public; Owner: zapata
--

CREATE TABLE public.income (
    index bigint,
    "Amount" bigint,
    "Jan" bigint,
    "Feb" bigint,
    "Monthly" bigint,
    "Balance" bigint,
    "Alert" boolean
);


ALTER TABLE public.income OWNER TO zapata;

--
-- Name: projects; Type: TABLE; Schema: public; Owner: zapata
--

CREATE TABLE public.projects (
    id integer NOT NULL,
    summary character varying(80),
    budget integer
);


ALTER TABLE public.projects OWNER TO zapata;

--
-- Name: projects_id_seq; Type: SEQUENCE; Schema: public; Owner: zapata
--

CREATE SEQUENCE public.projects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.projects_id_seq OWNER TO zapata;

--
-- Name: projects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zapata
--

ALTER SEQUENCE public.projects_id_seq OWNED BY public.projects.id;


--
-- Name: buildings id; Type: DEFAULT; Schema: public; Owner: zapata
--

ALTER TABLE ONLY public.buildings ALTER COLUMN id SET DEFAULT nextval('public.buildings_id_seq'::regclass);


--
-- Name: incidents id; Type: DEFAULT; Schema: public; Owner: zapata
--

ALTER TABLE ONLY public.incidents ALTER COLUMN id SET DEFAULT nextval('public.incidents_id_seq'::regclass);


--
-- Name: projects id; Type: DEFAULT; Schema: public; Owner: zapata
--

ALTER TABLE ONLY public.projects ALTER COLUMN id SET DEFAULT nextval('public.projects_id_seq'::regclass);


--
-- Data for Name: buildings; Type: TABLE DATA; Schema: public; Owner: zapata
--

COPY public.buildings (id, address, flats) FROM stdin;
1	6 Meridor Yaakov st., Tel Aviv, Israel	19
\.


--
-- Data for Name: fees; Type: TABLE DATA; Schema: public; Owner: zapata
--

COPY public.fees (id, "Apartment", "Fee_type", "Amount", project, "Jan", "Feb", "Balance", "Alert") FROM stdin;
1	1	2	4875	1	0	4875	0	f
2	2	2	4875	1	0	4875	0	f
3	3	2	3415	1	0	3415	0	f
4	4	2	3415	1	0	3415	0	f
5	5	2	3415	1	0	3415	0	f
6	6	2	3415	1	0	3415	0	f
7	7	2	3415	1	0	3415	0	f
8	8	2	4060	1	0	0	4060	t
9	9	2	4060	1	0	4060	0	f
10	10	2	4390	1	0	4390	0	f
11	11	2	4875	1	0	4875	0	f
12	12	2	4875	1	0	4875	0	f
13	13	2	4390	1	0	4390	0	f
14	14	2	4875	1	0	4875	0	f
15	15	2	4390	1	0	4390	0	f
16	16	2	4875	1	0	4875	0	f
17	17	2	4390	1	0	4390	0	f
18	18	2	6500	1	0	6500	0	f
19	19	2	6500	1	0	6500	0	f
\.


--
-- Data for Name: incidents; Type: TABLE DATA; Schema: public; Owner: zapata
--

COPY public.incidents (id, description) FROM stdin;
1	חיפויים
2	נזילת מים בחדר דוודים קומה 3
3	תאורת לובי קומות 3-4
4	להוציא קבלה ליפה כדורי על סך 700 ש״ח
5	לשלם לליאורה מילבאום 37.5 ש״ח בגין רכישת קבלות
6	תשלום לגנן הקודם - 1200 ש״ח
7	שכפול מפתחות לחדר אופניים
8	אינטרקום - הורדת עוצמת הצלצול
\.


--
-- Data for Name: income; Type: TABLE DATA; Schema: public; Owner: zapata
--

COPY public.income (index, "Amount", "Jan", "Feb", "Monthly", "Balance", "Alert") FROM stdin;
1	5400	1350	0	450	4050	f
2	5400	450	450	450	4500	f
3	3780	3780	0	315	0	f
4	3780	315	315	315	3150	f
5	3780	945	0	315	2835	f
6	3780	630	0	315	3150	f
7	3780	315	315	315	3150	f
8	4500	2250	0	375	2250	f
9	4500	1125	0	375	3375	f
10	4860	1215	0	405	3645	f
11	5400	450	450	450	4500	f
12	5400	1350	0	450	4050	f
13	4860	810	0	405	4050	f
14	5400	5400	0	450	0	f
15	4860	1215	0	405	3645	f
16	5400	1350	0	450	4050	f
17	4860	405	405	405	4050	f
18	7200	3600	0	600	3600	f
19	7200	600	600	600	6000	f
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: zapata
--

COPY public.projects (id, summary, budget) FROM stdin;
1	Claddings	85005
\.


--
-- Name: buildings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zapata
--

SELECT pg_catalog.setval('public.buildings_id_seq', 1, true);


--
-- Name: incidents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zapata
--

SELECT pg_catalog.setval('public.incidents_id_seq', 8, true);


--
-- Name: projects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zapata
--

SELECT pg_catalog.setval('public.projects_id_seq', 1, true);


--
-- Name: buildings buildings_pkey; Type: CONSTRAINT; Schema: public; Owner: zapata
--

ALTER TABLE ONLY public.buildings
    ADD CONSTRAINT buildings_pkey PRIMARY KEY (id);


--
-- Name: incidents incidents_pkey; Type: CONSTRAINT; Schema: public; Owner: zapata
--

ALTER TABLE ONLY public.incidents
    ADD CONSTRAINT incidents_pkey PRIMARY KEY (id);


--
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: zapata
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

