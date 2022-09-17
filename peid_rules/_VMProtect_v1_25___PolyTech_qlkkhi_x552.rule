rule __VMProtect_v1_25___PolyTech_qlkkhi
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5250559C515651535768000000008B74242C89E581ECC000000089E70375008A0683EEFF0FB6C08D0C85????????FF2189E883ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
