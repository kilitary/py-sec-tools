rule __VMProtect_v1_25___PolyTech_ocjirs
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B5F5A585E5D5B9D595DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
