rule __VMProtect_v1_25___PolyTech_yegeds
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????9C525651575350555168000000008B74242C89E581ECC000000089E70375008A06460FB6C0FF2485????????89E883ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
