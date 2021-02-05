rule __VMProtect_v1_25___PolyTech_mmjklp
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5250539C555154565768000000008B74242C89E581ECC000000089E70375008A06460FB6C08D0C85????????FF218B750083C504E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
