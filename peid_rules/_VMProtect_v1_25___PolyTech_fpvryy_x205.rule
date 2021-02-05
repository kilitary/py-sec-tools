rule __VMProtect_v1_25___PolyTech_fpvryy
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????668B0683ED02668945008D7602E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
