rule _ASPack_v2_11b_embmwb
{
	meta:
		description = "ASPack v2_11b"
	strings:
		$a = {60E802000000EB095D55}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
