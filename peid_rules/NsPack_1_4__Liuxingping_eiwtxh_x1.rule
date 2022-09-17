rule _NsPack_1_4__Liuxingping_eiwtxh
{
	meta:
		description = "NsPack 1_4 __ Liuxingping"
	strings:
		$a = {9C60E8000000005DB8????40002D????4000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
