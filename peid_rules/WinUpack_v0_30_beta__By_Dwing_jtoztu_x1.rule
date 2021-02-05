rule _WinUpack_v0_30_beta__By_Dwing_jtoztu
{
	meta:
		description = "WinUpack v0_30 beta __ By Dwing"
	strings:
		$a = {E9????????42794477696E6740000000504500004C0102}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
