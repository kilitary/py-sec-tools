rule _Upack_0_1x_0_20_0_21_0_24_beta__Dwing_euyrve
{
	meta:
		description = "Upack 0_1x  0_20  0_21  0_24 beta __ Dwing"
	strings:
		$a = {BE?8014000AD8BF8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
