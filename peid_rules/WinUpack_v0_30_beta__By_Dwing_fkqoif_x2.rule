rule _WinUpack_v0_30_beta__By_Dwing_fkqoif
{
	meta:
		description = "WinUpack v0_30 beta __ By Dwing"
	strings:
		$a = {E9????????42794477696E674000000050450000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
