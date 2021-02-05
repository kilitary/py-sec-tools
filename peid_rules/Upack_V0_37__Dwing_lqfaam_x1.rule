rule _Upack_V0_37__Dwing_lqfaam
{
	meta:
		description = "Upack V0_37 __ Dwing"
	strings:
		$a = {BE????????AD50FF????EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
