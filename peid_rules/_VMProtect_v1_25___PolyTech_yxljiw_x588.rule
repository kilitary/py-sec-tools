rule __VMProtect_v1_25___PolyTech_yxljiw
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????535051519C5257555668000000008B74242C89E581ECC000000089E70375008A06460FB6C0FF2485????????8B0683ED0483EEFC894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
