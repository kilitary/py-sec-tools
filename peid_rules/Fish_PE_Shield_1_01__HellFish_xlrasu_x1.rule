rule _Fish_PE_Shield_1_01__HellFish_xlrasu
{
	meta:
		description = "Fish PE Shield 1_01 __ HellFish"
	strings:
		$a = {60E812FEFFFFC390090000002C000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
