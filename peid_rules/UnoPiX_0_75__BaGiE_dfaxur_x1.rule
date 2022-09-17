rule _UnoPiX_0_75__BaGiE_dfaxur
{
	meta:
		description = "UnoPiX 0_75 __ BaGiE"
	strings:
		$a = {60E8070000006168????4000C383042418C32083B8ED2037EFC6B979379E61}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
