rule __VMProtect_v1_25___PolyTech_befmxu
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????89EC585A9D5B595D5F585E5EC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
