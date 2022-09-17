rule __VMProtect_v1_25___PolyTech_utchhj
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????668B450083ED02660145049C8F4500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
