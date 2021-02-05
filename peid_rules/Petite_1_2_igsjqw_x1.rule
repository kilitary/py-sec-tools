rule _Petite_1_2_igsjqw
{
	meta:
		description = "Petite 1_2"
	strings:
		$a = {669C60E8CA000000030004000500060007000800}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
