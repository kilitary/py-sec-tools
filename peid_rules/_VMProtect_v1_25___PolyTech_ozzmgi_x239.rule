rule __VMProtect_v1_25___PolyTech_ozzmgi
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A0666989883ED0446894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
