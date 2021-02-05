rule __VMProtect_v1_25___PolyTech_veztiw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????8A068A040783ED0283EEFF66894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
