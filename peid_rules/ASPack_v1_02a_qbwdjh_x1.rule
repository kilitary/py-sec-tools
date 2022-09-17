rule _ASPack_v1_02a_qbwdjh
{
	meta:
		description = "ASPack v1_02a"
	strings:
		$a = {60E8????????5D81ED06??????64A023}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
