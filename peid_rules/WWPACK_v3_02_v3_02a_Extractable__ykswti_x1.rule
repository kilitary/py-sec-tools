rule _WWPACK_v3_02_v3_02a_Extractable__ykswti
{
	meta:
		description = "WWPACK v3_02_ v3_02a _Extractable_"
	strings:
		$a = {B8????8CCA03D08CC981C1????5133C9B1??510606BB????538CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
