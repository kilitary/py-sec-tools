rule _ASPack_v2_12_aaltis
{
	meta:
		description = "ASPack v2_12"
	strings:
		$a = {60E803000000E9EB045D4555C3E801}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
