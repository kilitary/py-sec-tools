rule _Upack_v0_32_Beta__Dwing_tszwwy
{
	meta:
		description = "Upack v0_32 Beta __ Dwing"
	strings:
		$a = {BE8801????AD50??AD91??F3A5}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
