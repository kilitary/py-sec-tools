rule __VMProtect_v1_25___PolyTech_gohrut
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A0683C60166989883ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
