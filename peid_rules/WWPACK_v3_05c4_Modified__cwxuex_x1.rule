rule _WWPACK_v3_05c4_Modified__cwxuex
{
	meta:
		description = "WWPACK v3_05c4 _Modified_"
	strings:
		$a = {B8????8CCA03D08CC981C1????51B9????510606B1??518CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
