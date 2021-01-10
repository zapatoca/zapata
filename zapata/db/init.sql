--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1 (Debian 13.1-1.pgdg100+1)
-- Dumped by pg_dump version 13.1 (Debian 13.1-1.pgdg100+1)

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
-- Name: income; Type: TABLE; Schema: public; Owner: zapata
--

CREATE TABLE public.income (
    index bigint,
    "Total" bigint,
    "January" bigint
);


ALTER TABLE public.income OWNER TO zapata;

--
-- Data for Name: income; Type: TABLE DATA; Schema: public; Owner: zapata
--

COPY public.income (index, "Total", "January") FROM stdin;
1	5400	1350
2	5400	450
3	3780	3780
4	3780	315
5	3780	945
6	3780	157
7	3780	0
8	4500	2250
9	4500	1125
10	4860	1215
11	5400	450
12	5400	1350
13	4860	810
14	5400	5400
15	4860	1215
16	5400	1350
17	4860	405
18	7200	3600
19	7200	600
\.


--
-- Name: ix_income_index; Type: INDEX; Schema: public; Owner: zapata
--

CREATE INDEX ix_income_index ON public.income USING btree (index);


--
-- PostgreSQL database dump complete
--

