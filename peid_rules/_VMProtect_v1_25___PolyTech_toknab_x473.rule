rule __VMProtect_v1_25___PolyTech_toknab
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B9D595A5B585B5F5E5DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
