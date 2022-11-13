
alter table appearance rename to appearance_old;

CREATE TABLE IF NOT EXISTS public.appearance
(
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    "position" character varying(20) COLLATE pg_catalog."default",
    assists integer,
    num_shots integer,
    goals integer,
    yellow_cards integer,
    red_cards integer,
    CONSTRAINT appearance_pkeys PRIMARY KEY (game_id, player_id),
    CONSTRAINT "game_id" FOREIGN KEY (game_id)
        REFERENCES public.game (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT player_id FOREIGN KEY (player_id)
        REFERENCES public.player (player_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)


TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.appearance_old
    OWNER to wpepkodmgckzze;