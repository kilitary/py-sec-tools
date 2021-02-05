rule _ASPack_v1_02b_tlhdtu
{
	meta:
		description = "ASPack v1_02b"
	strings:
		$a = {60E8000000005D81ED96784300B89078430003C5}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
