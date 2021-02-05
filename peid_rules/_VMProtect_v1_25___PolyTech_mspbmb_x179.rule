rule __VMProtect_v1_25___PolyTech_mspbmb
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A0666989883ED048D7601894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
