rule __VMProtect_v1_25___PolyTech_eovzhd
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????55515253509C57565468000000008B74242C89E581ECC000000089E70375008A068D76010FB6C08D0C85????????FF2189E883ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
