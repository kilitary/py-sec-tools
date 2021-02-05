rule __VMProtect_v1_25___PolyTech_jwrycd
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????515257535556509C5768000000008B74242C89E581ECC000000089E70375008A0683EEFF0FB6C08D0C85????????FF218B45008B00894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
