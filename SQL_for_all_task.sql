-- Table: public.test_dev_directory_product

-- DROP TABLE IF EXISTS public.test_dev_directory_product;

CREATE TABLE IF NOT EXISTS public.test_dev_directory_product
(
    id bigint NOT NULL DEFAULT nextval('test_dev_directory_product_id_seq'::regclass),
    name_product character varying(255) COLLATE pg_catalog."default",
    price integer,
    CONSTRAINT test_dev_directory_product_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.test_dev_directory_product
    OWNER to postgres;
	
-- Table: public.test_dev_directory_counterparties

-- DROP TABLE IF EXISTS public.test_dev_directory_counterparties;

CREATE TABLE IF NOT EXISTS public.test_dev_directory_counterparties
(
    id bigint NOT NULL DEFAULT nextval('test_dev_directory_counterparties_id_seq'::regclass),
    contract character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT test_dev_directory_counterparties_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.test_dev_directory_counterparties
    OWNER to postgres;
	
-- Table: public.test_dev_document_header

-- DROP TABLE IF EXISTS public.test_dev_document_header;

CREATE TABLE IF NOT EXISTS public.test_dev_document_header
(
    id bigint NOT NULL DEFAULT nextval('test_dev_document_header_id_seq'::regclass),
    number_document integer,
    date date NOT NULL,
    summ_document integer,
    link_dc_id bigint,
    state_document character varying(255) COLLATE pg_catalog."default",
    type_document character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT test_dev_document_header_pkey PRIMARY KEY (id),
    CONSTRAINT test_dev_document_header_link_dc_id_key UNIQUE (link_dc_id),
    CONSTRAINT test_dev_document_he_link_dc_id_1db4a720_fk_test_dev_ FOREIGN KEY (link_dc_id)
        REFERENCES public.test_dev_directory_counterparties (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.test_dev_document_header
    OWNER to postgres;

-- Table: public.test_dev_product_stock

-- DROP TABLE IF EXISTS public.test_dev_product_stock;

CREATE TABLE IF NOT EXISTS public.test_dev_product_stock
(
    id bigint NOT NULL DEFAULT nextval('test_dev_product_stock_id_seq'::regclass),
    count_fact integer,
    count_reserv integer,
    link_dp_id bigint,
    CONSTRAINT test_dev_product_stock_pkey PRIMARY KEY (id),
    CONSTRAINT test_dev_product_stock_link_dp_id_key UNIQUE (link_dp_id),
    CONSTRAINT test_dev_product_sto_link_dp_id_9b369afa_fk_test_dev_ FOREIGN KEY (link_dp_id)
        REFERENCES public.test_dev_directory_product (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.test_dev_product_stock
    OWNER to postgres;
	
-- Table: public.test_dev_document_specification

-- DROP TABLE IF EXISTS public.test_dev_document_specification;

CREATE TABLE IF NOT EXISTS public.test_dev_document_specification
(
    id bigint NOT NULL DEFAULT nextval('test_dev_document_specification_id_seq'::regclass),
    counts integer,
    counts_reserv integer,
    prices integer,
    discount integer,
    link_dh_id bigint,
    link_dp_id bigint,
    link_ps_id bigint,
    CONSTRAINT test_dev_document_specification_pkey PRIMARY KEY (id),
    CONSTRAINT test_dev_document_specification_link_dh_id_key UNIQUE (link_dh_id),
    CONSTRAINT test_dev_document_specification_link_dp_id_key UNIQUE (link_dp_id),
    CONSTRAINT test_dev_document_specification_link_ps_id_key UNIQUE (link_ps_id),
    CONSTRAINT test_dev_document_sp_link_dh_id_0a216b02_fk_test_dev_ FOREIGN KEY (link_dh_id)
        REFERENCES public.test_dev_document_header (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT test_dev_document_sp_link_dp_id_e0ae2538_fk_test_dev_ FOREIGN KEY (link_dp_id)
        REFERENCES public.test_dev_directory_product (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT test_dev_document_sp_link_ps_id_c8b4df18_fk_test_dev_ FOREIGN KEY (link_ps_id)
        REFERENCES public.test_dev_product_stock (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.test_dev_document_specification
    OWNER to postgres;
