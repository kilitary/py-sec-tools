rule __VMProtect_v1_25___PolyTech_usqtkh
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5755519C555253565068000000008B74242C89E581ECC000000089E70375008A068D76010FB6C08D0C85????????FF218B45008B00894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
