rule _ASPack_v1_07b_ghvnsq
{
	meta:
		description = "ASPack v1_07b"
	strings:
		$a = {90909075??E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
