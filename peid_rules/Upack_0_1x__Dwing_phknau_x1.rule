rule _Upack_0_1x__Dwing_phknau
{
	meta:
		description = "Upack 0_1x __ Dwing"
	strings:
		$a = {BE48014000AD8BF8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
