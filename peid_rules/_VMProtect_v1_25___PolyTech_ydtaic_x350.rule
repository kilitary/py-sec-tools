rule __VMProtect_v1_25___PolyTech_ydtaic
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC595A5F5F585E5D9D595BC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
