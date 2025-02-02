-- create table
CREATE TABLE public.data (
    date TIMESTAMP NOT NULL,
    img_url VARCHAR,
    title VARCHAR,
    content VARCHAR,
    wav_url VARCHAR,
    moved BOOLEAN,
    CONSTRAINT pk_data PRIMARY KEY (date)
);

ALTER TABLE public.data
    OWNER TO root;

GRANT DELETE, INSERT, SELECT, UPDATE ON public.data TO project;

-- request history
select * from net._http_response;

-- 트리거 생성
create trigger after_insert_data_trigger
    after insert
    on data
    for each row
    execute procedure after_insert_data();

