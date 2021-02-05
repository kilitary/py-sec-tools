rule _ASPack_v1_08_02_hwzodl
{
	meta:
		description = "ASPack v1_08_02"
	strings:
		$a = {90750190E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
