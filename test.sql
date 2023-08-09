SELECT game,
       MODE,
       MONEY
FROM halo_comp
WHERE game == "CTF";


CREATE OR REPLACE FUNCTION public.f_epoch_to_datetime(epoch int8) RETURNS timestamp LANGUAGE plpythonu IMMUTABLE AS $$

	from datetime import datetime
	return datetime.fromtimestamp(epoch // 1000)

$$ ;