rule _WWPACK_v3_03_yfmrcl
{
	meta:
		description = "WWPACK v3_03"
	strings:
		$a = {B8????8CCA03D08CC981C1????51B9????510606BB????53}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
