rule __VMProtect_v1_25___PolyTech_qwtpmk
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????660FB70683EEFE9883ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
