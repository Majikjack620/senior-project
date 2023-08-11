SELECT *, count(games) FROM halo_comp GROUP BY comp_game

CREATE OR REPLACE FUNCTION public.f_epoch_to_datetime(epoch int8) RETURNS timestamp LANGUAGE plpythonu IMMUTABLE AS $$

	from datetime import datetime
	return datetime.fromtimestamp(epoch // 1000)

$$;

CREATE OR REPLACE
FUNCTION hello(world int8, goodbye string
	RETURNS int8
	LANGUAGE plpythonu IMMUTABLE
	AS $$

			import datetime
			return datetime
$$
;
