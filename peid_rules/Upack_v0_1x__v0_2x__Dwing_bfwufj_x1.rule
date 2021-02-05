rule _Upack_v0_1x__v0_2x__Dwing_bfwufj
{
	meta:
		description = "Upack v0_1x _ v0_2x __ Dwing"
	strings:
		$a = {BE8801????AD8BF895}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
