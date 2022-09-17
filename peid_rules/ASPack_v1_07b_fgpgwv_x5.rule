rule _ASPack_v1_07b_fgpgwv
{
	meta:
		description = "ASPack v1_07b"
	strings:
		$a = {60E8????????5D81ED????????60E82B030000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
