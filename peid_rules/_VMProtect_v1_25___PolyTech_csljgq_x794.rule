rule __VMProtect_v1_25___PolyTech_csljgq
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????555052519C5753525668000000008B74242C89E581ECC000000089E70375008A06460FB6C0FF3485????????C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
