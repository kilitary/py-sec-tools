rule __VMProtect_v1_25___PolyTech_dbxexy
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????5153565251509C575568000000008B74242C89E581ECC000000089E70375008A060FB6C046FF2485????????8B4500668B550483C506668910E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
