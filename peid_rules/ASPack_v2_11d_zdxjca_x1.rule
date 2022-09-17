rule _ASPack_v2_11d_zdxjca
{
	meta:
		description = "ASPack v2_11d"
	strings:
		$a = {60E802000000CD20E8000000005E2BC9587402}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
