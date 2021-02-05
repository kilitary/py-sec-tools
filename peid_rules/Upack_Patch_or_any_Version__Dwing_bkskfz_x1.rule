rule _Upack_Patch_or_any_Version__Dwing_bkskfz
{
	meta:
		description = "Upack_Patch or any Version __ Dwing"
	strings:
		$a = {60E809000000??????00E90602}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
