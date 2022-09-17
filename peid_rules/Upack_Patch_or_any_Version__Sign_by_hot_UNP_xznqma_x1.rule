rule _Upack_Patch_or_any_Version__Sign_by_hot_UNP_xznqma
{
	meta:
		description = "Upack_Patch or any Version __ Sign by hot_UNP"
	strings:
		$a = {60E80900000017CD0000E90602}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
