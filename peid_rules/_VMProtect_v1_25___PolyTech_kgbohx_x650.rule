rule __VMProtect_v1_25___PolyTech_kgbohx
{
	meta:
		description = "_ VMProtect v1_25 ___ PolyTech"
	strings:
		$a = {68????????E8????????9C575552545051535668000000008B74242C89E581ECC000000089E70375008A06460FB6C08D0C85????????FF2189E883ED04894500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
