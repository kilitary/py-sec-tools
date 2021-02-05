rule _Upack_V0_36__Dwing_bnydfv
{
	meta:
		description = "Upack V0_36 __ Dwing"
	strings:
		$a = {BE????????FF36E9C3000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
