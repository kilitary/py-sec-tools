rule _Fish_PE_Shield_1_121_16__HellFish_cwhgik
{
	meta:
		description = "Fish PE Shield 1_121_16 __ HellFish"
	strings:
		$a = {60E8EAFDFFFFFFD0C38D4000??0000002C000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
