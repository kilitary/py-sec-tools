rule __VMProtect_v1_25___PolyTech_hubqpi
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5A5D595D5F585E5B9DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
