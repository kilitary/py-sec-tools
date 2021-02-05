rule _ASPack_v1_06b_sqlfja
{
	meta:
		description = "ASPack v1_06b"
	strings:
		$a = {9061BE????????8DBE????????5783CDFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
