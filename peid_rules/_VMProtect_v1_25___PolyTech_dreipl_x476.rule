rule __VMProtect_v1_25___PolyTech_dreipl
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC5B9D5F585E5A5B595D59C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
